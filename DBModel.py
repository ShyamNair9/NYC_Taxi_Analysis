from GreenTaxi.models import RequestTable
import csv

with open('E:/NYU Docs/Django_Project/Revmax/finaldata.csv') as csvfile:

	reader = csv.DictReader(csvfile)
	for row in reader:
		a = RequestTable(vendor_id=row['vendor_id'], pick_lat=row['pick_lat'],
						 pick_lon=row['pick_lon'], drop_lat=row['drop_lat'],
						 drop_lon=row['drop_lon'], passenger=row['passenger'],
						 trip_dist= row['trip_dist'], start_time=row['start_time'],
						 end_time=['end_time'])
		a.save()


