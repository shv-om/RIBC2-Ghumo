from django.db import models

class Marketplace:
	item_name = models.CharField(max_length=50)
	item_details = models.CharField(max_length=500)
	item_type = models.CharField(max_length=25)
	item_price = models.IntegerField()
	item_photo = models.ImageField(upload_to='uploads')

	def __str__(self):
		return self.item_name
