#!/usr/bin/env python3

import matplotlib.pyplot as plt
import os,xlrd
import numpy as np

#directory & column
data = xlrd.open_workbook('C:/Users/Qukoyk/Desktop/201611-12.xlsx')
table = data.sheet_by_index(0) #sheet of data
ncols = table.ncols #get the number of columns

#number of subplot
z = 1

#
for i in range(ncols): #circulation of bar plot
    x = table.col_values(i) #data in columns
    y = np.arange(len(x)) #set groups as lenth of x-tick
    plt.subplot(ncols,1,z) #draw subplot(all subplot,draw in 1 column,this subplot)
    plt.bar(y,x,color='k') #draw bar plot
    plt.xticks(visible=False) #xticks invisible
    plt.yticks(visible=False) #yticks invisible
    plt.subplots_adjust(hspace=0) #no places between subplots
    plt.ylim(0,50) #set limitation of y-tick to 50
    z = z+1 #number of subplot +1  &  into the next circulation

plt.show() #show the actogram, takes about 1 minute under Raspberry Pi 3B
