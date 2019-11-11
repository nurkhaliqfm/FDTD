import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

epsilon = 1
mu = 1
del_t = 1
del_x = 1
w = np.pi
Nx = 100
Nt = 100
C = 1
G = 0.9
R = 0.9
L = 1

n_Ex = []
n_Hy = []

Ex = np.zeros((Nx, Nt))
Hy = np.zeros((Nx, Nt))

class BentukInput:
    def Sinusoidal(fase):
        for j in range(Nt):
            if j % 2 == 0:
                Ex[j, 0] = np.sin((w/fase) * (j + 1))
            else:
                Hy[j, 1] = np.sin((w/fase) * (j))

    def Tangga(fase):
        awal = 0
        akhir = fase * 2
        akhir1 = akhir + akhir
        akhir2 = akhir1 + akhir
        akhir3 = akhir2 + akhir
        for j in range(Nt):
            if j % 2 == 0:
                if j > awal and j <= akhir :
                    Ex_ = -1
                    Ex[j, 0] = Ex_
                elif j > akhir and j <= akhir1:
                    Ex_ = 1
                    Ex[j, 0] = Ex_
                elif j > akhir1 and j <= akhir2:
                    Ex_ = -1
                    Ex[j, 0] = Ex_
                elif j > akhir2 and j <= akhir3:
                    Ex_ = 1
                    Ex[j, 0] = Ex_
                else:
                    Ex_ = 0
                    Ex[j, 0] = Ex_
            else:
                if j > awal and j <= akhir:
                    Hy_ = 1
                    Hy[j, 1] = Hy_
                else:
                    Hy_ = 0
                    Hy[j, 1] = Hy_

def Input_Awal():
    for i in range(Nx):
        if i % 2 == 0:
            Ex_ = 0
            Ex[0, i] = Ex_
        else:
            Hy_ =  0
            Hy[1, i] = Hy_

#    BentukInput.Sinusoidal(5)
    BentukInput.Tangga(10)
def FDTD():
    for j in range(2, Nt):
        if j % 2 == 0:
            for i in range(2, Nx - 1):
                if i % 2 == 0:
                    if i > 33 and i <= 66:
                        dV_ = Ex[j - 2, i] * (((2 * C) - (G * del_t)) / ((2 * C) + (G * del_t))) - (Hy[j - 1, i + 1] - Hy[j - 1, i - 1]) * ((2 * del_t) / (((2 * C) + (G * del_t)) * del_x))
                        Ex[j, i] = dV_
                    else:
                        Ex_ = Ex[j - 2, i] - (del_t / (epsilon * del_x)) * (Hy[j - 1, i + 1] - Hy[j - 1, i - 1])
                        Ex[j, i] = Ex_
        else:
            for i in range(3, Nx - 1):
                if i % 2 == 1:
                    if i > 33 and i <= 66:
                        dI_ = Hy[j - 2, i] *  (((2 * L) - (R * del_t)) / ((2 * L) + (R * del_t))) - (Ex[j - 1, i + 1] - Ex[j - 1, i - 1]) * ((2 * del_t) / (((2 * L) + (R * del_t)) * del_x))
                        Hy[j, i] = dI_
                    else:
                        Hy_ = Hy[j - 2, i] - (del_t / (mu * del_x)) * (Ex[j - 1, i + 1] - Ex[j - 1, i - 1])
                        Hy[j, i] = Hy_

def HapusNolMatriks():
    for j in range(Nt):
        if j % 2 == 0:
            row = []
            for i in range(Nx):
                if i % 2 == 0:
                    row.append(Ex[j, i])
            n_Ex.append(row)
        else:
            row = []
            for i in range(Nx):
                if i % 2 == 1:
                    row.append(Hy[j, i])
            n_Hy.append(row)


Input_Awal()
FDTD()
HapusNolMatriks()

data_Ex = pd.DataFrame(n_Ex)
data_Hy = pd.DataFrame(n_Hy)
data_Hy.to_csv('/home/nurkhaliq/Documents/ATOM/FDTD/fdtd_1D_Hy--nn.csv')
data_Ex.to_csv('/home/nurkhaliq/Documents/ATOM/FDTD/fdtd_1D_Ex--nn.csv')

class Analisis:
    def Plot():
        dataEx = np.array(data_Ex)
        dataEx = np.transpose(dataEx)
        data_plot1 = dataEx[0]
        for i in range(1,49):
            plot1 = dataEx[i,i:]
            data_plot1 = np.append(data_plot1, plot1)

        x = np.linspace(0, 1274, 1274)
        plt.plot(x, data_plot1)
        plt.show()

    def Energi():
        Energi = data_Ex**2 + data_Hy**2
        Energi = np.array(Energi)
        Sigma_Energi = []
        k = 0
        for i in range(41):
            Energi_ = 0
            for j in range(10):
                Energi_ += Energi[j+k][i]
            k += 1
            Sigma_Energi.append(Energi_)

        Sigma_Energi = pd.DataFrame(Sigma_Energi)

        #data_sinus6 = pd.DataFrame(Sigma_Energi)
        #data_sinus6.to_csv('/home/nurkhaliq/Documents/ATOM/FDTD/data_sinus6.csv')
        return Sigma_Energi

    def Transmitansi():
        hasil = (Analisis.Energi()[0][33]/Analisis.Energi()[0][1]) * 100
        print("Transmitansi = {}".format(hasil))
Analisis.Transmitansi()
Analisis.Plot()
Analisis.Energi()
