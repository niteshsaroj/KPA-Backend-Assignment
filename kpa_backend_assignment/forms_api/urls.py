from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BogieChecksheetFormViewSet, WheelSpecificationViewSet

router = DefaultRouter()
router.register(r'forms/bogie-checksheet', BogieChecksheetFormViewSet, basename='bogie-checksheet')
router.register(r'forms/wheel-specifications', WheelSpecificationViewSet, basename='wheel-specifications')

urlpatterns = [
    path('', include(router.urls)),
]
