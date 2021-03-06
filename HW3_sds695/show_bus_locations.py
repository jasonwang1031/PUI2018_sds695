from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys


apikey = sys.argv[1]
bus=sys.argv[2]
count=0
url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s"%(apikey)

print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)


vehicle_monitoring_delivery=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Bus Line "+bus)
l=[]
for v in vehicle_monitoring_delivery:
	if(v['MonitoredVehicleJourney']['PublishedLineName']==bus):
		count=count+1
		l.append(v['MonitoredVehicleJourney']['VehicleLocation'])
print("Number of active buses:"+str(count))
for i in l:
	print("The latitude is "+str(i['Latitude'])+" and the logitude is"+str(i['Longitude']))
