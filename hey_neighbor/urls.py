from django.urls import path
from . import views

app_name = 'hey_neighbor'

urlpatterns = [
    # path('<int:tool_id>/borrow/', views.borrow, name='borrow'),
    path('neighbors/', views.NeighborView.as_view(), name='neighbors'),
    path('<int:pk>/edittool/', views.EditView.as_view(), name='edit_tool'),
    path('neighbors_tools/', views.MyToolView.as_view(), name='neighbors_tool'),
    path('mytools/', views.MyToolView.as_view(), name='my_tool'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('new/', views.CreateView.as_view(), name='tool_new'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<str:selection>/', views.IndexView.as_view(), name='selection'),
    path('', views.IndexView.as_view(), name='index'),
]
