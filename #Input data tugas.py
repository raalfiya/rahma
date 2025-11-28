ulang = 2
data_list = []
for i in range(ulang):
    print("Data ke - " + str(i + 1))
    nama = input("Masukkan NIM Anda: ")
    uts = int(input("Masukkan Nilai UTS Anda: "))
    uas = int(input("Masukkan Nilai UAS: "))
    tugas1 = int(input("Masukkan nilai tugas 1: "))
    tugas2 = int(input("Masukkan nilai tugas 2: "))
    absen =int(input("masukkan nilai absen"))

    # Rata-rata nilai tugas
    jml_tugas = (tugas1 + tugas2 /2 )
    jml= nilai_akhir = (uts * 0.30) + (uas * 0.40) + (jml_tugas * 0.30)

    # Menentukan grade berdasarkan nilai akhir
    if nilai_akhir >= 80:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"

    # Menampilkan hasil
    print("NIM anda %s, nilai UTS anda %i, nilai UAS anda %i, nilai tugas 1 %i, nilai tugas 2 %i, nilai_absen%i, nilai akhir %.2f, grade %s" % (nama, uts, uas, tugas1, tugas2, nilai_akhir, grade))
    print("-------------------------------------\n")

    ulang=2
list_nim = []
list_uts = []
list_uas = []
list_total = []
for i in range(ulang):
 print ("data Ke - " + str(i+1))
 list_nim.append(input("Masukkan Nim anda : "))
 list_uts.append(int(input("Masukkan Nilai UTS anda :")))
 list_uas.append(int(input("Masukkan Nilai UAS : ")))


 #proses
for i in range(ulang):
 list_total.append((list_uas[i] + list_uts[i]) / 2)
#Cetak
print("========================================================")
print("Nim Nilai Uts Nilai UAS Total")
print("========================================================")
for i in range(ulang):
 print ("%s \t %i \t\t %i \t\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
print("========================================================")

