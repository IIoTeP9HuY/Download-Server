from django.db import models

import urllib2
import sys

# Create your models here.

class Download(models.Model):

	name = models.CharField(max_length = 200)
	url = models.CharField(max_length = 200)

	class Meta:
		abstract = True


	@classmethod
	def create(Class, url):
		download = Class()
		download.url = url
		download.name = url.split("/")[-1]
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

class SimpleUrlDownload(Download):
	
	def type(self):
		return "Simple Url Download"

	def start(self):
		file_name = "/tmp/" + self.name
		u = urllib2.urlopen(self.url)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print >> sys.stderr, "Downloading: {0} Bytes: {1}".format(self.url, file_size)

		downloaded_file_size = 0
		read_block_size = 8196

		#while buffer = u.read(block_size):
		while True:
			buffer = u.read(read_block_size)
			if not buffer:
				break

			downloaded_file_size += len(buffer)
			f.write(buffer)
			download_progress = float(downloaded_file_size) / file_size
			status = r"{0}  [{1:.2%}]".format(downloaded_file_size, download_progress)
			status = status + chr(8)*(len(status) + 1)
			print >> sys.stderr, status

		print >> sys.stderr, "Download finished"

class TorrentDownload(Download):

	def type(self):
		return "Torrent Download"
