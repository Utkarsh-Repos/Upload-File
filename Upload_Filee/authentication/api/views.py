from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

from .serializers import SignUpSerializer
from django.conf import settings

class SignUpView(APIView):
    """
    Handles user registration (sign-up) requests.

    On successful registration, it returns a JWT pair (refresh and access tokens).
    """
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new user and create a refresh token
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Handles user login requests.

    Authenticates the user and returns a JWT pair (refresh and access tokens) if credentials are valid.
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        # Authenticate the user using email and password
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TokenRefreshView(APIView):
    """
    Handles the refresh of JWT tokens.

    Requires a refresh token to be provided in the request. If valid, it returns a new access token
    and optionally a new refresh token.
    """
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decode the refresh token
            refresh = RefreshToken(refresh_token)

            # Get user from the token's 'user_id' claim
            user_id = refresh['user_id']
            user = User.objects.get(id=user_id)

            # Generate a new access token
            access = str(refresh.access_token)

            # Optionally, issue a new refresh token if using rotation
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                new_refresh = RefreshToken.for_user(user)
                return Response({
                    'access': access,
                    'refresh': str(new_refresh),
                })

            return Response({
                'access': access
            })

        except (TokenError, User.DoesNotExist) as e:
            # Handle invalid or expired token, or user not found
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)