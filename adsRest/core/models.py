from django.db import models

# Generic request helper
class request(models.Model):
	def get(url):
		return 'GET REQUEST to %s' % url
	def post(url,data):
		return 'POST REQUEST'