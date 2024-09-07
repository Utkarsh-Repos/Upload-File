from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('file-upload/', views.file_upload, name='file-upload'),
    path('generate-report/', views.generate_summary_report, name='generate-report'),

]
