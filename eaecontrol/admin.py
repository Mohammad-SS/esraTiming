from django.contrib import admin
from eaecontrol import models

class TimingAdmin(admin.ModelAdmin):
    search_fields = ['person__name']

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(models.Person , PersonAdmin)
admin.site.register(models.Timing , TimingAdmin)
admin.site.register(models.Group)