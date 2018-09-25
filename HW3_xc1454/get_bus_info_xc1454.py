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

url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(apikey, bus_line)

# get data through api
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

fout.write("Latitude,Longitude,Stop Name,Stop Status" + "\n")
for item in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    Longitude = item['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Latitude = item['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Stop_Name = item['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    if Stop_Name == None:
        Stop_Name == "N/A"
    Stop_Status = item['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    if Stop_Status == None:
        Stop_Status == "N/A"
    #print(Stop_Name, Stop_Status)
    fout.write(str(Latitude) + "," + str(Longitude) + "," + Stop_Name + "," + Stop_Status + "\n")

fout.close()