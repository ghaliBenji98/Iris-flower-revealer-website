from django.urls import path
from. import views

urlpatterns = [
    path('', views.flowerNature, name='model'),
]
