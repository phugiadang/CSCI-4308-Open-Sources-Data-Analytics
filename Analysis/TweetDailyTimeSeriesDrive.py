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
import collections
from AnalysisObjectFactory import AnalysisObjectFactory


def main():
	dic = QueryingDavid.candidateCountRangeHourlyDict("trump","2016041100","2016041700")
	ordered_dic = collections.OrderedDict(sorted(dic.items()))
	dates =[]
	count =[]
	for item in ordered_dic:
		dates.append(item)
		count.append(float(ordered_dic[item]))
	AnalysisObjectFactory.initialFactory()
	types = AnalysisObjectFactory.createObject("TimeSeriesObject","trump","Twitter",dates,count)
	text= types.timeSeriesAnalysis()
	return 0

if __name__ == '__main__':
	main()


