from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('', views.home, name='home'),
     path('properties/', views.property_list, name='property_list'),
      path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('contact_us/', views.contact_us, name='contact_us'),
     path('blog/', views.blog_list, name='blog_list'),
     path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # Other URL patterns for the "listing" app
]