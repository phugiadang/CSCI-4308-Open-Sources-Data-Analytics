from pollster import Pollster
from datetime import date
import sys

pollster = Pollster()

def getPollsByPollster(Pollster):
	pollCat = pollster.charts()
	#iterate through every category of polls
	for x in pollCat:
		#iterate through all the polls in the category
		for y in x.polls():
			if(y.pollster == Pollster):
				print y
	

if(len(sys.argv) != 2):
	print '\nUsage: python PollByPollster <pollster>'
	print 'If the pollster includes a space character, put it in quotes'
	print 'eg. <PPP (D)> won\'t work but <"PPP (D)"> will\n'
	print 'Pollsters:'
	print 'Gallup, ARG, PPP (D), Rasmussen, Suffolk, Quinnipiac, SurveyUSA, War Room Logistics, Magellan Research (R), CNN/Time, NBC/Marist, We Ask America, etc'
else:
	getPollsByPollster(sys.argv[1])