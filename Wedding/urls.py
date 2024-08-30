"""Wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Wedding import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('wedding', views.Wedding, name='wedding'),
    path('registration', views.Registration, name='registration'),
    path('login', views.Login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgetpassword', views.ForgetPassword, name='forget'),

    path('venues', views.Venue, name='venues'),
    path('venders', views.Vender, name='venders'),
    path('managers', views.Manager, name='managers'),

    path('venueDtls/<uuid:venue_id>', views.VenuesDetails, name='venueDtls'),
    path('venderDtls/<uuid:vender_id>', views.VenderDetails, name='venderDtls'),
    path('cakeDtls/<uuid:cake_id>', views.CakeDetails, name='cakeDtls'),
    path('managerDtls/<uuid:manager_id>', views.ManagerDetails, name='managerDtls'),

    path('order', views.Order, name='order'),

    path('wishlist', views.Wishlist, name='wishlist'),
    path('addvenue_towish/<uuid:venue_id>',
         views.addvenue_towishlist, name='addvenue_towish'),
    path('addvender_towish/<uuid:vender_id>',
         views.addvender_towishlist, name='addvender_towish'),
    path('removevenue_towish/<uuid:venue_id>',
         views.removevenue_towishlist, name='removevenue_towish'),
    path('removevender_towish/<uuid:vender_id>',
         views.removevender_towishlist, name='removevender_towish'),
    path('addcake_towish/<uuid:cake_id>',
         views.addcake_towishlist, name='addcake_towish'),
    path('removecake_towish/<uuid:cake_id>',
         views.removecake_towishlist, name='removecake_towish'),

    path('cart', views.Cart, name='cart'),
    path('addvenue_tocart/<uuid:venue_id>',
         views.addvenue_tocart, name='addvenue_tocart'),
    path('addvender_tocart/<uuid:vender_id>',
         views.addvender_tocart, name='addvender_tocart'),
    path('removevenue_tocart/<uuid:venue_id>',
         views.removevenue_tocart, name='removevenue_tocart'),
    path('removevender_tocart/<uuid:vender_id>',
         views.removevender_tocart, name='removevender_tocart'),
    path('addcake_tocart/<uuid:cake_id>',
         views.addcake_tocart, name='addcake_tocart'),
    path('removecake_tocart/<uuid:cake_id>',
         views.removecake_tocart, name='removecake_tocart'),

    path('profile', views.Profile, name='profile'),
    path('bookvender', views.book_vender, name='bookvender'),
    path('bookvenue', views.book_venue, name='bookvenue'),
    path('bookcake', views.book_cake, name='bookcake'),
    path('bookmanager/<uuid:manager_id>', views.book_manager, name='book_manager'),

    path('bookingvender',views.BookVenderForUser,name='bookvenderforuser'),
    path('search', views.Search, name='search'),
    path('detailsofsevices/<uuid:mb_id>',views.detailsofsevices,name="detailsofsevices"),


    # birthday section urls

    path('birthday', views.Birthday, name='birthday'),
    path('cake', views.Cakes, name='cakes'),
    path('menu', views.Menu, name='menu')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
