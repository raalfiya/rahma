# Data Daftar belanja

print("                      MR.DIY                  ")
print("-----------------------------------------------------")
print("Kode  Nama Barang   Harga")
print("9069104 BAKING BRUSH 360 15,500")
print("9076652 PAINT BRUSH 360 3,500")
print("-----------------------------------------------------")

#Input data pembelian
Hicard=input("Masukkan nomor HICARD anda: ")
tanggal_pembelian=input("Masukkan tanggal pembelian (DD/MM/YYYY): ")
banyak_barang = int(input("Masukkan jumlah jenis barang yang dibeli: "))

#Inisialisasi list
kode_barang_list=[]
nama_barang_list=[]
jumlah_barang_list=[]
harga_list=[]

#Input data pembelian
for i in range(banyak_barang):
    print(f"\nMasukkan data barang ke-{i+1}:")
    kode_input=input("Kode Barang: ")
    jumlah_input=int(input("Jumlah Barang: "))

    # Mencari data barang berdasarkan kode
    nama_item = "Barang tidak ditemukan"
    harga_item = 0

    if kode_input == "9069104":
        nama_item ="BAKING BRUSH 360"
        harga_item = 15000
    elif kode_input == "9076652":
        nama_item ="PAINT BRUSH 360"
        harga_item = 3500

    kode_barang_list.append(kode_input)
    nama_barang_list.append(nama_item)
    jumlah_barang_list.append(jumlah_input)
    harga_list.append(harga_item)


# CETAK STRUK PEMBELIAN
print("\n                  MR.DIY                   ")
print("=============================================")
print("No Kode Barang    Nama Barang      Harga      Banyak   Jumlah Harga")
print("=============================================")

total_belanja= 0
for i in range(banyak_barang):
    jumlah_harga_item = harga_list[i] * jumlah_barang_list[i]
    print(f"{i+1:<4} {kode_barang_list[i]:<13} {nama_barang_list[i]:<16} {harga_list[i]:<11,.0f} {jumlah_barang_list[i]:<8} {jumlah_harga_item:<12,.0f}")
    total_belanja += jumlah_harga_item

print("==============================================")

#HITUNG PAJAK DAN TOTAL
pajak=total_belanja * 0.1
total_bayar = total_belanja + pajak

print(f"Total Belanja     : Rp {total_belanja:,.0f}")
print(f"Pajak (10%)       : Rp {pajak:,.0f}")
print(f"Total Bayar       : Rp {total_bayar:,.0f}")

# Input pembayaran
tunai = float(input("\nMasukkan jumlah tunai: Rp "))
kembali = tunai - total_bayar

# CETAK KEMBALIAN
print("================ STRUK PEMBELIAN ================")
print(f"Jumlah items: {banyak_barang}")
print(f"TOTAL: Rp {total_bayar:,.0f}")
print(f"Tunai: Rp {tunai:,.0f}")
print(f"Kembali: Rp {kembali:,.0f}")
        
