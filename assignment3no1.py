# Membaca angka-angka dari file teks indata.txt
with open("indata.txt", "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

# Menghitung jumlah dari angka-angka tersebut
total = sum(numbers)

# Mencetak hasil dengan pemisah koma dan dua digit di belakang koma
print("{:,.2f}".format(total))
