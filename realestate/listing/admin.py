from django.contrib import admin
from .models import Property, Inquiry, Contact, BlogPost

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'area', 'bedrooms', 'bathrooms', 'parking_slots')
    list_filter = ('bedrooms', 'bathrooms', 'parking_slots')
    search_fields = ('title', 'address', 'description')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'property', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'query_type', 'submitted_at')
    list_filter = ('query_type', 'submitted_at')
    search_fields = ('name', 'email', 'query')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'updated_date')
    list_filter = ('published_date', 'updated_date')
    search_fields = ('title', 'content')
