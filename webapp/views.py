from django.shortcuts import render, get_object_or_404, HttpResponse
from webapp.models import Video

# Create your views here.
def index(request):
    videos = Video.objects.all()
    return render(request,'main/index.jinja', {
        'videos':videos
    })

def videoizle(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'main/video.jinja', {
        'video':video
    })