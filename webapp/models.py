from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Video(models.Model):
    baslik = models.CharField(max_length=255, verbose_name="Başlık")
    aciklama = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    video_dosyasi = models.FileField(upload_to="medias/", verbose_name="Video Dosyası")
    kapak_resmi = models.ImageField(upload_to='medias/')
    yuklenme_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Yüklenme Tarihi")
    slug = AutoSlugField(populate_from="baslik", unique=True, verbose_name="Slug")

    def __str__(self):
        return self.baslik