from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.movie_create, name='movie_create'),
    path('<slug:slug>/edit/', views.movie_update, name='movie_update'),
    path('<slug:slug>/delete/', views.movie_delete, name='movie_delete'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
]