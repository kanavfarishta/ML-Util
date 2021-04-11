# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:34:07 2020

@author: Kanav Farishta
"""
import math
import pandas as pd
def total_entropy(target):
    try:
        unique_op = set(target)
        entropy = 0
        length = len(target)
        for i in unique_op:
            count = target.count(i)
            entropy = entropy -1*(count/length * math.log2(count/length))
        return(entropy)
    except:
        return(target,"is not iterable")

def rem_entropy_discrete(X_label,target):
    if(type(X_label)==str):
        X_label = list(X_label)
    X = pd.DataFrame({"F1":X_label,'Target':target})
    unique_outcome = set(target)
    unique_input = set(X_label)
    remEntr = 0
    targetLength = len(target)
    for i in unique_input:
        boolMap = X['F1'] == i
        temp = X[boolMap]
        leng = len(temp)
        entropy = 0
        for j in unique_outcome:
            countVal = list(temp['Target']).count(j)
            if(countVal):
                entropy = entropy - (countVal/leng)* math.log2(countVal/leng)
        remEntr = remEntr +(leng/targetLength)*entropy
    return(remEntr)

def gini_index(target):
    gini = 1
    leng= len(target)
    for i in set(target):
        count = target.count(i)
        gini = gini - (count/leng)**2
    return gini

def continiousFeatureToDiscrete(feature, target):
    df = pd.DataFrame(list(zip(feature,target)), columns = ['F1','target'])
    df = df.sort_values("F1")
    
    
#print(total_entropy("oxymoron"))
#print(total_entropy(3132143)) 
#print(total_entropy(['t','f','t','t','f','f'])) 
#F1 = [False,False,False,False,True ,False,]
#target = [True ,False,True ,False,True ,False,]
#print(rem_entropy_discrete(F1,target))  
print(gini_index([0,0,1,1,1,1,1,4]))