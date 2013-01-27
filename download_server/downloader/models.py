from django.db import models

import urllib2
import sys

# Create your models here.

class Download(models.Model):

	name = models.CharField(max_length = 255)
	file_name = models.CharField(max_length = 255)
	url = models.CharField(max_length = 255)
	state = models.CharField(max_length = 20)
	file_size = models.IntegerField()
	downloaded_file_size = models.IntegerField()

	class Meta:
		abstract = True

	@classmethod
	def create(Class, url):
		download = Class()
		download.url = url
		download.name = url.split("/")[-1]
		download.file_name = "/tmp/" + download.name
		download.state = "Not started"
		download.downloaded_file_size = 0
		u = urllib2.urlopen(download.url)
		meta = u.info()
		download.file_size = int(meta.getheaders("Content-Length")[0])
		if download.file_size == 0:
			raise Exception("File size is zero")

		return download

	def type(self):
		pass

	def __unicode__(self):
		return self.name

	def start(self):
		pass

	def pause(self):
		pass

	def stop(self):
		pass

	def resume(self):
		pass

	def progress(self):
		pass

class SimpleUrlDownload(Download):

	read_block_size = 8196

	def type(self):
		return "Simple Url Download"

	def progress(self):
		return int(float(self.downloaded_file_size) / self.file_size) * 100

	def start(self):
		f = open(self.file_name, 'wb')
		u = urllib2.urlopen(self.url)

		self.state = "Started"
		while True:
			buffer = u.read(self.read_block_size)
			if not buffer:
				break

			self.downloaded_file_size += len(buffer)
			f.write(buffer)
			self.save()

		self.state = "Finished"
		self.save()

class TorrentDownload(Download):

	def type(self):
		return "Torrent Download"
