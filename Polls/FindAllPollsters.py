from pollster import Pollster
import sys

pollsterList = []

pollster = Pollster()

pollCharts = pollster.charts()
#iterate through every category of polls
for x in pollCharts:
	#iterate through all the polls in the category
	for y in x.polls():
		if(y.pollster not in pollsterList):
			pollsterList.append(y.pollster)

print pollsterList