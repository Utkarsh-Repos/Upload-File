from django.urls import path
from .views import (SignUpView,
                    LoginView,
                    TokenRefreshView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),

]