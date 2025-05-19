from django.urls import path
from . import views


urlpatterns = [
    path('detect', views.PlateView.as_view(), name='plate-view'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login')
]
