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
		self.__fixed_para_one = fixed_para_one
		self.__fixed_para_two = fixed_para_two
		self.__list_para_one = list_para_one
		self.__list_para_two = list_para_two
		
	def getfixed_para_one(self):
		return self.__fixed_para_one
		
	def getfixed_para_two(self):
		return self.__fixed_para_two
		
	def getlist_para_one(self):
		return self.__list_para_one
		
	def getlist_para_two(self):
		return self.__list_para_two

