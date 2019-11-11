import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [5,8,10,16,25,40]
data_sinus = [8.376297318432392e-9, 2.1325615368650518e-9, 1.229454846506604e-9, 5.662450780941043e-10,  1.7635666129969677e-10, 1.0182521630181779e-10]
data_kotak = [1.5723158085147111e-06, 5.922565517250321e-07, 5.086675971969259e-07, 5.086675971969259e-07, 5.086675971969259e-07, 5.086675971969259e-07]
plt.plot(x,data_sinus, label = 'Sinusoidal')
plt.plot(x, data_kotak, label = 'Kotak')
plt.legend()
plt.show()
