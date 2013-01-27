# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Download
from models import SimpleUrlDownload
import sys

def index(request):
	return render(request, "downloader/index.html")

def new_download(request):
	return render(request, "downloader/new_download.html")

def submit_new_download(request):
	try:
		download_url = request.POST['download_url']
		download_type = request.POST['download_type']
	except (KeyError):
		return render(request, 'downloader/new_download.html', {
			'error_message': "You didn't select a download type.",
		})

	if download_type == "simple_url_download":
		download = SimpleUrlDownload.create(download_url)
	else:
		return render(request, 'downloader/new_download.html', {
			'error_message': "Unsupported download type.",
		})
	download.save()
	download.start()

	return HttpResponseRedirect(reverse('downloader:downloads_list'))

def downloads_list(request):
	#latest_poll_list = Poll.objects.filter(pub_date__lte = timezone.now).order_by('-pub_date')[:5]
	#latest_downloads_list = Download.objects.all()
	latest_downloads_list = SimpleUrlDownload.objects.all()
	context = {'latest_downloads_list': latest_downloads_list}
	return render(request, "downloader/downloads_list.html", context)
