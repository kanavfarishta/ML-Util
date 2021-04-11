# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:36:00 2021

@author: Kanav Farishta
"""
import pandas as pd


class smoothingProb():
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
    
    
    def smoothingConditProb(self,k0):
        """P(x=A|B) = {count(x=A|B) + K}/{count(x=A|B) + K} +domain(x)"""
        tempDf = self.dataFrame.iloc[:,:-1]
        probMatrix = {}
        columnName = tempDf.columns.tolist()
        for i in range(0,len(tempDf.columns)):
            domain = len(tempDf.iloc[:,i].unique())
            for k in self.dataFrame.iloc[:,-1].unique():
                keys = self.dataFrame[columnName[i]][self.dataFrame.iloc[:,-1]==k].value_counts().keys()
                values = self.dataFrame[columnName[i]][self.dataFrame.iloc[:,-1]==k].value_counts()
                for j in range(0,len(values)):
                    inpKey = 'P({}={}|Target={})'.format(str(columnName[i]),str(keys[j]),str(k))
                    probMatrix[inpKey] = (values[j] + int(k0))/(values[j] + int(k0)*domain)
        return(probMatrix)

cols = ['CREDIT-HISTORY','GUARANTOR-COAPPLICANT','ACCOMMODATION']
X = [["current","paid",	"paid",	"paid",	"arrears","arrears","current","arrears","current","none",	"current","current","current","paid",	"arrears","current","arrears","arrears","arrears","paid",	],["none",		"none",		"none",		"guarantor",	"none",		"none",		"none",		"none",		"none",		"none",		"coapplicant","none",		"none",		"none",		"none",		"none",		"coapplicant","none",		"none",		"none",		],["own","own","own","rent","own","own","own","own","rent","own","own","own","rent","own","own","own","rent","free","own","own",]]

Y =["true","false","false","true","false","true","false","false","false","true","false","true","true","false","false","false","false","false","false","false"]


obj = smoothingProb(X,Y,cols)

print(obj.smoothingConditProb(3))
