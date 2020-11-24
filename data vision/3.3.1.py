import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
filename = "flowingdata_subscribers.csv"
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num!=1:
            datay.append(datarow[1])
xa = list(range(1,len(datay)+1))
plt.scatter(xa,datay,s=50,c='r',marker='o',alpha=0.5)
plt.show()
#plt.ylim((0, 27500))
#plt.yticks(np.arange(10000, 27500, 2500))
