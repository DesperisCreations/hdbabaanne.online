from django.contrib import admin
from webapp.models import Video, Kategori

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("baslik",'aciklama','kategori','kapak_resmi', "yuklenme_tarihi")  # Admin panelinde gösterilecek sütunlar
    
@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ("id","isim")    
 
