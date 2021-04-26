from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import UserViewSet

# base project url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<version>/', include('api.urls')),
    path('api/<version>/auth/login/', obtain_auth_token),
    path('api/<version>/auth/signup/', UserViewSet)

]
