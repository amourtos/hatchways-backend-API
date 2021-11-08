from django.conf.urls import include, url


from rest_framework import routers

from api.views import RecipeViewSet

router = routers.DefaultRouter()

router.register('recipe', RecipeViewSet, basename='recipe')

urlpatterns = [
    url(r"^api/", include(router.urls))
]
