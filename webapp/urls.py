from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index),
    path('video/<slug:slug>', views.videoizle),
]
