from django.urls import path
from . import views

urlpatterns = [
    # Vista principal de libros
    path('', views.book_list, name='list'),
    
    # CRUD de libros
    path('nuevo/', views.book_create, name='create'),
    path('<slug:slug>/', views.book_detail, name='detail'),
    path('<slug:slug>/editar/', views.book_update, name='update'),
    path('<slug:slug>/eliminar/', views.book_delete, name='delete'),
    
    # Vistas para géneros
    # path('generos/', views.genre_list, name='genre_list'),
    # path('generos/<slug:slug>/', views.genre_detail, name='genre_detail'),
] 