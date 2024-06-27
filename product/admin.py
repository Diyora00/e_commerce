from django.contrib import admin
from product.models import *


# Register your models here.
# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttributeValue)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    search_fields = ('title',)
    list_filter = ('price', )
