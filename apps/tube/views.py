from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from apps.tube.forms import VideoForm
from apps.tube.models import Video
from apps.tube.services import open_file


class VideoView:
    def get_streaming_video(request, pk: int):
        file, status_code, content_length, content_range = open_file(request, pk)
        response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(content_length)
        response['Cache-Control'] = 'no-cache'
        response['Content-Range'] = content_range
        return response


class HomeView(ListView):
    model = Video
    template_name = 'apps/tube/index.html'
    context_object_name = 'video'

