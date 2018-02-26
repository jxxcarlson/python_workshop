from matplotlib import pyplot as plt
import sys
from get_data import *

dataList = get_data(sys.argv[1])

years = first(dataList)
anomalies = to_float(second(dataList))

plt.plot(years, anomalies, color='red', marker='', linestyle='solid')
plt.title("Temperature anomaly")
plt.ylabel("Degrees C")

plt.show()
