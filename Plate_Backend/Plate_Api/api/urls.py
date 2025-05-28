from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views


urlpatterns = [
    path('detect', views.PlateView.as_view(), name='plate-view'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api-token-auth',  obtain_auth_token, name='api_token_auth'),
]
