# Generated by Django 5.1.7 on 2025-03-20 14:10

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=255, verbose_name='Başlık')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('video_dosyasi', models.FileField(upload_to='videos/', verbose_name='Video Dosyası')),
                ('yuklenme_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Yüklenme Tarihi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Slug')),
            ],
        ),
    ]
