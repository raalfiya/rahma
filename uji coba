def garis():
    print("=" * 70 )
garis()
print("                  UNIVERSITAS BINA SARANA INFORMATIKA               ")
print("                     FAKULTAS TEKNIK INFORMATIKA                   ")
print("                PROGRAM STUDI S1 TEKNOLOGI INFORMASI               ")
garis()
print("                         KARTU RENCANA STUDI (KRS)                 ")
print("                       SEMESTER : Ganjil 2024/2025                 ")
garis()

print("|                        IDENTITAS MAHASISWA                       |")
def garis_satu(): # Define garis_satu once
    print("-" * 70 )
garis_satu()
nim = input("NIM (Nomor Induk Mahasiswa) : ")
nama = input("Nama Mahasiswa              : ")
garis()

# Daftar mata kuliah
daftar_matkul = {
    "153": {"nama": "PENGANTAR TEKNOLOGI INFORMASI DAN KOMUNIKASI", "sks": 3, "keterangan": "Wajib"},
    "712": {"nama": "ENTREPRENEURSHIP", "sks": 3, "keterangan": "Wajib"},
    "101": {"nama": "PENDIDIKAN PANCASILA", "sks": 2, "keterangan": "Wajib"},
    "894": {"nama": "DASAR PEMROGRAMAN", "sks": 4, "keterangan": "Wajib"},
    "104": {"nama": "BAHASA INGGRIS I", "sks": 2, "keterangan": "Pilihan"},
    "207": {"nama": "LOGIKA DAN ALGORITMA", "sks": 4, "keterangan": "Wajib"}
}

print("         Daftar Data Kuliah Tersedia         ")
garis_satu()
print("Kode      Mata Kuliah                                SKS   Keterangan ")
for kode, matkul_info in daftar_matkul.items():
    print(f"{kode:<8} {matkul_info['nama']:<36} {matkul_info['sks']:<5} {matkul_info['keterangan']:<10}")
garis()

banyak_matkul = int(input("Masukkan banyak mata kuliah yang akan diambil : ")) # Added this line

kode_list=[]
matkul_list=[]
sks_list=[]
keterangan_list=[]
kelas_list=[]

#input data
for i in range (banyak_matkul) :
    print(f"\nMasukkan data matkul ke-{i+1}:")
    kode = input("Kode Mata Kuliah (153/712/101/894/104/207): ")
    kelas = input("Kelas (A/B/C): ")

    if kode in daftar_matkul:
        matkul_info = daftar_matkul[kode]
        nama_mata_kuliah = matkul_info["nama"]
        sks = matkul_info["sks"]
        keterangan = matkul_info["keterangan"]
    else:
        nama_mata_kuliah = "Kode Mata Kuliah Tidak Dikenal"
        sks = 0
        keterangan = "Tidak Dikenal"

    kode_list.append (kode)
    matkul_list.append (nama_mata_kuliah)
    sks_list.append (sks)
    keterangan_list.append (keterangan)
    kelas_list.append(kelas)

total_sks=0
#cetak KRS

print("\n-------------------- KARTU RENCANA STUDI -----------------------")
print("(Mata Kuliah yang akan diambil pada semester ini)")
garis_satu()
print("Kode     Mata Kuliah                                SKS   Kelas Keterangan    ")
for i in range(banyak_matkul):
    print(f"{kode_list[i]:<8} {matkul_list[i]:<36} {sks_list[i]:<5} {kelas_list[i]:<5} {keterangan_list[i]:<10}")
    total_sks += sks_list[i]
garis_satu()
print(f"Total SKS yang diambil: {total_sks}")
garis_satu()

print("\n======================== DATA MAHASISWA ============================")
print(f"NIM             : {nim}")
print(f"Nama Mahasiswa  : {nama}")
print("Program Studi   : S1 Teknologi Informasi")
print("Dosen Wali      : Dr. Andi Suhendra, M.Kom.")
print("====================================================================")
print("KRS berhasil dicetak. Selamat\u00a0belajar!")