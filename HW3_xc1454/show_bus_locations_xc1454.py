from __future__ import print_function
import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# get input
apikey = sys.argv[1]
bus_line = 'MTA%20NYCT_' + sys.argv[2]
print("Bus Line :", sys.argv[2])

url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(apikey, bus_line)

# get data through api
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# output the data we want
vehicles_number = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print('Number of Active Buses :', vehicles_number)

i = 0
for item in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    Longitude = item['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Latitude = item['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print('Bus ', i,' is at latitude', Latitude,' and longitude', Longitude)
    i += 1
