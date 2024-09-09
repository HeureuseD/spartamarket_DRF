from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title