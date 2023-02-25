from django.contrib import admin
from shop.models import *


@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('id', 'name')


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('id', 'name')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ordering = ['user__username']
    list_display = ('id', 'user', 'registered_at')


@admin.register(StoreOwner)
class StoreOwnerAdmin(admin.ModelAdmin):
    ordering = ['user__username']
    list_display = ('id', 'user', 'registered_at')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('id', 'name', 'owner', 'store_category')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('id', 'name', 'category', 'price', 'quantity', 'info', 'store')


@admin.register(MyBag)
class MyBagAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'display_items', 'total_price')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'display_items', 'buy_time', 'total_price')
