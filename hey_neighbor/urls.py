from django.urls import paths
from . import views

app_name = 'hey_neighbor'

urlpatterns = [
    path('', views.index, name='index'),
]
