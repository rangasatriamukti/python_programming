jumlah_siswa = int(input("masukkan jumlah siswa"))

for i in range (jumlah_siswa + 1):
    nama = input("masukkan nama anda")
    
    a = int(input("masukkan nilai tugas 1"))
    b = int(input("masukkan nilai tugas 2"))
    c = int(input("masukkan nilai tugas 3"))
    
      
    jumlah = a + b + c
      
    
    rata_rata = jumlah / 3
    
    if rata_rata >= 70:
        print("kamu lulus")
    elif rata_rata >= 50 and rata_rata < 69:
        print("perbaikan")
    else rata_rata < 50:
        print("tidak lulus")