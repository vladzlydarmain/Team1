from django.db import models

# Create your models here.
class Movie(models.Model):
    image = models.ImageField(upload_to='app3000/movies',blank=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    discrition = models.CharField(max_length=5000)