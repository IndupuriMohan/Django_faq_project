from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

# Create a router and register the FAQViewSet
router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),