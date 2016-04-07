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
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

class TimeSeriesObject(AnalysisObject):
	
	#fixed_para_one: name of candidate
	#fixed_para_two:  Source
	#list_para_one: list of dates for x-values
	#list_para_two: list of counts for y values
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		super(TimeSeriesObject,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
	
	def __testStationarity(self,time_series,text_output):
		#Determing rolling statistics
		rol_mean = pd.rolling_mean(time_series,window=2)
		rol_std = pd.rolling_std(time_series,window=2)
		#Plot rolling statistics:
		plt.plot(time_series, color='blue',label='Original')
		plt.plot(rol_mean, color='red', label='Rolling Mean')
		plt.plot(rol_std, color='black', label = 'Rolling Std')
		plt.legend(loc='best')
		plt.title('Rolling Mean & Standard Deviation')
		#plt.show()
		plt.savefig('Rolling_Mean_Standard_Deviation',bbox_inches='tight',dpi=100)
		#Perform Dickey-Fuller test:
		text_output = text_output + 'Results of Dickey-Fuller Test:\n'
		text_output = text_output + 'In statistics, the Dickey–Fuller test tests whether a unit root is present in an autoregressive model. It is named after the statisticians David Dickey and Wayne Fuller, who developed the test in 1979.\n'
		df_test = adfuller(time_series)
		df_output = pd.Series(df_test[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
		for key,value in df_test[4].items():
			df_output['Critical Value (%s)'%key] = value
		text_output = text_output + str(df_output)
		if (df_output['Test Statistic'] < df_output['Critical Value (1%)']):
			text_output = text_output + "\nSince Text Statistic is smaller than Critical Value (1%): This is a stationarity.\n"
		elif (df_output['Test Statistic'] < df_output['Critical Value (5%)']):
			text_output = text_output + "\nSince Text Statistic is smaller than Critical Value (5%): This is a stationarity within Critical Value (5%).\n"
		elif (df_output['Test Statistic'] < df_output['Critical Value (10%)']):
			text_output = text_output + "\nSince Text Statistic is smaller than Critical Value (10%): This is a stationarity within Critical Value (10%).\n"
		else:
			text_output = text_output + "\nSince Text Statistic is greater than Critical Value (10%): This is NOT a stationarity.\n"
		return text_output
	
	def timeSeriesAnalysis(self):
		name = self.getfixed_para_one()
		source = self.getfixed_para_two()
		data_one = self.getlist_para_one()
		data_two = self.getlist_para_two()
		text_output = "TIME SERIES ANALYSIS\n"
		text_output = text_output + "Candidate Name: " + name + "\n"
		text_output = text_output + "Data is collected from " + data_one[0] + " to " + data_one[len(data_one)-1] + "\n"
		text_output = text_output+"A Time Series is said to be stationary if its statistical properties such as mean, variance remain constant over time.\n"
		text_output = text_output + "Stationarity is defined using very strict criterion. However, for practical purposes we can assume the series to be stationary if it has constant statistical properties over time, ie. the following:\n1.constant mean\n2.constant variance\n3.an autocovariance that does not depend on time\n"
		dates = []
		for x in data_one:
			dates.append(pd.Timestamp(x))
		dic = {'Date':dates,source:data_two}
		data = pd.DataFrame(dic)
		data_index = data.set_index(['Date'])
		ts = data_index[source]
		text_output = self.__testStationarity(ts,text_output)	
		return text_output
		
		
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return TimeSeriesObject(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
