import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
crime = pd.read_csv("crimeRatesByState2005.csv")
print(list(crime.murder))
crime2 = crime[crime.state != "United States"]
crime2 = crime2[crime2.state != "District of Columbia"]
z = list(crime2.population/10000)
colors = np.random.rand(len(list(crime2.murder)))
cm = plt.cm.get_cmap('RdYlBu')
plt.scatter(list(crime2.murder), list(crime2.burglary), s=z, c=z, cmap=cm, linewidth=0.5, alpha=0.5)
plt.xlabel("murder")
plt.ylabel("burglary")
plt.show()
