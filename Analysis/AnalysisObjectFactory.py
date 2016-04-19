#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AnalysisObjectFactory.py
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
from GraphAnalysisNormalized import GraphAnalysisNormalized
from ClassificationAnalysis import ClassificationAnalysis
from LinearRegressionObject import LinearRegressionObject
from TimeSeriesObject import TimeSeriesObject
from RegressionAnalysis import RegressionObject
from TweetSentimentAnalysis import TweetSentimentAnalysis
from TweetAnalWord2Vec import TweetAnalWord2Vec
from ClusteringAnalysis import ClusteringAnalysis

class AnalysisObjectFactory:
	
	factories = {}
	
	@staticmethod
	def initialFactory():
		types = AnalysisObject.__subclasses__()
		for i in types:
			AnalysisObjectFactory.factories[i.__name__] = eval(i.__name__ + '.Factory()')
	
	
	@staticmethod
	def addFactory(id,analysisObjectFactory):
		AnalysisObjectFactory.factories.update({id:analysisObjectFactory})

	
	@staticmethod
	def createObject(id,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		return AnalysisObjectFactory.factories[id].create(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
	

