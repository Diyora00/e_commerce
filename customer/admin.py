from django.contrib import admin

from customer.models import Customer


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'is_active',]
    search_fields = ['id', 'email']
    list_filter = ['joined', 'is_active']
