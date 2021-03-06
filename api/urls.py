from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CharacterViewSet, QouteViewSet, FavouritesViewSet

# register api routes
router = routers.DefaultRouter()

router.register('characters', CharacterViewSet, basename='characterModel')
router.register('favourites', FavouritesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
