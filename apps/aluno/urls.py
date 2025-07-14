from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.aluno_list, name='aluno_list'),
    path('novo/', views.aluno_create, name='aluno_create'),
    path('<int:pk>/editar/', views.aluno_update, name='aluno_update'),
    path('<int:pk>/excluir/', views.aluno_delete, name='aluno_delete'),
]