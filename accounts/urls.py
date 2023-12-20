from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.registrationPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout' ),
    path('admin-dashboard/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.create_order, name='order_form'),
    path('update_order/<str:pk>/', views.updateOrder, name='update'),
    path('delete/<str:pk>/', views.deleteOrder, name='delete'),
    path('', views.userPage, name="user"),
    path('settings/', views.accountSettings, name="settings"),

    path("reset_password/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name="password_reset_confirm"),

    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_complete"),
    
]

