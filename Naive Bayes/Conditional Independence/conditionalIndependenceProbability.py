# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:42:38 2021

@author: Kanav Farishta
"""

import pandas as pd


class conditionalIndependence():
    def __init__(self,X,Y,columns):
        self.data = X
        self.target = Y
        self.columns = columns
        self.dataFrame = None
        if(len(X[0]) != len(Y)):
            raise("Different Data Length")
        else:
            self.createDataFrame()
    def createDataFrame(self):
        self.dataFrame = pd.DataFrame(pd.DataFrame(self.data).transpose())
        self.dataFrame.columns = self.columns
        self.dataFrame['Target'] = self.target
    

    def probabilityOfTarget(self):
        dictOfTarget = {}
        keys = self.dataFrame['Target'].value_counts().keys()
        pairs = self.dataFrame['Target'].value_counts()
        length = len(self.dataFrame['Target'])
        for i in range(0,len(keys)):
            dictOfTarget[keys[i]] = pairs[i]/length
        return(dictOfTarget)
        
    def conditionalProb(self):
        targetProbDict = self.probabilityOfTarget()
        #print(targetProbDict)
        tempDf = self.dataFrame.iloc[:,:-1]
        probMatrix = {}
        columnName = tempDf.columns.tolist()
        for i in range(0,len(tempDf.columns)):
            for j in tempDf.iloc[:,i].unique():
                for k in self.dataFrame.iloc[:,-1].unique():
                    prob  = len(self.dataFrame[self.dataFrame.iloc[:,i]==j][self.dataFrame.iloc[:,-1]==k])/len(self.dataFrame)
                    targetProb = targetProbDict[k]
                    try:
                        key = 'P({}={}|{})'.format(str(columnName[i]),str(j),str(k))
                        probMatrix[key] = prob/targetProb
                    except ValueError as err:
                        print(err)
        return(probMatrix)
        
cols = ['CREDIT-HISTORY','GUARANTOR-COAPPLICANT','ACCOMMODATION']
X = [["current","paid",	"paid",	"paid",	"arrears","arrears","current","arrears","current","none",	"current","current","current","paid",	"arrears","current","arrears","arrears","arrears","paid",	],["none",		"none",		"none",		"guarantor",	"none",		"none",		"none",		"none",		"none",		"none",		"coapplicant","none",		"none",		"none",		"none",		"none",		"coapplicant","none",		"none",		"none",		],["own","own","own","rent","own","own","own","own","rent","own","own","own","rent","own","own","own","rent","free","own","own",]]

Y =["true","false","false","true","false","true","false","false","false","true","false","true","true","false","false","false","false","false","false","false"]


obj = conditionalIndependence(X,Y,cols)
#print(obj.dataFrame)
print(obj.conditionalProb())
        