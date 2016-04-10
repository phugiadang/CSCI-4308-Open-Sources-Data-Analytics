#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AnalysisDrive.py
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

from AnalysisObjectFactory import AnalysisObjectFactory
import numpy as np

def linearRegressionObject():
        AnalysisObjectFactory.initialFactory()
	types = AnalysisObjectFactory.createObject("LinearRegressionObject","hillary clinton",["2/17/2016","2/18/2016","2/19/2016","2/20/2016","2/21/2016","2/22/2016","2/23/2016"],("GDELT",[1,2,3,7,4,3,10]),("Tweet",[20,10,15,20,5,17,21]))
	(text,data)= types.linearRegressionAnalysis()
	print text
	print data
	return 0

def classificationAnalysis():
        AnalysisObjectFactory.initialFactory()
	types = AnalysisObjectFactory.createObject("ClassificationAnalysis","2/23/2016","gdelt",["hilary clinton","donaldtrump","ted cruz"],[9,8,2])
	print types.getlist_para_two()

def graphAnalysis():
        AnalysisObjectFactory.initialFactory()
        types = AnalysisObjectFactory.createObject("GraphAnalysisNormalized","hilary clinton","gdelt",["2/23/2016","2/22/2016"],[15,23])
        print types.getlist_para_two()


def regressionObject():
        fake_tweets = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        #change these values to plot different points
        fake_polls = np.array([3, 2, 5, 0, 4, 10, 7, 0, 5])

        AnalysisObjectFactory.initialFactory()
        types = AnalysisObjectFactory.createObject("RegressionObject", "Bernie", "Dates I guess", fake_tweets, fake_polls)
        types.Interpolate()

def timeSeriesObject():
        AnalysisObjectFactory.initialFactory()
        types = AnalysisObjectFactory.createObject("TimeSeriesObject", "Trump", "Date", [1, 2, 3, 4, 5, 6, 7, 8], [10, 8, 4, 6, 7, 5, 9, 2])
        print types.getlist_para_two()

def main():
        
        #linearRegressionObject()
        #print 'Regression Analysis:'
        #regressionObject()
        #print '\nClassification Analysis: '
        #classificationAnalysis()
        #print '\nGraph Analysis: '
        #graphAnalysis()
        #print '\nLinear Regression Analysis: '
        #linearRegressionObject()
        #print '\nTime Series Analysis: '
	timeSeriesObject()

if __name__ == '__main__':
	main()




