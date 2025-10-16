from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to="recipe")

    def __str__(self):
        return self.title