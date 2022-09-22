import json
import collections
orderedDict = collections.OrderedDict()
from collections import OrderedDict

file = open("ireg.txt", "r")
Lines = file.readlines()
x = 0
y = ""
count = 0
ccount = 0
jsonFilePath='data.json'
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
	jj = '{"verb":['
	jsonf.write(jj)
	for line in Lines:
		y = "{}".format(line.strip())
		
		ccount = ccount + 1
		if count == 0:
			y = '{"'+ y + '":["' + y +'",'
			jsonf.write(y)
		if count == 1:
			y = '"'+ y + '",'
			jsonf.write(y)
		count = count + 1
		if count == 3:
			y = '"' + y + '"]}'
			if ccount < 318:
				y = y + ','
			jsonf.write(y)
			y = ""
			count = 0
	jj = "]}"
	jsonf.write(jj)