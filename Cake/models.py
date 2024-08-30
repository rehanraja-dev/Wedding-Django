from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator
# Create your models here.

class CAKE_FLAVOUR(models.Model):
    flavour_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    flavour_name = models.CharField(max_length=20)

    def __str__(self):
        return self.flavour_name
    class Meta:
        ordering=['flavour_name']

class CAKE_PROVIDER(models.Model):
    cakeprovider_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    cakep_name = models.CharField(max_length=20)
    mobile = models.CharField(default='9155007890',validators=[MinLengthValidator(10),MaxLengthValidator(10)],max_length=10)
    email = models.EmailField(default='@gmail.com',validators=[MinLengthValidator(11),MaxLengthValidator(50)])
    state = models.CharField(default='Madhya Pradesh' ,max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.cakep_name} {self.mobile}"
    class Meta:
        ordering=['cakep_name']

cake_color = [
    ('Black','Black'),
    ('White','White'),
    ('Pink','Pink'),
]
class CAKE(models.Model):
    cake_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    cake_name = models.CharField(max_length=20)
    flavour = models.ForeignKey(CAKE_FLAVOUR, on_delete=models.CASCADE)
    provider = models.ForeignKey(CAKE_PROVIDER, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Cake_Image')
    price = models.FloatField(default=1000.0,validators=[MinValueValidator(1000.0),MaxValueValidator(10000.0)])
    color = models.CharField(max_length=10,choices=cake_color)
    def __str__(self):
        return self.cake_name
    class Meta:
        ordering=['flavour']

class CAKE_CART(models.Model):
    cakecart_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cake = models.ForeignKey(CAKE,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.first_name} {self.cake.cake_name} {self.cake.flavour.flavour_name}"
    class Meta:
        ordering=['user']

class CAKE_WISHLIST(models.Model):
    cakewish_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cake = models.ForeignKey(CAKE,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.first_name} {self.cake.cake_name} {self.cake.flavour.flavour_name}"
    class Meta:
        ordering=['user']

class CAKE_BOOKING(models.Model):
    cakeorder_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cake = models.ForeignKey(CAKE,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.first_name} {self.cake.cake_name} {self.cake.flavour.flavour_name}"
    class Meta:
        ordering=['user']