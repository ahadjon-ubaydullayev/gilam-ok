
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('clients', client, name='clients'),
    path('add_clients', add_client, name='add_clients'),
    path('add_product', add_product, name='add_product'),
    path('add-raw', add_raw_material, name='add_raw_material'),
    path('edit_clients/<int:id>', edit_client, name='edit_clients'),
    path('edit_material/<int:id>', edit_material, name='edit_material'),
    path('edit_product/<int:id>', edit_product, name='edit_product'),
    path('delete_clients/<int:id>', delete_client),
    path('delete_material/<int:id>', delete_material),
    path('delete_product/<int:id>', delete_product),
    path('raw_material', raw_material, name='rawmaterials'),
    path('login/', user_login, name='login'),
]
