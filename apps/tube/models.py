from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='video/', null=True, verbose_name="")
    datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    datetime_up = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User')

    def __str__(self):
        return self.title + ": " + str(self.file)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.file)
        # self.profile = Profile.user
        super(Video, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def get_absolute_url(self):
        return reverse('video', kwargs={'video_id': self.pk})
