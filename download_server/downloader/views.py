# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
	return render(request, "downloader/index.html")

def new_download(request):
	return render(request, "downloader/new_download.html")

def submit_new_download(request):
	return HttpResponseRedirect(reverse('downloader:downloads_list'))

def downloads_list(request):
	return HttpResponse("Downloads list");
