from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('all/', views.booking_list, name='booking_list'),
    path('confirm/<int:pk>/', views.confirm_booking, name='confirm_booking'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]