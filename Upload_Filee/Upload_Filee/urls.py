from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/', include('authentication.urls')),
    path('', include('Fileupload.urls')),
]
