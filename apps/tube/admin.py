from django.contrib import admin

from apps.tube.models import Video



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

