from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return f"{self.name}, {self.country.code}"


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        unique_together = ('name', 'state')

    def __str__(self):
        return f"{self.name}, {self.state.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Business(models.Model):

    VERIFICATION_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="businesses")
    name = models.CharField(max_length=255)
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="businesses")

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="businesses")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="businesses")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="businesses")

    phone = models.CharField(max_length=20, blank=True)
    instagram_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    verification_status = models.CharField(
        max_length=20,
        choices=VERIFICATION_STATUS,
        default='pending'
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SavedBusiness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_businesses")
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'business')

    def __str__(self):
        return f"{self.user.username} saved {self.business.name}"
