from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    # path('checkout/', views.checkout, name='checkout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
]