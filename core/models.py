from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(_('email address'), unique = True)
  availabele_for_work = models.BooleanField(default=True)
  phone_no = models.CharField(max_length = 10)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  def __str__(self):
      return "{}".format(self.email)

    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    rate = models.PositiveIntegerField()
    rate_color = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.name
    



class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/project_images")
    link = models.URLField(max_length = 200,blank =True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField()

    used_tools = models.ManyToManyField(Skill)
   
    


    def __str__(self):
        return self.title



class VistedPlace(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/places")
    link = models.URLField(max_length = 200,blank =True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_visted = models.DateTimeField()


class ContactMethod(models.Model):
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
class Location(models.Model):
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    specific_address = models.CharField(max_length=250)


    def __str__(self):
        return f" {self.country}, { self.city }"

class  Donate(models.Model):
    pass

class Service(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "images/services")
    description = models.TextField()
    hover_color = models.CharField(max_length=25)



    def __str__(self):
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to = "images/icon")


    def __str__(self):
        return f" {self.name}"
    


class Email(models.Model):
    sender_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    title = models.CharField(max_length=250)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.title


   



    