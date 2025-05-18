from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store_data, name='store_data'),
    path('delete/<str:tasks_add>/', views.delete_data, name='delete'),
    path('toggle_status/<int:task_id>/', views.toggle_status, name='toggle_status'),
    path('update_task/', views.update_task, name='update_task'),
]


