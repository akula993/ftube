# Generated by Django 4.1.1 on 2022-09-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_video_datetime_up_alter_video_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='path',
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default=1, upload_to='video'),
            preserve_default=False,
        ),
    ]