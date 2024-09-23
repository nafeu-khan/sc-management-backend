from django.contrib import admin

from common.models import *

# Register your models here.

from .models import ResearchInterestOptions

@admin.register(ResearchInterestOptions)
class ResearchInterestOptionsAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_at', 'updated_at')
admin.site.register(Countries)
admin.site.register(GeoAdmin1)
admin.site.register(Document)
admin.site.register(GeoAdmin2)  
admin.site.register(State)
