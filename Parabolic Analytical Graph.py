import math
import numpy
import matplotlib.pyplot


def hitungWaktu(kecepatanAwal,gravitasi,sudut):
    waktu = (2*(kecepatanAwal*(numpy.sin(numpy.deg2rad(sudut))))/(-gravitasi))
    return waktu

def hitungParabolaX(time,timeStep,kecepatanAwal,gravitasi,VOX):
    posisiSumbuX = 0
    listSumbuX = []
    for i in numpy.arange(0,time,timeStep):
        posisiSumbuX = VOX*i
        listSumbuX.append(posisiSumbuX)
    return listSumbuX

def hitungParabolaY(time,timeStep,kecepatanAwal,gravitasi,VOY):
    posisiSumbuY = 0
    listSumbuY = []
    for i in numpy.arange(0,time,timeStep):
        posisiSumbuY += (gravitasi/2)*pow(i,2)+(VOY*i)
        listSumbuY.append(posisiSumbuY)
    return listSumbuY

def tampilGraph(listSumbuX,listSumbuY):
    matplotlib.pyplot.plot(listSumbuX,listSumbuY)
    matplotlib.pyplot.show()

def main():
    const_gravity = -9.8
    sudut = int(input("Masukkan Nilai Sudut : "))
    timeStep = float(input("Masukkan Nilai TimeStep : "))
    kecepatanAwal = int(input("Masukkan Kecepatan Awal : "))
    nilaiVOX = kecepatanAwal*numpy.cos(numpy.deg2rad(sudut))
    nilaiVOY = kecepatanAwal*numpy.sin(numpy.deg2rad(sudut))
    waktu = hitungWaktu(kecepatanAwal,const_gravity,sudut)
    listSumbuX = hitungParabolaX(waktu,timeStep,kecepatanAwal,const_gravity,nilaiVOX)
    listSumbuY = hitungParabolaY(waktu,timeStep,kecepatanAwal,const_gravity,nilaiVOY)
    tampilGraph(listSumbuX,listSumbuY)


if __name__ == '__main__':
    main()