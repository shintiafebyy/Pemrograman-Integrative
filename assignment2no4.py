grades = []
grade_sum = 0
count = 0

# Membaca nilai-nilai hingga -1 dimasukkan
while True:
    grade = input("Masukkan nilai (masukkan -1 untuk mengakhiri): ")
    if grade == "-1":
        break
    grades.append(int(grade))
    grade_sum += int(grade)
    count += 1

# Menghitung rata-rata
average = int(grade_sum / count) if count > 0 else 0

# Mencetak rata-rata
print("Rata-rata:", average)

# Mencetak nilai-nilai yang dimasukkan
for grade in grades:
    print(grade)