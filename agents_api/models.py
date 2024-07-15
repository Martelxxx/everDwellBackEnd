from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100)
    agency = models.CharField(max_length=100, default='Unspecified Agency')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Class for Home Addresses and Specs
class Home(models.Model):
    address = models.CharField(max_length=200)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # zipcode = models.CharField(max_length=10)
    price = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    sqft = models.IntegerField()
    # agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
# Class for Buyer Info
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preapproval = models.BooleanField(default=False)
    budget = models.IntegerField()
    address = models.CharField(max_length=200)
    homeRating = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name