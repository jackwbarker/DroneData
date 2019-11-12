import os
import json
from jsonmerge import merge 

data = [] 

for obj in os.listdir():
	if(obj.endswith('.json') and obj != []):
		with open(obj) as json_file:
			d = json.load(json_file)
			data.append(d)

init = merge(data[0], data[1])


for i in range(2, len(data)):
	print(i)
	init = merge(init, data[i])


with open('combined.json', 'w') as outfile:
	json.dump(init, outfile)
