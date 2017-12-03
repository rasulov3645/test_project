from django.contrib import admin

# Register your models here.

from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        module = Status

admin.site.register(Status, StatusAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        module = Order

admin.site.register(Order, OrderAdmin)



class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        module = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


