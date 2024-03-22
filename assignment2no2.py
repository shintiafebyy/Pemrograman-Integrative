jumlah_angka = 0

while True:
    angka = int(input("Masukkan angka (sampai -1 untuk berhenti): "))
    # memberhentikan penjumlahan apabila angka -1 dimasukkan
    if angka == -1:
        break
    
    # Add the entered number to the sum
    jumlah_angka += angka

# menampilkan hasil penjumlahan
print(f"Jumlah semua angka yang dimasukkan adalah: {jumlah_angka:.2f}")