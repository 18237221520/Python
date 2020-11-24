import ggplot as gp
import pandas as pd
crime = pd.read_csv("crimeRatesByState2005.csv")
crime2 = crime[crime.state != "United States"]
crime2 = crime2[crime2.state != "District of Columbia"]
plots = gp.ggplot(gp.aes(x='murder', y='burglary'), data=crime2)
point = gp.geom_point()
smooth = gp.stat_smooth(method='loess', color='red')
print(plots + point + smooth)
