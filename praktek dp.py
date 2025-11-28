#variable yg berulang menggunakan List/matriks 
list_nim = [] 
list_uts = [] 
list_uas = [] 
list_tugas1 = [] 
list_tugas2 = []
list_nilai_absen = []
list_jml = []
list_grade = []

ulang = 2

# input data
for i in range(ulang):
    print("Data ke -", i + 1)
    list_nim.append(input("Masukkan NIM anda : "))
    list_uts.append(int(input("Masukkan Nilai UTS anda : ")))
    list_uas.append(int(input("Masukkan Nilai UAS anda : ")))
    list_tugas1.append(int(input("Masukkan Nilai Tugas 1 : ")))
    list_tugas2.append(int(input("Masukkan Nilai Tugas 2 : ")))
    list_nilai_absen.append(int(input("Masukkan Nilai Absen anda : ")))
    print("-------------------------------------")

# proses perhitungan nilai dan grade
for i in range(ulang):
    jml_tugas = (list_tugas1[i] + list_tugas2[i]) / 2
    jml = (list_uts[i] * 0.3) + (list_uas[i] * 0.4) + (jml_tugas * 0.2) + (list_nilai_absen[i] * 0.1)
    list_jml.append(jml)

    if jml >= 80:
        grade = "A"
    elif jml >= 70:
        grade = "B"
    elif jml >= 60:
        grade = "C"
    elif jml >= 50:
        grade = "D"
    else:
        grade = "E"
    list_grade.append(grade)

# cetak hasil
print("\n========================================================")
print("NIM\tUTS\tUAS\tT1\tT2\tAbsen\tNilai Akhir\tGrade")
print("========================================================")

for i in range(ulang):
    print("%s\t%i\t%i\t%i\t%i\t%i\t%i\t\t%s" %
          (list_nim[i], list_uts[i], list_uas[i], list_tugas1[i],
           list_tugas2[i], list_nilai_absen[i], list_jml[i], list_grade[i]))
print("========================================================")