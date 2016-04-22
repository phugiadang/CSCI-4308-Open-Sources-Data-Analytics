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
import numpy as np
from statsmodels.tsa.arima_model import ARIMA


def test_stationarity(timeseries,term,text_output):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(window=24,center=False).mean()
    rolstd = timeseries.rolling(window=24,center=False).std()

    #Plot rolling statistics:
    fig = plt.figure()
    fig.add_subplot(111)
    rolmean.plot(color='red', label='Rolling Mean')
    rolstd.plot(color='black', label = 'Rolling Std')
    timeseries.plot(color='blue',label='Original')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation'+term)
    plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/rolling_mean_sd_'+term,bbox_inches='tight',dpi=100,block=False)
    dfoutput,text_output = dickeyFullertest(timeseries,term,text_output)
    return dfoutput,text_output
		
    
def dickeyFullertest(timeseries,term,text_output):
	#Perform Dickey-Fuller test:
    text_output = text_output + 'Results of Dickey-Fuller Test for '+term+' data:\n'
    dftest = adfuller(timeseries)
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    text_output = text_output + str(dfoutput)
    return dfoutput,text_output

class TimeSeriesObject(AnalysisObject):
	
	#fixed_para_one: name of candidate
	#fixed_para_two:  Source
	#list_para_one: list of dates for x-values
	#list_para_two: list of counts for y values
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		super(TimeSeriesObject,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
	
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
			year= int(x[0:4])
			month= int(x[4:6])
			date= int(x[6:8])
			hour= int(x[8:10])
			dates.append(pd.Timestamp(pd.datetime(year,month,date,hour)))
		dic = {'Date':dates,source:data_two}
		data = pd.DataFrame(dic)
		data_index = data.set_index(['Date'])
		ts = data_index[source]	
		fig = plt.figure()
		fig.add_subplot(111)
		ts.plot(title="Hourly Tweet Counts For "+name)
		plt.ylabel("Number of Tweet Counts")
		plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/daily_graph_'+name,bbox_inches='tight',dpi=100)
		dfoutput,text_output=test_stationarity(ts,"orginal_"+name,text_output)
		if dfoutput['Test Statistic'] < dfoutput['Critical Value (1%)']:
			text_output = text_output + "Since Test Statistic Value less than Critical Value (1%): Time Series is stationary for 99% confidence\n"
		elif dfoutput['Test Statistic'] < dfoutput['Critical Value (5%)']:
			text_output = text_output + "Since Test Statistic Value less than Critical Value (5%): Time Series is stationary for 95% confidence\n"
		elif dfoutput['Test Statistic'] < dfoutput['Critical Value (10%)']:
			text_output = text_output + "Since Test Statistic Value less than Critical Value (10%): Time Series is stationary for 90% confidence\n"
		else:
			text_output = text_output + 'ESTIMATING & ELIMINATING TREND:\n'
			exweight_avg = ts.ewm(halflife=12,ignore_na=False,min_periods=0,adjust=True).mean()
			fig = plt.figure()
			fig.add_subplot(111)
			plt.plot(ts)
			plt.plot(exweight_avg,color='red')
			plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/exponent_weight_moving_average_'+name,bbox_inches='tight',dpi=100)
			ts_log_ewma_diff = ts - exweight_avg
			ts_log_ewma_diff.dropna(inplace=True)
			dfoutput,text_output=test_stationarity(ts_log_ewma_diff,"perform_exp_weight_avg_"+name,text_output)
			ts_log = np.log(ts)
			ts_log_diff = ts_log - ts_log.shift()
			model = ARIMA(ts_log, order=(2,1,2))
			results_ARIMA = model.fit(disp=-1)
			predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues,copy=True)
			predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
			prediction_ARIMA_log = pd.Series(ts_log.ix[0],index=ts_log.index)
			prediction_ARIMA_log = prediction_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
			prediction_ARIMA = np.exp(prediction_ARIMA_log)
			fig = plt.figure()
			fig.add_subplot(111)
			ts.plot(label="Original")
			prediction_ARIMA.plot(label="Forecasting using ARIMA Model for "+name)
			plt.legend(loc='best')
			plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/Final_Result'+name,bbox_inches='tight',dpi=100)
		ts_diff = ts - ts.shift(1)
		model = ARIMA(ts, order=(2,1,2))
		results_ARIMA = model.fit(disp=-1)
		predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues,copy=True)
		predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
		prediction_ARIMA = pd.Series(ts.ix[0],index=ts.index)
		prediction_ARIMA = prediction_ARIMA.add((-1)*predictions_ARIMA_diff_cumsum,fill_value=0)
		#prediction_ARIMA = np.exp(prediction_ARIMA_log)
		#print prediction_ARIMA
		fig = plt.figure()
		fig.add_subplot(111)
		ts.plot(label="Original")
		prediction_ARIMA.plot(label="Forecasting using ARIMA Model for "+name)
		plt.legend(loc='best')
		plt.title('Time Series Forecasting for '+name)
		plt.savefig('../FrontEnd/NGC-FrontEnd/public/analysis-images/Final_Result'+name,bbox_inches='tight',dpi=100)
		f = open('../FrontEnd/NGC-FrontEnd/public/analysis-images/Time_Series_Analysis_'+name+'.txt','w')
		f.write(text_output)
		f.close()
		
		
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return TimeSeriesObject(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
