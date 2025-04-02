from django.urls import path
from . import api

urlpatterns = [
    path( '',api.properties_list, name='properties_list'),
    path('create/', api.create_property, name='api_create_property'),
    path('<uuid:pk>/', api.properties_detail, name='api_properties_detail'),
    path('<uuid:pk>/book/', api.book_prorperty, name='api_book_prorperty'),
    path('<uuid:pk>/reservations/', api.property_reservations, name='api_property_reservations'),
]