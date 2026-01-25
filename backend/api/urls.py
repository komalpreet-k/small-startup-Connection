from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet,
    StateViewSet,
    CityViewSet,
    CategoryViewSet,
    BusinessViewSet, 
    SavedBusinessViewSet
)

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'businesses', BusinessViewSet)
router.register(r'saved-businesses', SavedBusinessViewSet)

urlpatterns = router.urls
