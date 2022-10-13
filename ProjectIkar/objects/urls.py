from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('objects/', include('objects.urls')),
    path('admin/', admin.site.urls),
]
