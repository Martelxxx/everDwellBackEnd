from django.contrib import admin

# Register your models here.
from .models import Agent
from .models import Home
from .models import Buyer

admin.site.register(Agent)
admin.site.register(Home)
admin.site.register(Buyer)