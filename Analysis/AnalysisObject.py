#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AnalysisObject.py
#  
#  Copyright 2016 user <user@cu-cs-vm>
#  
#  Phu Dang

import numpy as np

# Use to create instance of object
# 4 variables: fixed_para_one: 1st fixed parameter, fixed_para_two: 2nd fixed parameter,
# list_para_one: list of 1st variable parameters, list_para_two: list of 2nd variable parameters
class AnalysisObject(object):
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		#candidate
		self.__fixed_para_one = fixed_para_one
		#source
		self.__fixed_para_two = fixed_para_two
		#Date
		self.__list_para_one = list_para_one
		#count
		self.__list_para_two = list_para_two
		
	def getfixed_para_one(self):
		return self.__fixed_para_one
		
	def getfixed_para_two(self):
		return self.__fixed_para_two
		
	def getlist_para_one(self):
		return self.__list_para_one
		
	def getlist_para_two(self):
		return self.__list_para_two
	
	def createJson(self):
		counts = self.getlist_para_two()
		candidate = self.getfixed_para_one().title()
		source = self.getfixed_para_two()
		print counts
		jsonCandidateString = '''{
                    "seriesname": "''' + candidate + ''' ''' + source + ''' Counts",
                    "data": [ '''
		for i in range(0,len(counts)-1):
			jsonCandidateString += '{ "value": "' + str(counts[i]) + '" },'
		jsonCandidateString += '{ "value": "' + str(counts[len(counts)-1]) + '" }]}'
		return jsonCandidateString	
