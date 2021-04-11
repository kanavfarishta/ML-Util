# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:17:45 2020

@author: Kanav Farishta
"""

class Shingling():
    def __init__(self,file_loc):
        file = open(file_loc,'r')
        self.data = file.read()
        file.close()
    def characterShingle(self,k):
        temp = self.data.replace(' ','')
        #Removing \n character
        temp = temp[0:-2]
        shingle = set()
        for i in range(0,len(temp)-k+1):
            shingle.add(temp[i:i+k])
        return(shingle)
    def wordShingle(self,k):
        temp = self.data[0:-2]
        temp = self.data.split(" ")
        shingle = set()
        for i in range(0,len(temp)-k+1):
            temp_str = ""
            for j in range(i,i+k):
                temp_str = temp_str+" "+temp[j]
            shingle.add(temp_str)
        return(shingle)

class DocSimilarity():
    def __init__(self,loc1,loc2):
        self.obj1 = Shingling(loc1)
        self.obj2 = Shingling(loc2)
    def JaccardSimilarity(self,length,Jtype):
        """
        Jtype = 0 for Character Shingling
        Jtype = 1 for Word Shingling
        """
        if(Jtype==0):
            s1 = self.obj1.characterShingle(length)
            s2 = self.obj2.characterShingle(length)    
        elif(Jtype==1):
            s1 = self.obj1.wordShingle(length)
            s2 = self.obj2.wordShingle(length)
        else:
            raise Exception("Please choose a valid Type")
        if(len(s1)==len(s2)==0):
            return(0)
        unions = s1.union(s2)
        intersects = s1.intersection(s2)
        return(len(intersects)/len(unions))

        
        
doc1 = r'C:\Code\ML\Util\KNN\Shingling and Hashing\Dataset\D1.txt'
doc2 = r'C:\Code\ML\Util\KNN\Shingling and Hashing\Dataset\D2.txt'
doc3 = r'C:\Code\ML\Util\KNN\Shingling and Hashing\Dataset\D3.txt'
doc4 = r'C:\Code\ML\Util\KNN\Shingling and Hashing\Dataset\D4.txt'

obj = DocSimilarity(doc1,doc3)

print(obj.JaccardSimilarity(length = 2, Jtype = 1))


        