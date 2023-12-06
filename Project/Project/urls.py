
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('App.urls')),
    path('v/', admin.site.urls),
]
