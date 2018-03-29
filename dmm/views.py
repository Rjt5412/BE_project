from django.shortcuts import render, get_object_or_404, redirect
from . import services

# Create your views here.

def index(request):
    twitter_trends = services.get_twitter_trends()
    gplus_trends,tumblr_trends = services.get_tumblr_and_gplus_trends()
    return render(request, 'dmm/index.html',{'twitter_trends': twitter_trends, 'gplus_trends': gplus_trends, 'tumblr_trends': tumblr_trends})

def search(request):
    return render(request, 'dmm/search.html')



