"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import SimpleUrlDownload

class SimpleUrlDownloadTest(TestCase):
	
	def test_local_file_download(self):
		"""
		Tests local file download.
		"""
		download = SimpleUrlDownload.create("http://localhost")
		download.save()
		download.start()
		self.assertEqual(download.file_size, download.downloaded_file_size)
		self.assertEqual(download.name, 'localhost')
		self.assertEqual(download.state, 'Finished')
