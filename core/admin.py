from django.contrib import admin
from django.db.models import fields
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
# Register your models here.


class UserAdmin(BaseUserAdmin):
#   form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('availabele_for_work', 'phone_no',"profile_image",'location')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "availabele_for_work", "phone_no","profile_image",'location']
  search_fields = ('email', 'first_name', 'last_name','location')
  ordering = ('email', )


admin.site.register(User,UserAdmin)
admin.site.register(Project)
admin.site.register(Skill)

