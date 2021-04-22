from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users/signup', UserViewSet)
router.register('characters', CharacterViewSet)
# router.register('favourites', FavouritesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
