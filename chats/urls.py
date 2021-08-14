from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path("chat/<str:room_name>/", views.Room, name='room'),
    # AUTH
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('logout/', views.logoutPage, name='logout'),
]
