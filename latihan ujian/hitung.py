jumlah_karyawan = int(input("masukkan jumlah_karyawan"))

for i in range(jumlah_karyawan):
    jam_kerja = int(input("masukkan jumlaj jam_kerja: "))

    tarif_normal = 50000
    tarif_lembur = 75000

    if jam_kerja > 40:
        jam_lembur = jam_kerja - 40
        gaji_pokok = (tarif_normal*40) + (tarif_lembur*jam_lembur)

    else:
        gaji_pokok = tarif_normal*40

    print(f"gaji karyawan yang diterima{gaji_pokok} dengan jam kerja{jam_kerja}")