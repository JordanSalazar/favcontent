from django.urls import path
from . import views

urlpatterns = [
    # Vista principal de artículos
    path('', views.article_list, name='list'),
    
    # CRUD de artículos
    path('nuevo/', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name='detail'),
    path('<slug:slug>/editar/', views.article_update, name='update'),
    path('<slug:slug>/eliminar/', views.article_delete, name='delete'),
    
    # Vistas para categorías
    # path('categorias/', views.category_list, name='category_list'),
    # path('categorias/<slug:slug>/', views.category_detail, name='category_detail'),
] 