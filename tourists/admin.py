from django.contrib import admin
from .models import ExplorerProfile, Location, MeetUp
# Register your models here.

admin.site.Register(ExplorerProfile)
admin.site.Register(Location)
admin.site.Register(MeetUp)