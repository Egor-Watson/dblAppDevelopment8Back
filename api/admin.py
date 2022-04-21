from django.contrib import admin
from .models import Listing, ExtraUserInformation, Offer

# Register your models here.
admin.site.register(Listing)
admin.site.register(ExtraUserInformation)
admin.site.register(Offer)
