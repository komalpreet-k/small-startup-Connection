from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Country, State, City, Category, Business
from .serializers import (
    CountrySerializer,
    StateSerializer,
    CitySerializer,
    CategorySerializer,
    BusinessSerializer
)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.filter(is_active=True)
    serializer_class = BusinessSerializer
