from AnalysisObjectFactory import AnalysisObjectFactory
import numpy as np
from sklearn import linear_model
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import GetHourlyTweetsDayRange
from RegressionReadyPolls import RegressionReadyPolls
from GetPollsFromDatabase import DatabasePolls
from RegressionAnalysis import RegressionObject
import GetDailyGDELTCounts
import sys

AnalysisObjectFactory.initialFactory()



