from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator
# Create your models here.
from Cake.models import CAKE
from Tables.models import Venders ,Venue_Provider

class MANAGER(models.Model):
    manager_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='Profile', default='')
    mobile = models.CharField(default='7970656807',validators=[MinLengthValidator(10),MaxLengthValidator(10)],max_length=10)
    state = models.CharField(default='Madhya Pradesh' ,max_length=20)
    city = models.CharField(default='Bhopal' ,max_length=20)
    price = models.IntegerField(default='10000')
    def __str__(self):
        return f"{self.user.first_name}"
    class Meta:
        ordering=['user']

class MANAGER_VENUE_BOOKING(models.Model):
    mbooking_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    manager = models.ForeignKey(MANAGER,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    venue =  models.ForeignKey(Venue_Provider, on_delete=models.CASCADE)

    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.manager.user.first_name} {self.user.first_name} {self.venue.venue_name}"
    class Meta:
        ordering=['-order_date']

class MANAGER_VENDER_BOOKING(models.Model):
    mbooking_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    manager = models.ForeignKey(MANAGER,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    vender = models.ForeignKey(Venders, on_delete=models.CASCADE)

    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.manager.user.first_name} {self.user.first_name} {self.vender.vender_name}"
    class Meta:
        ordering=['-order_date']

class MANAGER_CAKE_BOOKING(models.Model):
    mbooking_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    manager = models.ForeignKey(MANAGER,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    cake = models.ForeignKey(CAKE, on_delete=models.CASCADE)

    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.manager.user.first_name} {self.user.first_name} {self.cake.provider.cakep_name}"
    class Meta:
        ordering=['-order_date']

class MANAGER_BOOKING(models.Model):
    mb_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    manager = models.ForeignKey(MANAGER,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    photographer = models.BooleanField(default=False,)
    cake = models.BooleanField(default=False,)
    mehndi = models.BooleanField(default=False,)
    makeup = models.BooleanField(default=False,)

    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.manager.user.first_name}"
    class Meta:
        ordering=['-order_date']
