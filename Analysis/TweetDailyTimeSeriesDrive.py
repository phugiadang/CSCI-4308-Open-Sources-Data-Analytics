#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TweetDailyTimeSeriesDrive.py
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

import QueryingDavid

from AnalysisObjectFactory import AnalysisObjectFactory


def main():
	dic = QueryingDavid.candidateCountRangeHourlyDict("sanders","2016032800","2016040400")
	print dic
	#AnalysisObjectFactory.initialFactory()
	#types = AnalysisObjectFactory.createObject("TimeSeriesObject","hillary clinton","GDELT",["2/17/2016","2/18/2016","2/19/2016","2/20/2016","2/21/2016","2/22/2016","2/23/2016","2/24/2016","2/25/2016","2/26/2016","2/27/2016","2/28/2016","2/29/2016","3/1/2016"],[1,2,3,7,4,3,10,1,2,3,7,4,3,10])
	#text= types.timeSeriesAnalysis()
	#print text
	return 0

if __name__ == '__main__':
	main()


