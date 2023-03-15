from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('create_post/', views.create_post, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('post_list/', views.post_list, name='customer'),
    path('post_list/<str:category>/',views.patient_dashboard,name='customer'),
]