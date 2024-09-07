from django.db.models import Sum, F
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal, InvalidOperation
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render
import pandas as pd

from .models import Product


def login(request):
    """
    Renders the login page.
    """
    return render(request,'../templates/login.html',{})

def signup(request):
    """
    Renders the signup page.
    """
    return render(request,'../templates/signup.html',{})


@csrf_exempt
def file_upload(request):
    """
    Handles CSV file uploads to update or create Product records in the database.

    CSV file should include columns: product_id, product_name, category, price, quantity_sold, rating, review_count.
    - Missing prices and quantities are filled with median values.
    - Missing ratings are filled with the mean rating of the category.
    """
    if request.method == 'POST' and request.FILES.get('csv-file'):
        file = request.FILES['csv-file']
        df = pd.read_csv(file)

        # Fill missing values
        df['price'].fillna(df['price'].median(), inplace=True)
        df['quantity_sold'].fillna(df['quantity_sold'].median(), inplace=True)
        df['rating'] = df.groupby('category')['rating'].transform(lambda x: x.fillna(x.mean()))

        # Convert columns to numeric types
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['quantity_sold'] = pd.to_numeric(df['quantity_sold'], errors='coerce')
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce')


        try:
            for _, row in df.iterrows():
                # Convert to appropriate data types with error handling
                try:
                    price = Decimal(row['price']) if not pd.isna(row['price']) else Decimal('0.00')
                except InvalidOperation:
                    price = Decimal('0.00')

                try:
                    quantity_sold = int(row['quantity_sold']) if not pd.isna(row['quantity_sold']) else 0
                except ValueError:
                    quantity_sold = 0

                try:
                    rating = Decimal(row['rating']) if not pd.isna(row['rating']) else Decimal('0.00')
                except InvalidOperation:
                    rating = Decimal('0.00')

                # Update or create Product record
                product, created = Product.objects.update_or_create(
                    product_id=row['product_id'],
                    defaults={
                        'product_name': row['product_name'],
                        'category': row['category'],
                        'price': price,
                        'quantity_sold': quantity_sold,
                        'rating': rating,
                        'review_count': row['review_count']
                    }
                )
        except Exception as e:
            print('issue in data saving>>>>',str(e))
            return JsonResponse({'message': 'An error occurred while processing the file.'}, status=500)

        return render(request,'file_upload_portal.html',{'message': 'success'})

    return render(request, 'file_upload_portal.html', {})


@csrf_exempt
def generate_summary_report(request):
    """
    Generates and returns a CSV summary report of product sales by category.

    The report includes:
    - Category name
    - Total revenue for the category
    - Top product in terms of quantity sold within the category
    """
    if request.method == 'POST':
        categories = Product.objects.values('category').distinct()
        data = []

        for category in categories:
            category_name = category['category']

            # Calculate total revenue for the category
            total_revenue = Product.objects.filter(category=category_name).aggregate(
                total_revenue=Sum(F('price') * F('quantity_sold'))
            )['total_revenue'] or 0

            # Find the top product in terms of quantity sold
            top_product = Product.objects.filter(category=category_name).order_by(
                '-quantity_sold'
            ).first()

            top_product_name = top_product.product_name if top_product else ''
            top_product_quantity_sold = top_product.quantity_sold if top_product else 0

            data.append({
                'category': category_name,
                'total_revenue': total_revenue,
                'top_product': top_product_name,
                'top_product_quantity_sold': top_product_quantity_sold
            })

        # Create a DataFrame and generate CSV response
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="summary_report.csv"'
        df.to_csv(path_or_buf=response, index=False)

        return response
    else:
        return render(request, 'generate-report.html', {})
