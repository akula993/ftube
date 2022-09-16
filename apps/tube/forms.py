from django import forms

from apps.tube.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["title", "file", 'user']
