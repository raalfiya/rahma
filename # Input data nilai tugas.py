ulang = 2
data_list = []
for i in range(ulang):
    print("Data ke - " + str(i + 1))
    nama = input("Masukkan NIM Anda: ")
    uts = int(input("Masukkan Nilai UTS Anda: "))
    uas = int(input("Masukkan Nilai UAS: "))
    tugas1 = int(input("Masukkan nilai tugas 1: "))
    tugas2 = int(input("Masukkan nilai tugas 2: "))
    absen = int(input("masukkan absen anda: "))

    # Rata-rata nilai tugas, 
    jml_tugas = (tugas1 + tugas2)/2
    jml= nilai_akhir = (uts * 0.3) + (uas * 0.4) + (jml_tugas * 0.2) + (nilai_absen * 0.1)

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
    print("NIM anda %s, nilai UTS anda %i, nilai UAS anda %i, nilai tugas 1 %i, nilai tugas 2 %i, nilai absen %i, nilai akhir %i, , grade %s" % (nama, uts, uas, tugas1, tugas2, nilai_absen, nilai_akhir, grade))
    print("-------------------------------------\n")
