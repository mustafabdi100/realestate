from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.IntegerField(help_text="Square feet")
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking_slots = models.IntegerField(default=1)
    image = models.ImageField(upload_to='properties', null=True)

    def __str__(self):
        return self.title
    

class Inquiry(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry by {self.name} on {self.property}"
    
class Contact(models.Model):
    QUERY_TYPE_CHOICES = [
        ('rent', 'Rent house'),
        ('resident', 'Resident'),
        ('apartment', 'Apartment'),
        ('sale', 'Sale property'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    query_type = models.CharField(max_length=10, choices=QUERY_TYPE_CHOICES, default='rent')
    query = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_query_type_display()} inquiry from {self.name}"



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title
