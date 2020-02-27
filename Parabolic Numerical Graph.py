import math
import numpy
import matplotlib.pyplot
import mpmath


def hitungWaktu(kecepatanAwal,gravitasi,sudut):
    waktu = (2*(kecepatanAwal*(numpy.sin(numpy.deg2rad(sudut))))/(-gravitasi))
    return waktu

def hitungParabolaX(time,timeStep,kecepatanAwal,gravitasi,VOX):
    posisiSumbuX = 0
    listSumbuX = []
    nilaiXMax = VOX*time
    for i in numpy.arange(0,time,timeStep):
        posisiSumbuX += (VOX*timeStep)
        if(posisiSumbuX > nilaiXMax):
            break
        listSumbuX.append(posisiSumbuX)
    return listSumbuX

def hitungParabolaY(time,timeStep,kecepatanAwal,gravitasi,VOY):
    posisiSumbuY = 0
    listSumbuY = []
    listSumbuY.append(0)
    nilaiVY = VOY+(gravitasi*timeStep)
    for i in numpy.arange(0,time,timeStep):
        posisiSumbuY += (nilaiVY*timeStep)
        nilaiVY += gravitasi*timeStep
        if(posisiSumbuY < 0):
            break
        listSumbuY.append(posisiSumbuY)
    return listSumbuY

def hitungParabolaDrag(time,timeStep,gravitasi,nilaiVO,nilaiD,sudut,massa):
    listSumbuY = []
    listSumbuX = []
    nilaiVx = nilaiVO*numpy.cos(numpy.deg2rad(sudut))
    nilaiVy = nilaiVO*numpy.sin(numpy.deg2rad(sudut))
    posisiSumbuY = nilaiVy*timeStep 
    posisiSumbuX = nilaiVx*timeStep
    listSumbuX.append(posisiSumbuX) 
    listSumbuY.append(posisiSumbuY)
    nilaiV = mpmath.sqrt(mpmath.power(nilaiVx,2) + mpmath.power(nilaiVy,2))
    nilaiAx = -(nilaiD/massa)*nilaiV*nilaiVx 
    nilaiAy = gravitasi-(nilaiD/massa)*nilaiV*nilaiVy 
    for i in numpy.arange(0,time,timeStep):
        nilaiAx = -(nilaiD/massa)*nilaiV*nilaiVx 
        nilaiAy = gravitasi-(nilaiD/massa)*nilaiV*nilaiVy 
        nilaiVx += nilaiAx*timeStep
        nilaiVy += nilaiAy*timeStep
        nilaiV = mpmath.sqrt(mpmath.power(nilaiVx,2) + mpmath.power(nilaiVy,2))
        posisiSumbuY += nilaiVy*timeStep
        posisiSumbuX += nilaiVx*timeStep
        if(posisiSumbuY < 0):
            break
        listSumbuX.append(posisiSumbuX)
        listSumbuY.append(posisiSumbuY)
    tampilGraph(listSumbuX,listSumbuY)

def tampilGraph(listSumbuX,listSumbuY):
    matplotlib.pyplot.plot(listSumbuX,listSumbuY)
    matplotlib.pyplot.show()

def main():
    const_gravity = -9.8
    sudut = int(input("Masukkan Nilai Sudut : "))
    timeStep = float(input("Masukkan Nilai TimeStep : "))
    kecepatanAwal = int(input("Masukkan Kecepatan Awal : "))
    airDrag = float(input("Masukkan Hambatan Angin : "))
    massa = float(input("Masukkan Massa Udara :"))
    nilaiVOX = kecepatanAwal*numpy.cos(numpy.deg2rad(sudut))
    nilaiVOY = kecepatanAwal*numpy.sin(numpy.deg2rad(sudut))
    waktu = hitungWaktu(kecepatanAwal,const_gravity,sudut)
    listSumbuX = hitungParabolaX(waktu,timeStep,kecepatanAwal,const_gravity,nilaiVOX)
    listSumbuY = hitungParabolaY(waktu,timeStep,kecepatanAwal,const_gravity,nilaiVOY)
    hitungParabolaDrag(waktu,timeStep,const_gravity,kecepatanAwal,airDrag,sudut,massa)


if __name__ == '__main__':
    main()