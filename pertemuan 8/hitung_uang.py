jumlah_set = int(input("masukkan jumlah set transaksi:"))

for i in range(jumlah_set):
    print(f"\nset transaksi ke-{i+1}")

    target_uang = int(input("masukkan target jumlah uang: "))

    jumlah_100 = int(input("masukkan jumlah lembar/koin uang rp.100: "))
    jumlah_500 = int(input("masukkan jumlah lembar/koin uang rp.500: "))
    jumlah_1000 = int(input("masukkan jumlah lembar/koin uang rp.1000: "))
    jumlah_5000 = int(input("masukkan jumlah lembar/koin uang rp.5000: "))
    jumlah_10000 = int(input("masukkan jumlah lembar/koin uang rp.10000: "))
    jumlah_20000 = int(input("masukkan jumlah lembar/koin uang rp.20000: "))
    jumlah_50000 = int(input("masukkan jumlah lembar/koin uang rp.50000: "))
    jumlah_100000 = int(input("masukkan jumlah lembar/koin uang rp.100000: "))

    total_uang = (jumlah_100*100)+(jumlah_500*500)+(jumlah_1000*1000)+(jumlah_5000*5000)+(jumlah_10000*10000)+(jumlah_20000*20000)+(jumlah_50000*50000)+(jumlah_100000*100000)

    if total_uang > target_uang:
        print(f"target jumlah uang Rp.{target_uang} telah tercapai dengan total uang sebesar Rp.{total_uang}")
    elif total_uang < target_uang:
        print(f"target jumlah uang Rp.{target_uang} Bbelum tercapai dengan total uang sebesar Rp.{total_uang}")
    else:
        print(f"target jumlah uang Rp.{target_uang} sesuai dengan total uang sebesar Rp.{total_uang}")
