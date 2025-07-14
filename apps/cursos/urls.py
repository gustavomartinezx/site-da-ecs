from django.urls import path
from . import views


app_name = 'cursos'


urlpatterns = [
    path('', views.curso_list, name='curso_list'),
    path('novo/', views.curso_create, name='curso_create'),
    path('<int:pk>/editar/', views.curso_update, name='curso_update'),
    path('<int:pk>/excluir/', views.curso_delete, name='curso_delete'),
]