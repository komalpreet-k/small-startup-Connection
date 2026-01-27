from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from .models import Country, State, City, Category, Business, SavedBusiness
from .serializers import (
    CountrySerializer,
    StateSerializer,
    CitySerializer,
    CategorySerializer,
    BusinessSerializer,
    BusinessCreateSerializer,
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

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminUserCustom(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrReadOnly()]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUserCustom])
    def approve(self, request, pk=None):
        business = self.get_object()

        if business.verification_status == 'approved':
            return Response(
                {"message": "Business is already approved."},
                status=status.HTTP_400_BAD_REQUEST
            )

        business.verification_status = 'approved'
        business.save()

        return Response(
            {"message": "Business approved successfully."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUserCustom])
    def reject(self, request, pk=None):
        business = self.get_object()

        business.verification_status = 'rejected'
        business.save()

        return Response(
            {"message": "Business rejected."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUserCustom])
    def deactivate(self, request, pk=None):
        business = self.get_object()

        business.is_active = False
        business.save()

        return Response(
            {"message": "Business deactivated."},
            status=status.HTTP_200_OK
        )

    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BusinessCreateSerializer
        return BusinessSerializer

    def get_queryset(self):
        # Public view → only approved
        if self.action in ['list', 'retrieve']:
            queryset = Business.objects.filter(
                is_active=True,
                verification_status='approved'
            )
        else:
            # Owner view → show their own businesses
            queryset = Business.objects.filter(owner=self.request.user)

        # Filters for public listing
        if self.action == 'list':
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

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            verification_status='pending'
        )
    
    def perform_update(self, serializer):
        serializer.save(verification_status='pending')


class SavedBusinessViewSet(viewsets.ModelViewSet):
    queryset = SavedBusiness.objects.all()   # <-- ADD THIS
    serializer_class = SavedBusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SavedBusiness.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
