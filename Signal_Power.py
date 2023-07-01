import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

C = True
D = True
while D:
    T = float(input("¿Qué periodo en segundos será su T?, inserte un valor mayor o igual a 1" + "\u03BCs" + " o menor o igual a 1s: "))
    if T > 1:
        print("Inserte un valor menor o igual a 1s por favor")
        D= True
    elif T < 0.000001:
        print("Inserte un valor mayor o igual a 1" + "\u03BCs" + " por favor")
    elif T < 0:
        print("Inserte un valor positivo por favor")
        D = True
    else:
        D=False
0.001
while C:
    A = float(input("¿Cuál será su voltaje en Volts?, inserte un valor entre 5V y 10V: " ))
    if A>=5 and A<=10:
        C= False
    else:
        print("Inserte un valor entre 5v y 10V por favor")
        C=True
n_final = int(input("¿Cuántos armónicos quiere graficar?: "))

def fourier(t,n):
    f = (2*A/((2*n-1)*np.pi)*np.sin(2*(2*n-1)*np.pi*t/T))
    return f

t = np.linspace(0+(T/200),T-(T/(200)),10000)
f = 0
n= 1
m = 0

if n_final <= 3:
    m = 1
elif n_final > 3 and n_final <= 10:
    m = 2
elif n_final > 10 and n_final <= 40:
    m = 3
elif n_final > 40 and n_final <= 70:
    m = 4
elif n_final > 70 and n_final <= 100:
    m = 5
elif n_final > 100 and n_final <= 120:
    m = 6
elif n_final > 120 and n_final <= 150:
    m = 7
elif n_final > 150 and n_final <= 250:
    m = 8
else:
    m = 12

Delta_T = str("{0:.8f}".format((T*(2*m-1))/(2*n_final)))

while n<=n_final:
    f += fourier(t,n)
    f_final = f + (A/2)
    n += 1

plt.plot(t, f_final, color="m" ,label="Fourier")
plt.axvline((T/2)-((T*(2*m-1))/(4*n_final)), color='g',ls="dotted")
plt.axvline((T/2)+((T*(2*m-1))/(4*n_final)), color='r',ls="dotted")
plt.hlines(y=(A/2), xmin=(T/2)-((T*(2*m-1))/(4*n_final)), xmax=(T/2)+((T*(2*m-1))/(4*n_final)), color="b", label=r"$\Delta $T= " + Delta_T + "s")
plt.title("Serie de Fourier - Tarea#1 Electrónica")
plt.xlabel("Periodo [s]")
plt.ylabel("Voltaje [V]")
plt.legend(loc="upper right")
plt.show()



