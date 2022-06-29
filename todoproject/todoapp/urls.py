from . import views
from django.urls import path, include

app_name = 'todoapp'
urlpatterns = [

    path('', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.tasklistView.as_view(), name='listView'),
    path('cbvdetail/<int:pk>/', views.taskDetailView.as_view(), name='taskDetailView'),
    path('cbvupdate/<int:pk>/', views.taskUpdateView.as_view(), name='taskUpdateView'),
    path('cbvdelete/<int:pk>/', views.taskDeleteView.as_view(), name='taskDeleteView'),
]

