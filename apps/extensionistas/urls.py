from django.urls import path
from . import views

app_name = 'extensionistas'

urlpatterns = [
    path('home/', views.extensionista_list, name='extensionista_list'),
    path('novo/', views.extensionista_create, name='extensionista_create'),
    path('editar/<int:pk>/', views.extensionista_update, name='extensionista_update'),
    path('deletar/<int:pk>/', views.extensionista_delete, name='extensionista_delete'),
]