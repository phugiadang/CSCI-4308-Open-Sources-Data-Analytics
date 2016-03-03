#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ClassificationAnalysis.py
#  
#  Copyright 2016 user <user@cu-cs-vm>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from AnalysisObject import AnalysisObject

class ClassificationAnalysis(AnalysisObject):
	
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		list_two = self.__classification(list_para_two)
		super(ClassificationAnalysis,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_two)
	
	def __classification(self,data):
		sum_count = sum(data)
		normalized = []
		for num in data:
			normalized.append((float(num)/float(sum_count)*100))
		return normalized
	
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return ClassificationAnalysis(fixed_para_one,fixed_para_two,list_para_one,list_para_two)


