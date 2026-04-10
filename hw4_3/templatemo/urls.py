from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
   path('admin/', admin.site.urls),
]
urlpatterns = [
    path("", views.index, name="maison-templatemo"),
    path('admin/', admin.site.urls),
]