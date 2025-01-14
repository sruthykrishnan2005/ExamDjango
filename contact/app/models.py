from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    alternative = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='contact_images/', blank=True, null=True)

