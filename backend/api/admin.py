from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Country, State, City, Category, Business, SavedBusiness

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Business)
admin.site.register(SavedBusiness)
