from django.db import models

# Create your models here.
class Men(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=100)
    price=models.CharField(max_length=20)
    