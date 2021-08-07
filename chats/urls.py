from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path("<str:room_name>/", views.Room, name='room'),
]
