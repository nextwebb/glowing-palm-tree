from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import UserViewSet

# base project url patterns
# django provides an easy to use router for all your apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<version>/', include('api.urls')),
    # django provides a default usermodel
    path('api/<version>/auth/login/', obtain_auth_token),
    path('api/<version>/auth/signup/', UserViewSet)

]
