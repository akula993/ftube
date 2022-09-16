from django.urls import path

from apps.tube.views import HomeView, VideoView

urlpatterns = [
    path('stream/<int:pk>/', VideoView.get_streaming_video, name='stream'),
    path('', HomeView.as_view(), name='index'),

]