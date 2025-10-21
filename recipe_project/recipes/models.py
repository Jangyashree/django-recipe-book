from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to="recipe")

    def __str__(self):
        return self.title