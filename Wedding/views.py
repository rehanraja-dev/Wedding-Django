from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from django.conf import settings

from Tables.models import User, Venue_Provider, Venue_Wishlist, Vender_Wishlist, Venders, Venue_Cart, Vender_Cart, Venue_Booking, Vender_Booking, Venue_Rating, Vender_Rating
from Cake.models import CAKE, CAKE_BOOKING, CAKE_CART, CAKE_WISHLIST
from Manager.models import MANAGER,MANAGER_BOOKING,MANAGER_VENDER_BOOKING,MANAGER_VENUE_BOOKING,MANAGER_CAKE_BOOKING

def Home(request):
    return render(request, 'MainHome.html')

# SEARCH FUNCTION
def Search(request):
    if request.method == 'POST':
        search = request.POST.get('search_value')
        results1 = Venders.objects.filter(Q(vender_name__icontains=search) | Q(
            state__icontains=search) | Q(city__icontains=search) | Q(vender_type__vender_type=search))
        results2 = Venue_Provider.objects.filter(Q(venue_name__icontains=search) | Q(
            state__icontains=search) | Q(city__icontains=search) | Q(Venue_Type__venue_type=search))
        result3 = CAKE.objects.filter(Q(flavour__flavour_name__icontains=search) | Q(color__icontains=search) | Q(provider__state__icontains=search) | Q(provider__city__icontains=search) | Q(cake_name__icontains=search))
        data = {'searchvender': results1, 'searchvenue': results2,'searchcake':result3}
        return render(request, "Search.html", data)
    return redirect('wedding')

# WEDDING HOME FUNCTION
def Wedding(request):
    hotels = Venue_Provider.objects.filter(
        Venue_Type__venue_type='5 Star Hotel')
    hotel_count = Venue_Provider.objects.filter(
        Venue_Type__venue_type='5 Star Hotel').count()

    lawns = Venue_Provider.objects.filter(
        Venue_Type__venue_type='Lawn / Farmhouse')
    lawn_count = Venue_Provider.objects.filter(
        Venue_Type__venue_type='Lawn / Farmhouse').count()

    resorts = Venue_Provider.objects.filter(Venue_Type__venue_type='Resort')
    resort_count = Venue_Provider.objects.filter(
        Venue_Type__venue_type='Resort').count()

    photographers = Venders.objects.filter(
        vender_type__vender_type='Photographer')
    photographers_count = Venders.objects.filter(
        vender_type__vender_type='Photographer').count()

    MakeupArtists = Venders.objects.filter(
        vender_type__vender_type='Makeup Artist')
    MakeupArtists_count = Venders.objects.filter(
        vender_type__vender_type='Makeup Artist').count()

    MehndiArtist = Venders.objects.filter(
        vender_type__vender_type='Mehndi Artist')
    MehndiArtist_count = Venders.objects.filter(
        vender_type__vender_type='Mehndi Artist').count()

    blackforest = CAKE.objects.filter(flavour__flavour_name='Black Forest')
    blackforest_count = blackforest.count()

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'hotels': hotels, 'hotel_count': hotel_count, 'lawns': lawns, 'lawn_count': lawn_count, 'resorts': resorts,
            'resort_count': resort_count, 'photographers': photographers, 'photographers_count': photographers_count,
            'MakeupArtists': MakeupArtists, 'MakeupArtists_count': MakeupArtists_count, 'MehndiArtist': MehndiArtist, 
            'MehndiArtist_count': MehndiArtist_count, 'blackforest': blackforest, 'blackforest_count': blackforest_count, 
            'total_item':cart_item}
    return render(request, 'WeddingHome.html', data)

# VENUES PAGE FUNCTION
def Venue(request):
    venue = Venue_Provider.objects.all()
    total_venue = Venue_Provider.objects.all().count()

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'venue': venue, 'total_venue': total_venue, 'total_item': cart_item}
    return render(request, 'Venues.html', data)

# VENDER PAGE FUNCTION
def Vender(request):
    blackforest = CAKE.objects.filter(flavour__flavour_name='Black Forest')
    blackforest_count = blackforest.count()

    photographers = Venders.objects.filter(
        vender_type__vender_type='Photographer')
    photographers_count = Venders.objects.filter(
        vender_type__vender_type='Photographer').count()

    MakeupArtists = Venders.objects.filter(
        vender_type__vender_type='Makeup Artist')
    MakeupArtists_count = Venders.objects.filter(
        vender_type__vender_type='Makeup Artist').count()

    MehndiArtist = Venders.objects.filter(
        vender_type__vender_type='Mehndi Artist')
    MehndiArtist_count = Venders.objects.filter(
        vender_type__vender_type='Mehndi Artist').count()

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'blackforest': blackforest, 'blackforest_count': blackforest_count,
            'photographers': photographers, 'photographers_count': photographers_count,
            'MackeupArtists': MakeupArtists, 'MakeupArtists_count': MakeupArtists_count,
            'MehndiArtist': MehndiArtist, 'MehndiArtist_count': MehndiArtist_count,
            'total_item': cart_item}

    return render(request, 'Venders.html', data)


