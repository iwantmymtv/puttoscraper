import json, csv
from collections import OrderedDict #To maintain key value pair order
_json=json.loads(open('anyad.json', 'r').read(), object_pairs_hook=OrderedDict) 
out=open('colors.csv', 'w')
writer = csv.writer(out)               #create a csv.write
writer.writerow(_json[0].keys())      # header row
for row in _json:
    writer.writerow(row.values())