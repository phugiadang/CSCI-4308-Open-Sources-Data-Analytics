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
#import IPython.display as IPdisplay
import glob
from PIL import Image as PIL_Image
from images2gif import writeGif
from AnalysisObject import AnalysisObject
from sklearn.cluster import KMeans
import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from AnalysisObject import AnalysisObject

def makeGif(p_df,labels,candidates,date):
	threedee = plt.figure().gca(projection='3d')
	threedee.scatter(p_df['Twitter'], p_df['GDELT'], p_df['Poll'],c=labels.astype(np.float))
	for name in candidates:
		a = p_df.T[name]
		x=a['Twitter']
		y=a['GDELT']
		z=a['Poll']
		threedee.text(x,y,z,name,size=10,color='k')
	threedee.set_xlabel('Twitter')
	threedee.set_ylabel('GDELT')
	threedee.set_zlabel('Poll')
	plt.title("Clustering Candidates on "+date)
	threedee.elev = 89.9
	threedee.azim = 270.1
	threedee.dist = 11.0
	for n in range(0, 100):
		if n >= 20 and n <= 22:
			threedee.set_xlabel('')
			threedee.set_ylabel('')
			threedee.set_zlabel('')
			threedee.elev = threedee.elev-0.5
		if n >= 23 and n <= 36:
			#threedee.dist = 11.0
			threedee.elev = threedee.elev-1.0 
		if n >= 37 and n <= 60:
			threedee.elev = threedee.elev-1.5
			threedee.azim = threedee.azim+1.1
		if n >= 61 and n <= 64:
			threedee.elev = threedee.elev-1.0
			threedee.azim = threedee.azim+1.1
		if n >= 65 and n <= 73:
			threedee.elev = threedee.elev-0.5
			threedee.azim = threedee.azim+1.1
		if n >= 74 and n <= 76:
			threedee.elev = threedee.elev-0.2
			threedee.azim = threedee.azim+0.5
		if n == 77:
			threedee.set_xlabel('Twitter')
			threedee.set_ylabel('GDELT')
			threedee.set_zlabel('Poll')
		plt.savefig('home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/images/img' + str(n).zfill(3) + '.png',bbox_inches='tight')
	plt.close()
	images = [PIL_Image.open(image) for image in glob.glob('home/centos/CSCI-4308-Open-Sources-Data-Analytics/Analysis/images/*.png')]
	file_path_name = 'home/centos/CSCI-4308-Open-Sources-Data-Analytics/FrontEnd/NGC-FrontEnd/public/analysis-images/Clustering_Candidates.gif'
	writeGif(file_path_name, images, duration=0.2, dither=0)
	

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
		text_output = "CLUSTERING ANALYSIS\n"
		text_output = text_output + "Question we want to answer for this analysis is how to group the candidates based on their tweets, GDELT, and Poll datas. From the clustering result, we can see the combination of all 3 sources for each candidates and their groups.\n"
		text_output = text_output + "Clustering technique: K Means\n"
		data={}
		list_para_one = self.getlist_para_one()
		list_para_two = self.getlist_para_two()
		for i in xrange(0,len(list_para_one)):
			data[list_para_one[i]]=list_para_two[i]
		candidates=data.keys()
		p_df = pd.DataFrame.from_dict(data,orient='index')
		kmeans = KMeans(init='k-means++', n_clusters=self.getfixed_para_two(), n_init=10)
		kmeans.fit(p_df)
		labels = kmeans.labels_
		threedee = plt.figure().gca(projection='3d')
		threedee.scatter(p_df['Twitter'], p_df['GDELT'], p_df['Poll'],c=labels.astype(np.float))
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
		for i in xrange(0,self.getfixed_para_two()):
			text_output = text_output + "*Cluster "+str(i)+":\n"
			for j in xrange(0,len(labels)):
				if labels[j]==i:
					name=p_df.iloc[j].to_dict()
					k=list_para_two.index(name)
					text_output = text_output + "-"+str(list_para_one[k])+"\n"+p_df.iloc[j].to_string(header=False) + "\n"			
		f = open('home/centos/CSCI-4308-Open-Sources-Data-Analytics/FrontEnd/NGC-FrontEnd/public/analysis-images/Clustering_Candidates.txt','w')
		f.write(text_output)
		f.close()
		makeGif(p_df,labels,candidates,self.getfixed_para_one())
		
	
		
	class Factory:
		def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return ClusteringAnalysis(fixed_para_one,fixed_para_two,list_para_one,list_para_two)

