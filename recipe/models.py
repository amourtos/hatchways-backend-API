from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = ArrayField(models.CharField(
        max_length=20), default=list)
    instructions = ArrayField(models.CharField(
        max_length=20), default=list)

    def __str__(self):
        return self.name
