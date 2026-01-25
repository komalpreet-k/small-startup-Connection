from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
from rest_framework import viewsets
from .models import Country, State, City, Category, Business, SavedBusiness
from .serializers import (
    CountrySerializer,
    StateSerializer,
    CitySerializer,
    CategorySerializer,
    BusinessSerializer,
    SavedBusinessSerializer
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
    queryset = Business.objects.all()   # <-- ADD THIS
    serializer_class = BusinessSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Business.objects.filter(
            is_active=True,
            verification_status='approved'
        )

        country_id = self.request.query_params.get('country')
        state_id = self.request.query_params.get('state')
        city_id = self.request.query_params.get('city')
        category_id = self.request.query_params.get('category')


        if country_id:
            queryset = queryset.filter(country__id=country_id)

        if state_id:
            queryset = queryset.filter(state__id=state_id)

        if city_id:
            queryset = queryset.filter(city__id=city_id)
        
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset

class SavedBusinessViewSet(viewsets.ModelViewSet):
    queryset = SavedBusiness.objects.all()   # <-- ADD THIS
    serializer_class = SavedBusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SavedBusiness.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
