# Generated by Django 4.1.1 on 2022-09-16 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tube', '0004_rename_video_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(null=True, upload_to='video/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]