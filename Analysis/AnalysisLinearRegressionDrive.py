#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AnalysisLinearRegressionDrive.py
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


def main():
	AnalysisObjectFactory.initialFactory()
	#types = AnalysisObjectFactory.createObject("LinearRegressionObject","hillary clinton",["2/17/2016","2/18/2016","2/19/2016","2/20/2016","2/21/2016","2/22/2016","2/23/2016"],("GDELT",[1,2,3,7,4,5,6]),("Tweet",[5,10,15,20,20,25,35]))
	types = AnalysisObjectFactory.createObject("LinearRegressionObject","hillary clinton",["2/17/2016","2/18/2016","2/19/2016","2/20/2016","2/21/2016","2/22/2016","2/23/2016"],("GDELT",[1,2,3,7,4,3,10]),("Tweet",[20,10,15,20,5,17,21]))
	print types.linearRegressionAnalysis()
	return 0

if __name__ == '__main__':
	main()

