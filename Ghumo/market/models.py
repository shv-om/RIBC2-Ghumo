from django.db import models

from registration.models import Seller, Artist


class District(models.Model):
    district_name = models.CharField(max_length=50)
    area_name = models.CharField(max_length=50)
    area_code = models.IntegerField()

    def __str__(self):
        return self.district_name


class Marketplace(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=500)
    item_photo = models.ImageField(upload_to='all_items')
    district_instance = models.ForeignKey(District, on_delete=models.CASCADE)
    seller_instance = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class EventDetails(models.Model):
    event_name = models.CharField(max_length=50)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_poster = models.ImageField(upload_to='event_posters')
    artist_instance = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['event_start_date']