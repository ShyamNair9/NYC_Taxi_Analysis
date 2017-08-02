# coding=utf-8
import requests
import json
from math import sin, cos, sqrt, atan2, radians


class Results:

	# Loads the data from the url in json format
	def fetch_json(self, url):
		response = requests.get(url)
		return json.loads(response.content)

	# Calculates distance(kms) between 2 latitude and longitude points
	def check_dist(lat1, lon1, lat2, lon2):
		rad = 6373.0
		lat1 = radians(lat1)
		lat2 = radians(lat2)
		lon1 = radians(lon1)
		lon2 = radians(lon2)
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		distance = rad * c

		if distance > 10:
			return False
		else:
			return True

	# Checks if start time, end time, latitude and longitude
	# are in the specified range
	def getResults(self, st, et, in_lat, in_lon, count, jData):
		pickups = 0
		for i in range(0, len(jData)):
			if (st >= jData[i]['start_time'] and et <= jData[i][
				'end_time'] and Results.check_dist(float(in_lat), float(in_lon),
										   float(jData[i]['pick_lat']),
										   float(jData[i]['pick_lon']))):

				pickups = pickups + 1
		if count <= pickups:
			print("Yes : count={}, total pickups ={}".format(count, pickups))
		else:
			print("No: count={}, total pickups ={}".format(count, pickups))


if __name__ == '__main__':

	st=input("Provide start time in the format(YYYY-MM-DDTHH:MM:SSZ): ")
	et=input("Provide end time in the format(YYYY-MM-DDTHH:MM:SSZ): ")
	in_lat= float(input("Provide latitude: "))
	in_lon=float(input ("Provide longitude: "))
	count= int(input("Provide count: "))

	jData = Results().fetch_json("http://127.0.0.1:8000/status/")

	Results().getResults(st, et, in_lat, in_lon, count, jData)

#Sample input
'''
st = "2016-01-01T00:16:00Z"
et = "2016-01-01T00:29:00Z"
in_lat = "40.72317505"
in_lon = "-73.95267487"
count = 189
'''