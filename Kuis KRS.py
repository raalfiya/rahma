print("---------------------------------------------------")
print("       UNIVERSITAS BINA SARANA INFORMATIKA         ")
print("            FAKULTAS TEKNIK INFORMATIKA            ")
print("       PROGRAM STUDI S1 TEKNOLOGI INFORMASI        ")
print("---------------------------------------------------")

print("KARTU RENCANA STUDI (KRS)")
print("SEMESTER : Ganjil 2024/2025")

print("---------------------------------------------------")
print("IDENTITAS MAHASISWA")
print("---------------------------------------------------")
nim=input("NIM (Nomor Induk Mahasiswa) : ")
nama=input("Nama Mahasiswa             : ")
banyak_matkul=int(input("Jumlah Mata Kuliah yang diambil : "))
kelas =input("Kelas A/B/C              : ")   
print("---------------------------------------------------")

print("---------------------------------------------------")
print("DAFTAR MATA KULIAH TERSEDIA")
print("---------------------------------------------------")
print("Kode      Mata Kuliah             SKS   Keterangan ")
print("153       PENGANTAR TEKNOLOGI      3     Wajib")
print("712       ENTREPRENEURSHIP         3     Wajib") 
print("101       PENDIDIKAN PANCASILA     2     Wajib")
print("894       DASAR PEMROGRAMAN        4     Wajib")
print("104       BAHASA INGGRIS I         2     Pilihan")
print("207       LOGIKA DAN ALGORITMA     4     Wajib")
print("---------------------------------------------------")

list
kode_list=[]
matkul_list=[]
sks_list=[]
keterangan_list=[]
total_sks_list=[]
kelas_list=[]

#input data
for i in range (banyak_matkul) :
    print(f"\nMasukkan data matkul ke-{i+1}:")
    kode=input("Kode Mata Kuliah: ")
    matkul=input("Nama Mata Kuliah: ")
    sks=int(input("Jumlah SKS: "))
    keterangan=input("Keterangan (Wajib/ Pilihan): ")

    if kode == "153":
        nama_mata_kuliah="PENGANTAR TEKNOLOGI INFORMASI DAN KOMUNIKASI"
        sks=3
        keterangan="Wajib"
    elif kode == "712":
        nama_mata_kuliah="ENTREPRENEURSHIP"
        sks=3
        keterangan="Wajib"
    elif kode == "101":
        nama_mata_kuliah="PENDIDIKAN PANCASILA"
        sks=2
        keterangan="Wajib"
    elif kode == "894":
        nama_mata_kuliah="DASAR PEMROGRAMAN"
        sks=4
        keterangan="Wajib"
    elif kode == "104":
        nama_mata_kuliah="BAHASA INGGRIS I"
        sks=2
        keterangan="Pilihan"
    elif kode == "207":
        nama_mata_kuliah="LOGIKA DAN ALGORITMA"
        sks=4
        keterangan="Wajib"
    else:
        nama_mata_kuliah="Kode Mata Kuliah Tidak Dikenal"
        
    kode_list.append (kode)
    matkul_list.append (nama_mata_kuliah)
    sks_list.append (sks)
    keterangan_list.append (keterangan)
    
    total_sks=0
#cetak KRS

print("\n-------------------- KARTU RENCANA STUDI -----------------------")
print("(Mata Kuliah yang akan diambil pada semester ini)")
print("----------------------------------------------------------------")
print("Kode     Mata Kuliah                  SKS   Kelas Keterangan    ")
for i in range(banyak_matkul):
    print(f"{kode_list[i]:<8} {matkul_list[i]:<35} {sks_list[i]:<5} {keterangan_list[i]:<10}")
    total_sks += sks_list[i] 
print("----------------------------------------------------------------")
print(f"Total SKS yang diambil: {total_sks}") 
print("----------------------------------------------------------------")


