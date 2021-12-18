from django.core.checks import messages
from django.core.exceptions import SuspiciousOperation
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers, views, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .models import SocialLink, Email, Service, Location, ContactMethod,VistedPlace, Skill,Project,User
from .serializers import ContactMethodSerialaizer, EmailSerialaizer, LocationSerialaizer, ProjectSerialaizer, ServiceSerialaizer, SkillSerialaizer, SocialLinkSerialaizer, UserSerializer, VisitedPlacesSerialaizer
from rest_framework.views import APIView
from collections import defaultdict


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

class ProjectView(APIView):

    def get(self,request):
        projects = list(Project.objects.all())
        dumb = []

        for i in range(len(projects)):
            ob = defaultdict(lambda:[])
            item = projects[i]
            
            tools =[]
            for k in range(len(item.used_tools.all().values())):
                data = item.used_tools.all().values()[k]
                tool = defaultdict(lambda:[])
                tool['id'] = data['id']
                tool['name'] = data['name']

                tools.append(tool)
            ob["project"] = item.title
            ob["image"]  = item.image.url
            ob["link"]  = item.link
            ob ["date_created"] = item.date_created
            ob["date_posted"] = item.date_posted
            ob["id"] = item.id
            ob["tool"] = tools

            dumb.append(ob)


        return Response(dumb)

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerialaizer
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SocialLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerialaizer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerialaizer



    def create(self, request):
        email_from = request.data["email"]
        sender_name = request.data["sender_name"]
        title = request.data["title"]
       
        sub = request.data["subject"]
        subject = f"sender: { sender_name } ,  title: {title} "
        message =  request.data["message"]

     
       
        
        try:
            recipient_list = ["esraeldawit0@gmail.com", ]
            send_mail( subject, message, email_from, recipient_list )

            return Response("message Sent")
        except Exception as e:
            print(e)
            raise SuspiciousOperation("Invalid Data!")

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerialaizer

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerialaizer

class ContactMethodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactMethod.objects.all()
    serializer_class = ContactMethodSerialaizer

class VistedPlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VistedPlace.objects.all()
    serializer_class = VisitedPlacesSerialaizer






