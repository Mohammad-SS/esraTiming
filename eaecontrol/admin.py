from django.contrib import admin
from eaecontrol import models
from django.contrib.auth.models import Group , User
# Register your models here.

admin.site.register(models.Person )
admin.site.register(models.Timing )
admin.site.register(models.Group )
admin.site.unregister(Group )
admin.site.unregister(User )
