ulang=2
data_list= []
for i in range(ulang):
    print ("data ke - " + str (i+1))
    nama= input ("masukkan Nim anda : ")
    uts= int (input("masukkan Nilai UTS anda :"))
    uas= int (input("masukkan Nilai UAS : "))

    jml=(uts+uas)/2
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

print ("Nim anda adalah %s nilai UTS anda %i nilai UTS %i, jumlah nilai %i grade %s" % (nama,uts,uas,jml,grade))
print ("---------------------------------\n")



