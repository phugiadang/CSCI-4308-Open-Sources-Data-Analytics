#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ClusteringAnalysis.py
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

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import animation
from AnalysisObject import AnalysisObject
from sklearn.cluster import KMeans
import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from AnalysisObject import AnalysisObject



class ClusteringAnalysis(AnalysisObject):
	
	#fixed_para_one: name of candidate
	#fixed_para_two:  list of dates
	#list_para_one: list of userids for x-values
	#list_para_two: list of list of tweets for y values
	def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
		super(ClusteringAnalysis,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
		
	def clusterAnalysis(self):
		self.__clustering()
		
	def __clustering(self):
		data={}
		list_para_one = self.getlist_para_one()
		list_para_two = self.getlist_para_two()
		for i in xrange(0,len(list_para_one)):
			data[list_para_one[i]]=list_para_two[i]
		candidates=data.keys()
		p_df = pd.DataFrame.from_dict(data,orient='index')
		print p_df
		kmeans = KMeans(init='k-means++', n_clusters=self.getfixed_para_two(), n_init=10)
		kmeans.fit(p_df)
		labels = kmeans.labels_
		print labels
		threedee = plt.figure().gca(projection='3d')
		threedee.scatter(p_df['Twitter'], p_df['GDELT'], p_df['Poll'],c=labels.astype(np.float),edgecolors="green")
		for name in candidates:
			a = p_df.T[name]
			x=a['Twitter']
			y=a['GDELT']
			z=a['Poll']
			threedee.text(x,y,z,name,size=10,color='k')
		threedee.set_xlabel('Twitter')
		threedee.set_ylabel('GDELT')
		threedee.set_zlabel('Poll')
		plt.title("Clustering Candidates on "+self.getfixed_para_one())
		plt.savefig('home/centos/CSCI-4308-Open-Sources-Data-Analytics/FrontEnd/NGC-FrontEnd/public/analysis-images/Clustering_Candidates',bbox_inches='tight',dpi=100)
		
	def init():
		return 0
		
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return ClusteringAnalysis(fixed_para_one,fixed_para_two,list_para_one,list_para_two)

#clustering()
