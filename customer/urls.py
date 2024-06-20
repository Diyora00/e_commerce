from django.urls import path
from customer.views import *


urlpatterns = [
    path('customers/', show_customers, name='customers'),
    path('customer_details/int<customer_id>', customer_details, name='customer_details'),
    path('add_customer/', add_customer, name='add_customer'),
    path('delete_customer/<customer_id>', delete_customer, name='delete_customer'),
    path('update_customer/<customer_id>', update_customer, name='update_customer'),
]
