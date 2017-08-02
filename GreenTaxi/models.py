from django.db import models


class RequestTable(models.Model):
	vendor_id = models.IntegerField()
	pick_lat = models.FloatField(max_length=100)
	pick_lon = models.FloatField(max_length=100)
	drop_lat = models.FloatField(max_length=100)
	drop_lon = models.FloatField(max_length=100)
	passenger = models.IntegerField()
	start_time = models.DateTimeField(default=True)
	end_time = models.DateTimeField(default=True)
	trip_dist = models.FloatField(max_length=10, default=True)