import csv
import matplotlib.pyplot as plt
filename = "world-population.csv"
datax=[]
datay=[]
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num!=1:
            print(reader.line_num,datarow)
            datax.append(datarow[0])
            datay.append(datarow[1])
plt.plot(datax,datay)
plt.show()