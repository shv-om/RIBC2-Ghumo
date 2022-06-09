from django.urls import path, include
from . import views
from knox import views as knox_views

app_name = 'registration'

urlpatterns = [
    path('', include('knox.urls')),
    path('register/seller', views.SellerSignUpAPI.as_view(), name="seller"),
    path('login', views.SignInAPI.as_view(), name="login"),
    path('user', views.MainUser.as_view()),
    path('logout',knox_views.LogoutView.as_view(), name="knox-logout"),
]