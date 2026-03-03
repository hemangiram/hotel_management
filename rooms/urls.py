from django.urls import path
from . import views




urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('<int:pk>/', views.room_detail, name='room_detail'),
    path('add/',views.room_create, name='room_create'),
    path('edit/<int:pk>/', views.room_update, name='room_update'),
    path('delete/<int:pk>/', views.room_delete, name='room_delete'),
    

]