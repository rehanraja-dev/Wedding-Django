from django.contrib import admin

from .models import Venue_Provider, Venue_Type, Vender_Type, Venders, Venue_Cart, Vender_Cart, Venue_Booking, Vender_Booking, Venue_Rating, Vender_Rating,Venue_Wishlist,Vender_Wishlist

@admin.register(Venue_Type)
class admin_venuetype(admin.ModelAdmin):
    list_display=['venue_type']

@admin.register(Venue_Provider)
class admin_venue(admin.ModelAdmin):
    list_display=['venue_name','mobile','state','city','Venue_Type']
    list_filter = ['state','city','Venue_Type']

@admin.register(Vender_Type)
class admin_vendertype(admin.ModelAdmin):
    list_display = ['vender_type']

@admin.register(Venders)
class admin_vender(admin.ModelAdmin):
    list_display = ['vender_name', 'mobile', 'state','city', 'vender_type']
    list_filter = ['state','city','vender_type']


@admin.register(Venue_Cart)
class admin_venuecart(admin.ModelAdmin):
    list_display = ['user', 'venue']
    list_filter = ['user','venue']

@admin.register(Vender_Cart)
class admin_vendercart(admin.ModelAdmin):
    list_display = ['user', 'vender']



@admin.register(Venue_Wishlist)
class admin_venuewishlist(admin.ModelAdmin):
    list_display = ['user', 'venue']

@admin.register(Vender_Wishlist)
class admin_venderwishlist(admin.ModelAdmin):
    list_display = ['user', 'vender']



@admin.register(Venue_Booking)
class admin_venuebooking(admin.ModelAdmin):
    list_display = ['user','orderdate', 'venue','status']


@admin.register(Vender_Booking)
class admin_venderbooking(admin.ModelAdmin):
    list_display = ['user','orderdate', 'vender','status']

#
#@admin.register(Venue_Rating)
#class admin_venuerating(admin.ModelAdmin):
#    list_display = ['user','venue','rating']
#
#@admin.register(Vender_Rating)
#class admin_venderrating(admin.ModelAdmin):
#    list_display = ['user','vender','rating']
#    list_filter = ['rating','vender','user']
#