def Manager(request):
    managers=MANAGER.objects.all()
    manager_count=managers.count()
    data={'managers':managers,'manager_count':manager_count}
    return render(request, 'Manager.html',data)


def VenuesDetails(request, venue_id):
    venue_dtls = Venue_Provider.objects.filter(venue_id=venue_id)

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'venue_dtls': venue_dtls, 'total_item': cart_item}
    return render(request, 'VenueDetailed.html', data)


def VenderDetails(request, vender_id):
    vender_dtls = Venders.objects.filter(vender_id=vender_id)

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'vender_dtls': vender_dtls, 'total_item': cart_item}
    return render(request, 'VenderDetailed.html', data)

def ManagerDetails(request, manager_id):
    manager_dtls = MANAGER.objects.filter(manager_id=manager_id)

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'manager_dtls': manager_dtls, 'total_item': cart_item}
    return render(request, 'ManagerDetails.html', data)


def CakeDetails(request, cake_id):
    cake_dtls = CAKE.objects.filter(cake_id=cake_id)

    # Total item present in user cart.
    cart_item = 0
    if request.user.is_authenticated:
        user=request.user
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        cart_item = venue_count + vender_count + cake_count

    data = {'cake': cake_dtls,'total_item':cart_item}
    return render(request, 'CakeDetailed.html', data)


def Order(request):
    if request.user.is_authenticated:
        user = request.user
        vender_order = Vender_Booking.objects.filter(user=user)
        venue_order = Venue_Booking.objects.filter(user=user)
        cake_order = CAKE_BOOKING.objects.filter(user=user)

        # Total item present in user cart.
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        total_item = venue_count + vender_count + cake_count

        data = {'vender_order': vender_order, 'venue_order': venue_order,
                'cake_order': cake_order, 'total_item': total_item}
        return render(request, 'Order.html', data)

# Code of booking vender without manager.
def book_vender(request):
    user = request.user
    vender_cart = Vender_Cart.objects.filter(user=user)
    for c in vender_cart:
        Vender_Booking(user=user, vender=c.vender).save()
    vender_cart.delete()
    messages.success(request,'Vender successfully booked.')
    return redirect('order')

# Code of booking venue without manager.
def book_venue(request):
    user = request.user
    venue_cart = Venue_Cart.objects.filter(user=user)
    for c in venue_cart:
        Venue_Booking(user=user, venue=c.venue).save()
    venue_cart.delete()
    messages.success(request,'Venue successfully booked.')
    return redirect('order')

# Code of booking cake without manager.
def book_cake(request):
    user = request.user
    cake_cart = CAKE_CART.objects.filter(user=user)
    for c in cake_cart:
        CAKE_BOOKING(user=user, cake=c.cake).save()
    cake_cart.delete()
    messages.success(request,'Cake successfully booked.')
    return redirect('order')

# Code of booking manager.
def book_manager(request,manager_id):
    if request.user.is_authenticated:
        user = request.user
        manager = MANAGER.objects.get(manager_id=manager_id)
        if MANAGER_BOOKING.objects.filter(user=user):
            messages.success(request,'Manager already booked.')
            return redirect('profile')
        else:
            MANAGER_BOOKING(user=user,manager=manager).save()
            messages.success(request,'Manager successfully Booked.')
            return redirect('profile')
    else:
        messages.success(request,' service will open after login.')
        return render(request, 'Login.html')
    
# Code of booking services for customer through the manager.
def BookVenderForUser(request):
    user=request.user
    manager_booking=MANAGER_BOOKING.objects.filter(manager__user=user)
    for i in manager_booking:
        manager= i.manager
    userid = request.POST['user']
    customer = User.objects.get(id=userid)
    vender = Vender_Cart.objects.filter(user=user)
    venue = Venue_Cart.objects.filter(user=user)
    cake = CAKE_CART.objects.filter(user=user)

    for i in vender:
        MANAGER_VENDER_BOOKING(manager=manager,user=customer,vender=i.vender).save()
        MANAGER_VENUE_BOOKING(manager=manager,user=customer,venue=venue).save()
        MANAGER_CAKE_BOOKING(manager=manager,user=customer,cake=cake).save()
    vender.delete()
    venue.delete()
    cake.delete
    messages.success(request,'Services successfully booked.')
    return redirect ('cart')


