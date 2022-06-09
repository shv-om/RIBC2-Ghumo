from django.db import models

class FAQs(models.Model):
	ques = models.TextField()
	ans = models.TextField()

	def __str__(self):
		return self.ques