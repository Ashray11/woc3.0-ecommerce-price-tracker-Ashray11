from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('Flipkart/', views.flipkart, name="flipkartsite"),
    path('Amazon/', views.amazon, name="amazonsite"),
    path('Snapdeal/', views.snapdeal, name="snapdealsite"),
]
