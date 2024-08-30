from django.contrib import admin
from .models import CAKE_FLAVOUR,CAKE_PROVIDER,CAKE,CAKE_CART,CAKE_WISHLIST,CAKE_BOOKING

@admin.register(CAKE_FLAVOUR)
class admin_CAKE_FLAVOUR(admin.ModelAdmin):
    list_display=['flavour_name']
    list_filter=['flavour_name']

@admin.register(CAKE_PROVIDER)
class admin_CAKE_provider(admin.ModelAdmin):
    list_display=['cakep_name','mobile','state','city']
    list_filter=['state','city']

@admin.register(CAKE)
class admin_CAKE(admin.ModelAdmin):
    list_display=['cake_name','flavour','provider','price','color']
    list_filter=['flavour','provider','color',]

@admin.register(CAKE_CART)
class admin_CAKE_cart(admin.ModelAdmin):
    list_display=['user','cake']
    list_filter=['user']

@admin.register(CAKE_WISHLIST)
class admin_CAKE_wishlist(admin.ModelAdmin):
    list_display=['user','cake']
    list_filter=['user']

@admin.register(CAKE_BOOKING)
class admin_CAKE_booking(admin.ModelAdmin):
    list_display=['user','cake','order_date','status']
    list_filter=['user','status','order_date']