def Wishlist(request):
    if request.user.is_authenticated:
        user = request.user
        venue_wish = Venue_Wishlist.objects.filter(user=user)
        total_venue = Venue_Wishlist.objects.filter(user=user).count()

        vender_wish = Vender_Wishlist.objects.filter(user=user)
        total_vender = Vender_Wishlist.objects.filter(user=user).count()

        cake_wish = CAKE_WISHLIST.objects.filter(user=user)
        total_cake = CAKE_WISHLIST.objects.filter(user=user).count()

        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        total_item = venue_count + vender_count + cake_count

        data = {'venue_wish': venue_wish, 'vender_wish': vender_wish, 'cake_wish': cake_wish, 'total_venue': total_venue, 'total_vender': total_vender, 'total_cake': total_cake,
                'venue_count': venue_count, 'vender_count': vender_count, 'cake_count': cake_count, 'total_item': total_item}
        return render(request, 'Wishlist.html', data)
    else:
        messages.success(request,'Wishlist service will open after login.')
        return render(request, 'Login.html')


def addvenue_towishlist(request, venue_id):
    if request.user.is_authenticated:
        user = request.user
        venue = Venue_Provider.objects.get(venue_id=venue_id)

        if Venue_Wishlist.objects.filter(venue__venue_id=venue_id).filter(user=user).exists():
            messages.success(request, "Venue already added in wishlist.")
            return redirect('wishlist')
        else:
            Venue_Wishlist(user=user, venue=venue).save()
            messages.success(request, "Venue successfully added in wishlist.")
            return redirect('wishlist')
    else:
        messages.success(request, "First login your self before using this services.")
        return render(request, "login.html")


def addvender_towishlist(request, vender_id):
    if request.user.is_authenticated:
        user = request.user
        vender = Venders.objects.get(vender_id=vender_id)

        if Vender_Wishlist.objects.filter(vender__vender_id=vender_id).filter(user=user).exists():
            messages.success(request, "Vender already added in wishlist.")
            return redirect('wishlist')
        else:
            Vender_Wishlist(user=user, vender=vender).save()
            messages.success(request, "Vender successfully added in wishlist.")
            return redirect('wishlist')
    else:
        messages.success(request, "First login your self before using this services.")
        return render(request, "login.html")


def addcake_towishlist(request, cake_id):
    if request.user.is_authenticated:
        user = request.user
        cake = CAKE.objects.get(cake_id=cake_id)

        if CAKE_WISHLIST.objects.filter(cake__cake_id=cake_id).filter(user=user).exists():
            messages.success(request, "Cake already added in wishlist.")
            return redirect('wishlist')
        else:
            CAKE_WISHLIST(user=user, cake=cake).save()
            messages.success(request, "Cake successfully added in wishlist.")
            return redirect('wishlist')
    else:
        messages.success(request, "First login your self before using this services.")
        return render(request, "login.html")


def removevenue_towishlist(request, venue_id):
    user = request.user
    venue = Venue_Wishlist.objects.filter(user=user).get(venue__venue_id=venue_id)
    venue.delete()
    messages.success(request, "Venue successfully removed from wishlist.")
    return redirect('wishlist')


def removevender_towishlist(request, vender_id):
    user = request.user
    vender = Vender_Wishlist.objects.filter(user=user).get(vender__vender_id=vender_id)
    vender.delete()
    messages.success(request, "Vender successfully removed from wishlist.")
    return redirect('wishlist')


def removecake_towishlist(request, cake_id):
    user = request.user
    wish = CAKE_WISHLIST.objects.filter(user=user).get(cake__cake_id=cake_id)
    wish.delete()
    messages.success(request, "Cake successfully removed from wishlist.")
    return redirect('wishlist')


def Cart(request):
    if request.user.is_authenticated:
        user = request.user
        venue_cart = Venue_Cart.objects.filter(user=user)
        vender_cart = Vender_Cart.objects.filter(user=user)
        cake_cart = CAKE_CART.objects.filter(user=user)

        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        total_item = venue_count + vender_count + cake_count

        if total_item is 0:
            return render(request,'EmptyCart.html')
        else:
            booked_manager = MANAGER_BOOKING.objects.filter(manager__user=user)

            data = {'venue_cart': venue_cart, 'vender_cart': vender_cart, 'cake_cart': cake_cart,
                    'venue_count': venue_count, 'vender_count': vender_count, 'cake_count': cake_count, 'total_item': total_item
                    ,'manager':booked_manager}
            return render(request, 'Cart.html', data)
    else:
        messages.success(request,'Cart service will open after login in website.')
        return render(request, 'Login.html')


