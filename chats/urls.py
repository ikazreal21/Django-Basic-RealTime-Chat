from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path("chat/<str:room_name>/", views.Room, name='room'),
]
