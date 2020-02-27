import math
import numpy


def hitungWaktu(kecepatanAwal,gravitasi,sudut):
    waktu = (2*(kecepatanAwal*(numpy.sin(numpy.deg2rad(sudut))))/(-gravitasi))
    return waktu

def hitungParabola(time,timeStep,kecepatanAwal,gravitasi,VOX,VOY):
    posisiSumbuX = 0 
    posisiSumbuY = 0
    nilaiVY = VOY+(gravitasi*timeStep)
    print("T,                 X(t),                  Y(t)")
    print("0.0                  0                      0 ")
    for i in numpy.arange(0,time,timeStep):
        posisiSumbuX += (VOX*timeStep)
        posisiSumbuY += (nilaiVY*timeStep)
        nilaiVY += gravitasi*timeStep
        print(round(i+timeStep,2),"       ",posisiSumbuX,"       ",posisiSumbuY)
    pilihan = str(input("Ingin Kembali Ke Awal (Y/N) "))
    if(pilihan == "Y"):
        main()



def main():
    const_gravity = -9.8
    sudut = int(input("Masukkan Nilai Sudut : "))
    timeStep = float(input("Masukkan Nilai TimeStep : "))
    kecepatanAwal = int(input("Masukkan Kecepatan Awal : "))
    nilaiVOX = kecepatanAwal*numpy.cos(numpy.deg2rad(sudut))
    nilaiVOY = kecepatanAwal*numpy.sin(numpy.deg2rad(sudut))
    waktu = hitungWaktu(kecepatanAwal,const_gravity,sudut)
    hitungParabola(waktu,timeStep,kecepatanAwal,const_gravity,nilaiVOX,nilaiVOY)


if __name__ == '__main__':
    main()