from rest_framework import routers
from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'location', LocationViewSet, basename='location')
router.register(r'skill', SkillViewSet, basename='skill')
router.register(r'contact',ContactMethodViewSet, basename='contact')
router.register(r'email', EmailViewSet, basename='email')
router.register(r'social_link', SocialLinkViewSet, basename='social_link')
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'places', VistedPlaceViewSet, basename='visited_places')

urlpatterns = [
    path('projects',ProjectView.as_view(),name="projects")
] + router.urls
