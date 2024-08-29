import time

a = int(input("masukan jumlah siswa: "))

for i in range (a):
    nama = (input("masukan nama siswa / siswi: "))
    tugas1 = float(input("masukkan nilai tugas ke 1"))
    tugas2 = float(input("masukkan nilai tugas ke 2"))
    tugas3 = float(input("masukkan nilai tugas ke 3"))

b = 3

all = tugas1 + tugas2 + tugas3

avv = all // b

if  avv >= 70:
    print("selamat kamu lulus")
elif avv >= 50 and 69:
    print("anda harus perbaikan")    
elif avv <50:
    print("anda tidak lulus")    
else:
    print("anda tidak lulus, jangan lupa belajar lagi ya") 
    print(selamat",nama,"nilai rata rata kamu = ", avv, semangat belajarnya ya")
      