from django.urls import path
from . import views


urlpatterns = [
    path('todo_list', views.todo_list, name='todo_list'),
    path('about/', views.about, name='about'),
    path('about2/', views.about2, name='about2'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),    
    path('uncross/<list_id>', views.uncross, name='uncross'),    
    path('edit/<list_id>', views.edit, name='edit'),    
]
