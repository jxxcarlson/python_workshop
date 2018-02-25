from matplotlib import pyplot as plt
import sys
from get_data import get_data, first, second, to_float

dataList = get_data(sys.argv[1])

years = first(dataList)
temps = to_float(second(dataList))

plt.plot(years, temps, color='red', marker='o', linestyle='solid')
plt.title("Temperature anomaly")
plt.ylabel("Degrees C")

plt.show()
