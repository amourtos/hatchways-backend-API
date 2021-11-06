from django.contrib import admin
from recipe.models import Recipe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.


class RecipeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(Recipe, RecipeAdmin)
