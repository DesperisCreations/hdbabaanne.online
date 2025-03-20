from django.contrib import admin
from webapp.models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("baslik",'aciklama','kapak_resmi', "yuklenme_tarihi")  # Admin panelinde gösterilecek sütunlar