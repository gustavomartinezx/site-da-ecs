from django.urls import path
from . import views


app_name = 'extensionistas'


urlpatterns = [
    path('', views.home, name='home'),
]