import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_kotak1 = pd.read_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_kotak1.csv', index_col = 0)
data_kotak1 = np.array(data_kotak1)
data_kotak2 = pd.read_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_kotak2.csv', index_col = 0)
data_kotak2 = np.array(data_kotak2)
data_kotak3 = pd.read_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_kotak3.csv', index_col = 0)
data_kotak3 = np.array(data_kotak3)
data_kotak4 = pd.read_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_kotak4.csv', index_col = 0)
data_kotak4 = np.array(data_kotak4)
data_kotak5 = pd.read_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_kotak5.csv', index_col = 0)
data_kotak5 = np.array(data_kotak5)
data_kotak6 = pd.read_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_kotak6.csv', index_col = 0)
data_kotak6 = np.array(data_kotak6)

x = np.linspace(0, 41, 41)
plt.plot(x, data_kotak1, label = 'fase = 5')
plt.plot(x, data_kotak2, label = 'fase = 8')
plt.plot(x, data_kotak3, label = 'fase = 10')
plt.plot(x, data_kotak4, label = 'fase = 16')
plt.plot(x, data_kotak5, label = 'fase = 25')
plt.plot(x, data_kotak6, label = 'fase = 40')

plt.xlabel("X")
plt.ylabel("Energi")
plt.title("Perubahan Energi Gelombang Kotak")
plt.text(0, 0, r'$\sigma=0.9,\ \sigma_m=0.9, \mu=\epsilon=1$')
plt.legend()
plt.show()
