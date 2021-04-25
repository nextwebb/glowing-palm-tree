from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, CharacterViewSet

router = routers.DefaultRouter()
router.register('auth/signup', UserViewSet)
router.register('characters', CharacterViewSet, basename='characterModel')
# router.register('favourites', FavouritesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
