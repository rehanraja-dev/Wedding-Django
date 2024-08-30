from django.contrib import admin
from .models import MANAGER,MANAGER_VENDER_BOOKING,MANAGER_VENUE_BOOKING,MANAGER_CAKE_BOOKING,MANAGER_BOOKING
# Register your models here.

@admin.register(MANAGER)
class admin_manager(admin.ModelAdmin):
    list_display=['user','mobile','state','city']
    list_filter=['state','city']

@admin.register(MANAGER_VENUE_BOOKING)
class admin_manager_venue(admin.ModelAdmin):
    list_display=['manager','user','venue','order_date','status']
    list_filter=['manager','order_date','status']

@admin.register(MANAGER_VENDER_BOOKING)
class admin_manager_vender(admin.ModelAdmin):
    list_display=['manager','user','vender','order_date','status']
    list_filter=['manager','order_date','status']

@admin.register(MANAGER_CAKE_BOOKING)
class admin_manager_cake(admin.ModelAdmin):
    list_display=['manager','user','cake','order_date','status']
    list_filter=['manager','order_date','status']

@admin.register(MANAGER_BOOKING)
class admin_manager_booking(admin.ModelAdmin):
    list_display=['manager','user','order_date','status']
    list_filter=['manager','order_date','status']