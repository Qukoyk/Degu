import matplotlib.pyplot as plt
import matplotlib.spines as spines
import os,xlrd
import numpy as np


data = xlrd.open_workbook('C:/Users/Qukoyk/Desktop/201611-12.xlsx')
table = data.sheet_by_index(0)
ncols = table.ncols


z = 1

for i in range(ncols):
    x = table.col_values(i)
    y = np.arange(len(x))
    plt.subplot(ncols,1,z)
    plt.bar(y,x,color='k')
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    plt.subplots_adjust(hspace=0)
    # plt.subplots_adjust(left=0.30,right=0.7,hspace=0)
    plt.ylim(0,50)
    z = z+1

plt.show()
