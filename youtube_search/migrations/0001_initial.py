# Generated by Django 2.2.1 on 2021-06-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('published_at', models.DateTimeField()),
                ('thumbnail_url', models.CharField(blank=True, max_length=200, null=True)),
                ('video_id', models.CharField(max_length=100, unique=True)),
                ('channel_id', models.CharField(max_length=200)),
                ('channel_title', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
