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

fout = open(sys.argv[3], "w")

url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

# get data through api
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

fout.write("Latitude,Longitude,Stop Name,Stop Status" + "\n")
for item in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    Longitude = item['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Latitude = item['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    if item['MonitoredVehicleJourney']['OnwardCalls'] == {}:
        Stop_Name = 'N/A'
        Stop_Status = 'N/A'
    else:
        Stop_Name = item['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        Stop_Status = item['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']


    #print(Stop_Name, Stop_Status)
    fout.write(str(Latitude) + "," + str(Longitude) + "," + Stop_Name + "," + Stop_Status + "\n")

fout.close()