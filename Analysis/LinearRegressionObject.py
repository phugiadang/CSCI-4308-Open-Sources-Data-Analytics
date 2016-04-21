#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LinearRegressionObject.py
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
import numpy as np
from sklearn import linear_model
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

class LinearRegressionObject(AnalysisObject):

	#fixed_para_one: name of candidate
	#fixed_para_two: list of dates
	#list_para_one: list (source, list of counts) for x-values
	#list_para_two: list (source, list of counts) for y values
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
                print 'LinearRegressionObject X: ' + str(list_para_one)
                print 'LinearRegressionObject Y: ' + str(list_para_two)
		super(LinearRegressionObject,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)

	#use to calculate the corellation between two data sets
	def __correlationCalculation(self):
		correl = np.corrcoef(self.getlist_para_one()[1],self.getlist_para_two()[1])[0][1]
		if (correl == 0):
			return "Two variable sets are uncorrelated.\n"
		elif (correl > 0):
			return "There is a positive correlation: one variable set moves the the same direction by "+str(abs(correl))+" the amount that the other variable set moves.\n"
		else:
			return "There is a negative correlation: one variable set moves the the opposite direction by "+str(abs(correl))+" the amount that the other variable set moves.\n"


	def __graphData(self, data,slope,intercept,training):
		data.plot(kind='scatter',x=self.getlist_para_one()[0],y=self.getlist_para_two()[0])
		x_eval = self.getlist_para_one()[1][training:]
		y_eval = self.getlist_para_two()[1][training:]
		b = plt.scatter(x_eval,y_eval,c='yellow')
		x = []
		y = []
		for k in self.getlist_para_one()[1]:
			x.append(k)
			y_value = slope * k + intercept
			y.append(y_value)
		line, = plt.plot(x,y,c='red',linewidth=2)

		linear_reg = plt.savefig('report'+self.getfixed_para_one()+self.getlist_para_one()[0]+self.getlist_para_two()[0])
		f = open('../FrontEnd/NGC-FrontEnd/public/analyis-images/' + 'report'+ self.getfixed_para_one()+self.getlist_para_one()[0]+self.getlist_para_two()[0], 'w')
		f.write(linear_reg)

		plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/report'+self.getfixed_para_one()+self.getlist_para_one()[0]+self.getlist_para_two()[0])
	
	#Return the tuples of (report,(date,predict values, exact values))
	def linearRegressionAnalysis(self):
		text_output = "LINEAR REGRESSION ANALYSIS\n"
		text_output = text_output + "Candidate name: " + self.getfixed_para_one() + "\n"
		text_output = text_output + self.__correlationCalculation()
		fixed_para_two = self.getfixed_para_two()
		if text_output != "Two variable sets are uncorrelated.\n":
			training = int(len(fixed_para_two)*80/100)
			text_output = text_output + "Trainning data is from "+fixed_para_two[0]+" to "+fixed_para_two[training-1]+".\n"
			text_output = text_output + "Evaluation data is from "+fixed_para_two[training]+" to "+fixed_para_two[len(fixed_para_two)-1]+".\n"
			regr = linear_model.LinearRegression()
			dic = {self.getlist_para_two()[0]:self.getlist_para_two()[1][:training-1],self.getlist_para_one()[0]:self.getlist_para_one()[1][:training-1]}
			data = pd.DataFrame(dic)
			data.index += 1
			X = data[[self.getlist_para_one()[0]]]
			y = data[self.getlist_para_two()[0]]
			text_output = text_output + "x value is " + self.getlist_para_one()[0] + "\n"
			text_output = text_output + "y value is " + self.getlist_para_two()[0] + "\n"
			regr.fit(X,y)
			slope = regr.coef_[0]
			intercept = regr.intercept_
			text_output = text_output + "Coefficient computes from linear regression model:\n" + self.getlist_para_one()[0] + ", " + str(slope) + "\n"
			text_output = text_output + "Interception computes from linear regression model:\n" + self.getlist_para_one()[0] + ", " + str(intercept) + "\n"
			text_output = text_output + "Linear approximation line has form: y = " + str(slope) + " x + " + str(intercept) + "\n"
			dic_eval = {self.getlist_para_two()[0]:self.getlist_para_two()[1][training:],self.getlist_para_one()[0]:self.getlist_para_one()[1][training:]}
			data_eval = pd.DataFrame(dic_eval)
			data_eval.index += 1
			X_eval = data_eval[[self.getlist_para_one()[0]]]
			y_eval = data_eval[self.getlist_para_two()[0]]
			mean_sqr_err = np.mean((regr.predict(X_eval)-y_eval)**2)
			score = regr.score(X_eval,y_eval)
			text_output = text_output + "Mean square error is " + str(mean_sqr_err) + "\n"
			text_output = text_output + "Score of this prediction " + str(score) + "\n"
			text_output = text_output + "(Note: if score number equals 1, there is a perfect prediction and a strong linear relationship between two variables)\n"
			self.__graphData(data,slope,intercept,training)
			y_exact = self.getlist_para_two()[1][training:]
			y_predict = []
			date = []
			for x in range (training,len(fixed_para_two)):
				date.append(fixed_para_two[x])
				y_predict.append(int(slope*self.getlist_para_one()[1][x]+intercept))
			return (text_output,(date,y_predict,y_exact))


	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return LinearRegressionObject(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
