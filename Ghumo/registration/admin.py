from django.contrib import admin
from .models import User, Seller, Artist, Traveller

# Register your models here.
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Artist)
admin.site.register(Traveller)
