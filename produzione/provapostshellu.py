#!/usr/bin/python3
 
import requests

url ='https://shelly-103-eu.shelly.cloud/device/relay/control' 
myjson = {'channel': '0',
	'turn' : 'off',
	'id' : '30c6f780a3d8',
	'auth_key' : 'MjQ3NjAwdWlk3A9FB4F3DD95DD8D83C08910EEBBDB47BB82FAF6C6D16578AEA53971CBE31BE12075A3D120DA0C9F'}
print (myjson)
x = requests.post(url, data=myjson)

#print the response text (the content of the requested file):

print(x.text)
