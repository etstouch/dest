import requests

#dictionary to hold extra headers
HEADERS = {"X-API-KEY": '381bc3958d3541bf8db576788bd29d53'}

#make request for Gjallarhorn
r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", headers=HEADERS);

#convert the json objet we received into a Pythong dictionary object and
#print the name of the item
inventoryItem = r.json()

print(inventoryItem['Response']['data']['inventoryItem']['itemName'])
