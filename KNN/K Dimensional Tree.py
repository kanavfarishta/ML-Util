# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:52:37 2020

@author: Kanav Farishta
"""

# K Dimension Representation Graphically 
import pandas as pd
import matplotlib.pyplot as plt
#Scenario 1 

class Node:
    def __init__(self,data,depth,typ):
        self.left = None
        self.right = None
        self.data = data
        self.depth = depth
        self.type = typ
        
    def insert(self,depth):
#        print("Self Depth",":",self.depth)
#        print("Depth",":",depth)
        if(int(self.depth)==depth):
            return
        else:
            if(self.type==int):
                #Meaning divide by X
                temp = self.data
                median = temp["X"].median()
                self.left = Node(temp[temp["X"]<=median],self.depth+0.5,float)
                self.right = Node(temp[temp["X"]>median],self.depth+0.5,float)
                plt.plot([median,median],[max(self.data["Y"]),min(self.data["Y"])])
                self.left.insert(depth)
                self.right.insert(depth)
            if(self.type==float):
                #Meaning divide by Y
                temp = self.data
                median = temp["Y"].median()
                self.left = Node(temp[temp["Y"]<=median],self.depth+0.5,int)
                self.right = Node(temp[temp["Y"]>median],self.depth+0.5,int)
                plt.plot([max(self.data["X"]),min(self.data["X"])],[median,median])
                self.left.insert(depth)
                self.right.insert(depth)
                
    def printTree(self):
        if self.left:
            self.left.printTree()
        print("Data",self.data)
        print("Depth",self.depth)
        print("<===========>")
        if self.right:
            self.right.printTree()
            
    
        
class KDTree:
    def TwoDTree(self,depth,x_axis,y_axis):
        if(type(depth)!=int):
            raise Exception("Depth must be a positive Integer")
        else:
            if(depth<0):
                raise Exception("Depth must be positive")
            elif(depth==0):
                return
            df = pd.DataFrame(list(zip(x_axis,y_axis)),columns=["X","Y"])
            root = Node(df,0,int)
            plt
            root.insert(2)
            plt.xlabel("x Axis")
            plt.ylabel("y Axis")
            plt.show()
            #root.printTree()

data = pd.read_csv(r'C:\Users\Kanav Farishta\Downloads\archive\train.csv')
op = KDTree()
op.TwoDTree(1,data["x"].tolist(),data["y"].tolist())



            
            
                
            