def addvenue_tocart(request, venue_id):
    if request.user.is_authenticated:
        user = request.user
        venue = Venue_Provider.objects.get(venue_id=venue_id)

        if Venue_Cart.objects.filter(venue__venue_id=venue_id).filter(user=user).exists():
            messages.success(request, "Venue already added in cart.")
            return redirect('cart')
        else:
            Venue_Cart(user=user, venue=venue).save()
            messages.success(request, "Venue successfully added in cart.")
            return redirect('cart')
    else:
        messages.success(request, "First login your self before using this services.")
        return render(request, "login.html")


def addvender_tocart(request, vender_id):
    if request.user.is_authenticated:
        user = request.user
        vender = Venders.objects.get(vender_id=vender_id)

        if Vender_Cart.objects.filter(vender__vender_id=vender_id).filter(user=user).exists():
            messages.success(request, "Vender already added in cart.")
            return redirect('cart')
        else:
            Vender_Cart(user=user, vender=vender).save()
            messages.success(request, "Vender successfully added in cart.")
            return redirect('cart')
    else:
        messages.success(request, "First login your self before using this services.")
        return render(request, "login.html")


def addcake_tocart(request, cake_id):
    if request.user.is_authenticated:
        user = request.user
        cake = CAKE.objects.get(cake_id=cake_id)

        if CAKE_CART.objects.filter(cake__cake_id=cake_id).filter(user=user).exists():
            messages.success(request, "Cake already added in cart.")
            return redirect('cart')
        else:
            CAKE_CART(user=user, cake=cake).save()
            messages.success(request, "Cake successfully added in cart.")
            return redirect('cart')
    else:
        messages.success(request, "First login your self before using this services.")
        return render(request, "login.html")


def removevenue_tocart(request, venue_id):
    user = request.user
    venue = Venue_Cart.objects.filter(user=user).get(venue__venue_id=venue_id)
    venue.delete()
    messages.success(request, "Venue successfully removed from cart.")
    return redirect('cart')


def removevender_tocart(request, vender_id):
    user = request.user
    vender = Vender_Cart.objects.filter(user=user).get(vender__vender_id=vender_id)
    vender.delete()
    messages.success(request, "Vender successfully removed from cart.")
    return redirect('cart')


def removecake_tocart(request, cake_id):
    user = request.user
    cake = CAKE_CART.objects.filter(user=user).get(cake__cake_id=cake_id)
    cake.delete()
    messages.success(request, "Cake successfully added in cart.")
    return redirect('cart')


def Profile(request):
    if request.user.is_authenticated:
        user = request.user
        user_manager = MANAGER_BOOKING.objects.filter(user=user)

        booked_manager = MANAGER_BOOKING.objects.filter(manager__user=user)
        venders = MANAGER_VENDER_BOOKING.objects.filter(user=user)

        # Total item present in user cart.
        venue_count = Venue_Cart.objects.filter(user=user).count()
        vender_count = Vender_Cart.objects.filter(user=user).count()
        cake_count = CAKE_CART.objects.filter(user=user).count()
        total_item = venue_count + vender_count + cake_count

        data = {'total_item': total_item,'manager':booked_manager,'venders':venders,'user_manager':user_manager}
        return render(request, 'Profile.html', data)
    else:
        messages.success(request,'Profile service will open after login.')
        return render(request, 'Login.html')

def detailsofsevices(request,mb_id):
    mb = MANAGER_BOOKING.objects.filter(mb_id=mb_id)
    for i in mb:
        customer = i.user
    
    cus_vender = MANAGER_VENDER_BOOKING.objects.filter(user=customer)
    cus_venue = MANAGER_VENUE_BOOKING.objects.filter(user=customer)
    data= {'vender':cus_vender,'venue':cus_venue}
    return render(request,"ServiceDetails.html",data)

def Registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']

        if((first_name>='a' and first_name <= 'z') or (first_name >= 'A' and first_name <= 'Z')):
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(email=email).exists():
                messages.error(
                    request, "This email is already taken. Please try another email.")
                return redirect('registration')
            else:
                user = User.objects.create_user(
                    first_name=first_name, username=email, email=email, password=password)
                user.save()
                messages.success(request, "You have Successfully Registered.")
                return redirect('login')
        else:
            messages.success(request,'First name value is incorrect or invalid. Please enter valid input.')
            return redirect('registration')
    return render(request, 'Registration.html')


def Login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = auth.authenticate(
            username=loginusername, password=loginpassword)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully logged into website.")
            return redirect('home')
        else:
            messages.warning(
                request, "Username or password is invalid. Please try again.")
            return redirect('login')
    return render(request, 'Login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def ForgetPassword(request):
    return render(request, 'ForgetPassword.html')

# Birthday section views


def Birthday(request):
    return render(request, 'Birthday_Home.html')


def Cakes(request):
    return render(request, 'Cake_Place.html')


def Menu(request):
    return render(request, 'Cake_Menu.html')
