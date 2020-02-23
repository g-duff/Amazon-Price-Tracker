from matplotlib import pyplot as plt
import numpy as np

item_numbers = np.loadtxt("Item Numbers.txt", dtype=int)
year, month, day, hour, minute, second, *prices = np.loadtxt('Price Data.txt', unpack=True)

#here we remake the datetime because I don't know how else to do it
times = [(str(y)+","+str(m)+","+str(d)+":"+str(h)+":"+str(mi)) for y, m ,d ,h, mi in (zip(year, month, day, hour, minute))]

for item, price in zip(item_numbers, prices):
    plt.plot(times, price, label=item)
plt.xticks(rotation = 90)
plt.legend()
plt.tight_layout()
plt.show()


