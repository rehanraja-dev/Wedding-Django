from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator
# Create your models here.

class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    mobile = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='ProfileImage')
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class Venue_Type(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    venue_type = models.CharField(max_length=50)

    def __str__(self):
        return self.venue_type

class Venue_Provider(models.Model):
    venue_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    venue_name = models.CharField(max_length=50)
    venue_image = models.ImageField(upload_to='VenueImage')
    mobile = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    veg_price = models.IntegerField()
    nonveg_price = models.IntegerField() 
    room_availability = models.IntegerField()

    Venue_Type = models.ForeignKey(Venue_Type, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.venue_name)
    
    class Meta:
        ordering = ['-Venue_Type']
    
class Vender_Type(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    vender_type = models.CharField(max_length=50)

    def __str__(self):
        return self.vender_type
    
    class Meta:
        ordering = ['vender_type']

class Venders(models.Model):
    vender_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    vender_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    vender_image = models.ImageField(upload_to='VenderImage')
    price = models.CharField(max_length=5)
    
    vender_type = models.ForeignKey(Vender_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.vender_name
        
    class Meta:
        ordering = ['vender_type']
    
class Venue_Cart(models.Model):
    venuecart_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    venue = models.ForeignKey(Venue_Provider, on_delete=models.CASCADE)  
    def __str__(self):
        return self.user.first_name
    
class Vender_Cart(models.Model):
    vendercart_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    vender = models.ForeignKey(Venders, on_delete=models.CASCADE)  
    def __str__(self):
        return self.user.first_name
    
class Venue_Wishlist(models.Model):
    venuewl_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    venue = models.ForeignKey(Venue_Provider, on_delete=models.CASCADE)  
    def __str__(self):
        return self.user.first_name
    
class Vender_Wishlist(models.Model):
    venderwl_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    vender = models.ForeignKey(Venders, on_delete=models.CASCADE)  
    def __str__(self):
        return self.user.first_name
    
class Venue_Booking(models.Model):
    venueb_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    venue = models.ForeignKey(Venue_Provider, on_delete=models.CASCADE)  
    orderdate  = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    
    
class Vender_Booking(models.Model):
    venderb_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    vender = models.ForeignKey(Venders, on_delete=models.CASCADE)  
    orderdate  = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        ordering = ['-orderdate']
    
class Venue_Rating(models.Model):
    venuerating_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    venue = models.ForeignKey(Venue_Provider, on_delete=models.CASCADE) 
    rating = models.IntegerField()
    reviews = models.CharField(max_length=200,null=True) 
    image = models.ImageField(null=True,upload_to='Rating')
    def __str__(self):
        return self.user.first_name
    
class Vender_Rating(models.Model):
    venderrating_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    vender = models.ForeignKey(Venders, on_delete=models.CASCADE) 
    rating = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    reviews = models.CharField(max_length=200,null=True) 
    image = models.ImageField(upload_to='Rating',null=True,blank=True)
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        ordering = ['-rating']