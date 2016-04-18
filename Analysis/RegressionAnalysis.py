from AnalysisObject import AnalysisObject
import numpy as np
from scipy.interpolate import *
import scipy.stats as stats
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class RegressionObject(AnalysisObject):
    #should take, for example, (candidate, [dates that are fixed], [daily tweet counts], [daily poll counts])
    def __init__(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):
	super(RegressionObject,self).__init__(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
        self.order = 1
        print 'List paramater one: ' + str(list_para_one)
        #split into training data and observational data
        training_len_one = len(list_para_one)*80/100-1
        self.training_one = list_para_one[0:training_len_one]
        self.training_two = list_para_two[0:training_len_one]
        self.obs_one = list_para_one[training_len_one:len(list_para_one)]
        self.obs_two = list_para_two[training_len_one:len(list_para_one)]
        self.Interpolate()

    def Interpolate(self):

        if(len(self.training_one) != len(self.training_two)):
            print 'Arrays are not of the same length!'
            print 'x length: ' + str(len(self.training_one))
            print 'y length: ' + str(len(self.training_two))
            return

        plt.plot(self.training_one, self.training_two, 'o')

        xp = np.linspace(-2, 6, 100)
        print 'Training Data: ' + str(self.training_one) + ', ' + str(self.training_two)
        coeff = np.polyfit(self.training_one, self.training_two, self.order)

        plt.plot(xp, np.polyval(coeff, xp), 'b')
        
        #print the equation
        result_string = ''
        i = self.order
        j = 0
        while i>= 0:
            if(j != 0):
                result_string = ' + ' + result_string
            result_string = str(coeff[i]) + 'x^' + str(j) + result_string
            i = i - 1
            j += 1
        
        result_string = 'y = ' + result_string

        #calculate the predictions by evaluating the x-values of each observational point
        predictions = []
        c = 0
        while c < len(self.obs_one):
            current_prediction = 0
            i = self.order
            j = 0
            while i >= 0:
                current_prediction += coeff[i] * pow(self.obs_one[c], j)
                i = i - 1
                j += 1
            predictions.append([self.obs_one[c], current_prediction])
            c += 1

        #Print the equation of the best fit line
        print result_string
        
        #print the training data
        print 'Training Data: ' + str(self.training_one) + ', ' + str(self.training_two)
        
        #print actual points and predictions
        print '\nActual Point, Prediction'
        print '-----------------------'
        i = 0
        while i < len(predictions):
            print str([self.obs_one[i], self.obs_two[i]]) + '   |   ' + str(predictions[i])
            i += 1

        #calculate and print r-squared (only measures on training data)
        p = np.poly1d(coeff)
        yhat = p(self.training_one)
        ybar = np.sum(self.training_two)/len(self.training_two)
        ssreg = np.sum((yhat-ybar)**2)
        sstot = np.sum((self.training_two-ybar)**2)
        r_squared = ssreg/sstot
        print 'R^2: ' + str(r_squared)

        #other stuff for linear regression because why not
        #slope, intercept, r_value, p_value, std_err = stats.linregress(self.x, self.y)


        plt.savefig('interpolation.jpg')
        #plt.show()
    class Factory:
	def create(self,fixed_para_one,fixed_para_two,list_para_one,list_para_two):return RegressionObject(fixed_para_one,fixed_para_two,list_para_one,list_para_two)
