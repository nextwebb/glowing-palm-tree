from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/<version>/', include('api.urls')),
    path('api/<version>/auth/login/', obtain_auth_token),

]
