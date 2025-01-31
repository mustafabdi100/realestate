# Generated by Django 5.0.3 on 2024-03-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_property_description_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('query_type', models.CharField(choices=[('rent', 'Rent house'), ('resident', 'Resident'), ('apartment', 'Apartment'), ('sale', 'Sale property')], default='rent', max_length=10)),
                ('query', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
