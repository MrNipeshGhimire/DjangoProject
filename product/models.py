from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100,blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)