from matplotlib import pyplot as plt
import sys
from get_data import *

dataList = get_data(sys.argv[1])

years = first(dataList)
anomalies = to_float(second(dataList))

window = 10
years = drop_window(years, window)
anomalies1 = drop_window(anomalies, window)
anomalies2 = smooth(anomalies,window)

print [len(years), len(anomalies1), len(anomalies2)]
plt.plot(years, anomalies1, color='red', linestyle='solid')
plt.plot(years, anomalies2, color='blue', linestyle='solid')
plt.title("Temperature anomaly")
plt.ylabel("Degrees C")

plt.show()
