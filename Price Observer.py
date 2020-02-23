from matplotlib import pyplot as plt
import numpy as np

item_numbers = np.loadtxt("Item Numbers.txt", dtype=int)
year, month, day, hour, minute, second, *prices = np.loadtxt('Price Data.txt', unpack=True)

# Format dates and times to ISO 8601 
dates = (f'{y:.0f}-{m:02.0f}-{d:.0f}' for y, m, d in zip(year, month, day))
times = (f'{h:02.0f}:{m:02.0f}:{s:02.0f}' for h, m, s in zip(hour, minute, second))

# Make use of numpy datetime64 datatype
datetimes = [np.datetime64(f'{d}T{t}') for d, t in zip(dates, times)]

for item, price in zip(item_numbers, prices):
    plt.plot(datetimes, price, label=item)
plt.xticks(rotation = 90)
plt.legend()
plt.tight_layout()
plt.show()
