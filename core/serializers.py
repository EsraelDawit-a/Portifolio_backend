from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import SocialLink, Email, Service, Location, ContactMethod,VistedPlace, Skill,Project

class ProjectSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["titile","image","link","date_created","date_posted"]
       

class SkillSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class LocationSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class ContactMethodSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = ContactMethod
        fields = "__all__"

class VissitedPlacesSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = VistedPlace
        fields = "__all__"

class ServiceSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class EmailSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"

class SocialLinkSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"

