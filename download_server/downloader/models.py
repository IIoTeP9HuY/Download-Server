from django.db import models

# Create your models here.

class Download(models.Model):

	name = models.CharField(max_length = 200)
	url = models.CharField(max_length = 200)

	class Meta:
		abstract = True

	def type(self):
		pass

	def __unicode__(self):
		return self.name

class SimpleUrlDownload(Download):
	
	def type(self):
		return "Simple Url Download"

class TorrentDownload(Download):

	def type(self):
		return "Torrent Download"
