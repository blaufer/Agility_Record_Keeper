import agility_data as ad
from pprint import pprint

a = ad.AgilityData()
t = a.readJSON('test.json')
if t != None:
    print(t)

pprint(a.canine)
    
