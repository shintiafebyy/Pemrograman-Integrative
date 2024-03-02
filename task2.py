angka = int(input("Masukkan angka: "))

# membagi angka bulat dengan 3
hasil = angka/3

#menampilkan hasil
if int(hasil):
    print("Hasilnya adalah: {:.1f}".format(hasil))
else:
    print("Hasilnya adalah: {:.3f}".format(hasil))
    