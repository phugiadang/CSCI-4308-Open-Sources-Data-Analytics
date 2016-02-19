#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gdelt.py
#  
#  Copyright 2015 user <user@cu-cs-vm>
#  
#  Reference: http://nbviewer.jupyter.org/github/JamesPHoughton/Published_Blog_Scripts/blob/master/GDELT%20Wrangler%20-%20Clean.ipynb
#  Phu Dang
#  
#  
<<<<<<< HEAD

=======
>>>>>>> 79a87fe3bae985f02bd033fdf3f842a639a5c8c8
import argparse
import requests
import lxml.html as lh
import os.path
import urllib
import zipfile
import glob
import operator
import sys
#import pandas



gdelt_base_url = 'http://data.gdeltproject.org/gkg/'
local_path = '/home/user/Downloads/GDELT Data/'
key_word = ''

def setKeyword(name):
	global key_word
	key_word = name.split(",")

def prepareData(begin_date):
	infilecounter = 0
	outfilecounter = 0
	counter = 1
	# get the list of all the links on the gdelt file page
	page = requests.get(gdelt_base_url+'index.html')
	doc = lh.fromstring(page.content)
	link_list = doc.xpath("//*/ul/li/a/@href")

	# separate out those links that begin with four digits 
	file_list = [x for x in link_list if str.isdigit(x[0:4])]


	for compressed_file in file_list[infilecounter:]:
		if (counter%2 != 0):
			print compressed_file ,
		
			# if we dont have the compressed file stored locally, go get it. Keep trying if necessary.
			while not os.path.isfile(local_path+compressed_file): 
				print 'downloading,',
				urllib.urlretrieve(url=gdelt_base_url+compressed_file, 
							filename=local_path+compressed_file)
        
			# extract the contents of the compressed file to a temporary directory    
				print 'extracting,',
			z = zipfile.ZipFile(file=local_path+compressed_file, mode='r')    
			z.extractall(path=local_path+'tmp/')
    
			# parse each of the csv files in the working directory, 
			print 'parsing,',
			for name in key_word:
				for infile_name in glob.glob(local_path+'tmp/*'):
					outfile_name = local_path+name.replace(" ","")+compressed_file[:compressed_file.find(".")]+'.tsv'
					# open the infile and outfile
					with open(infile_name, mode='r') as infile, open(outfile_name, mode='w') as outfile:
						for line in infile:
							# extract lines with our interest country code
							if name in operator.itemgetter(6)(line.split('\t')):    
								outfile.write(line)
					outfilecounter +=1
            
				# delete the temporary file
			os.remove(infile_name)
			infilecounter +=1
			print 'done'
	
		counter=counter+1
		if (begin_date in compressed_file):
			break
		
#We may not need this function
def turnToPandas():
	file_name = key_word.replace(" ","")
	# Get the GDELT field names from a helper file
	colnames = pandas.read_excel('CSV.header.fieldids.xlsx', sheetname='Sheet1', 
                         index_col='Column ID', parse_cols=1)['Field Name']

	# Build DataFrames from each of the intermediary files
	files = glob.glob(local_path+file_name+'*')
	print files
	DFlist = []
	for active_file in files:
		print active_file
		DFlist.append(pandas.read_csv(active_file, sep='\t', header=None, dtype=str,
                              names=colnames, index_col=['GLOBALEVENTID']))

		# Merge the file-based dataframes and save a pickle
		DF = pandas.concat(DFlist)
		DF.to_pickle(local_path+'backup'+key_word+'.pickle')    
    
		# once everythin is safely stored away, remove the temporary files
		for active_file in files:
			os.remove(active_file)
	
<<<<<<< HEAD

=======
>>>>>>> 79a87fe3bae985f02bd033fdf3f842a639a5c8c8
def main():
	parser = argparse.ArgumentParser(description='Senior project')
	#flag n: name of candidate
	parser.add_argument("-n", type=str, help="List of the candidates in form first last,first last", required=True)
	#flag e: begin date
	parser.add_argument("-e", type=str, help="Begin date", required=False)
	args = parser.parse_args()
	setKeyword(args.n)
	prepareData(args.e)
	
<<<<<<< HEAD

=======
>>>>>>> 79a87fe3bae985f02bd033fdf3f842a639a5c8c8
	
if __name__ == '__main__':
	main()
