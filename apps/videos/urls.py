from django.urls import path
from . import views

urlpatterns = [
    # Vista principal de videos
    path('', views.video_list, name='list'),
    
    # CRUD de videos
    path('nuevo/', views.video_create, name='create'),
    path('<slug:slug>/', views.video_detail, name='detail'),
    path('<slug:slug>/editar/', views.video_update, name='update'),
    path('<slug:slug>/eliminar/', views.video_delete, name='delete'),
] 