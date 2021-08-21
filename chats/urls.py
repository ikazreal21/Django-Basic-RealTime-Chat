from django.urls import path

from . import views

urlpatterns = [
    path('', views.Fronpage, name='frontpage'),
    path('dashboard/', views.Index, name='index'),
    path("chat/<str:room_name>/", views.Room, name='room'),
    path("room", views.EnterRoom, name='enterroom'),
    # Save Room
    path("savedroom", views.SaveRoom, name='saveroom'),
    # AUTH
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('logout/', views.logoutPage, name='logout'),
]
