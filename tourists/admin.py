from django.contrib import admin
from .models import Explorer, Location, MeetUp
# Register your models here.

admin.site.Register(Explorer)
admin.site.Register(Location)
admin.site.Register(MeetUp)