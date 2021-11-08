from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from api.serializers import RecipeSerializer
from recipe.models import Recipe


@action(methods=['get'], detail=False)
class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def newset(self, request):
        recipe_list = self.get_queryset()
        serializer = self.get_serializer_class()(recipe_list)
        return Response(serializer.data)
