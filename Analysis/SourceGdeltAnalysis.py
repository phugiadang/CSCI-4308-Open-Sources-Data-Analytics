#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SourceGdeltAnalysis.py
#  
#  Phu Dang
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

import argparse
import csv
import operator
import datetime
import os
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt



def analysis(file_loc,name):
	text_output = 'GDELT SOURCE ANALYSIS\n'
	data = {}
	first_file = True
	os.getcwd()
	list_file = os.listdir(file_loc)
	for a in list_file:
		if name in a:
			if first_file == True:
				last_date = a[len(a)-12:len(a)-4]
			first_file = False
			first_date = a[len(a)-12:len(a)-4]
			loc = file_loc + a
			with open(loc,'rb') as f:
				reader = csv.reader(f, delimiter='\t')
				for row in reader:
					key = row[len(row)-2]
					if ';' in key:
						list_key = key.split(';')
						for k in list_key:
							if not data.has_key(k):
								data.update({k:1})
							else:
								data[k] = data[k]+1
					else:	
						if not data.has_key(key):
							data.update({key:1})
						else:
							data[key] = data[key]+1
	sort_data = sorted(data.items(),key=operator.itemgetter(1),reverse=True)
	text_output = text_output + "GDELT data is from " + first_date + " to " + last_date + "\n"
	text_output = text_output + "There are " + str(len(sort_data)) + " web sources that mention about " + name + "\n"
	text_output = text_output + "Top 10 web pages are:\n"
	top_ten_web = sort_data[:10]
	dic = {'Web Sources':[x[0] for x in top_ten_web],'Counts':[x[1] for x in top_ten_web]}
	data = pd.DataFrame(dic)
	data.index += 1
	# This following code is used to create graph
	data.plot(kind='barh',x='Web Sources',y='Counts')
	plt.savefig('top_ten_web'+name,bbox_inches='tight',dpi=100)
	###
	text_output = text_output + str(data)
	print text_output
	return 0

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Data Mining Project')
	parser.add_argument('-f', type=str, help="Location of csv files", required=True)
	parser.add_argument('-n', type=str, help="Name of candidate",required=True)
	args = parser.parse_args()
	if ( args.f and args.n ):
		analysis( args.f, args.n)

