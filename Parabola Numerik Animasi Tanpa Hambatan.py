import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpmath
import numpy

fig = plt.figure()
ax = plt.axes(xlim=(0,250),ylim=(0,50))
line, = ax.plot([], [])

posisiSumbuX = 0
posisiSumbuY = 0
const_gravity = -9.8
kecepatanAwal = int(input("Masukkan Kecepatan Awal : "))
timeStep = float(input("Masukkan TimeStep : "))
iterasi = 0
sudut = int(input("Masukkan Sudut yang dibutuhkan : "))
nilaiSin = numpy.sin(numpy.deg2rad(sudut))
nilaiCos = numpy.cos(numpy.deg2rad(sudut))
time = 0

nilaiVx = kecepatanAwal*nilaiCos
nilaiVy = kecepatanAwal*nilaiSin

listSumbuX = []
listSumbuY = []

while True :
        time += timeStep
        posisiSumbuY += nilaiVy*timeStep
        posisiSumbuX += nilaiVx*timeStep
        nilaiVy += const_gravity*timeStep
        print(time)
        print(posisiSumbuX)
        print(posisiSumbuY)
        listSumbuX.append(posisiSumbuX)
        listSumbuY.append(posisiSumbuY)
        if(posisiSumbuY <= 0):
            break

def init():
    line.set_data([], [])
    return line,

xdata,ydata = [], []

def animate(i):
    x = listSumbuX[i]
    y = listSumbuY[i]

    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata) 
    return line,

plt.title("Simulasi Gerak Parabola")

anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=1000, interval=10, blit=True)
plt.show()
