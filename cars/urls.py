from django.urls import path

from cars.apps import CarsConfig
from cars.views import (CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView)

app_name = CarsConfig.name

urlpatterns = [
    path('', CarListView.as_view(), name='product_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='product_detail'),
    path('cars/create', CarCreateView.as_view(), name='product_create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='product_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='product_delete'),

]

