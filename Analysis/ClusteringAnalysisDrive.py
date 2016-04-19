#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ClsuteringAnalysisDrive.py
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
	types = AnalysisObjectFactory.createObject("ClusteringAnalysis","2/17/2016",3,['Clinton','Sanders','Trump','Kasich'],[{'Poll':100.0,'GDELT':10.0,'Twitter':123.0},{'Poll':25.0,'GDELT':5.0,'Twitter':1234.0},{'Poll':10.0,'GDELT':4.0,'Twitter':145.0},{'Poll':5.0,'GDELT':4.0,'Twitter':145.0}])
	types.clusterAnalysis()
	return 0

if __name__ == '__main__':
	main()

