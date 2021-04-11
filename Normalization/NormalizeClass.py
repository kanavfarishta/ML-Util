# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:40:37 2020

@author: Kanav Farishta
"""

# =============================================================================
#Normalization Code  
#       Range Normalization
#   Kanav Utils- Pt.1
# =============================================================================

import pandas as pd 
import numpy as np

class Normalize():
    def __init__(self,input_array):
        self.input = pd.Series(input_array)
    def mean(self):
        return(self.input.mean())
    def rangeNormalize(self,upper,lower):
        if(min(self.input)==max(self.input)):
            return(self.input)
        opp = self.input - min(self.input)
        opp = opp /(max(self.input)-min(self.input))
        return(opp * (upper-lower) - lower)
    
# =============================================================================
#         a' = [a - min(a)]/max(a) - min(a)
# =============================================================================

