#membuka dan mau membaca file d:/data.txt
file = open("C:/data.txt","r")

#baca baris pertama dari file
#simpan ke dalam variabel bil1 sebagai integer
bil1 = int(file.readline())

#baca baris kedua dari file
#simpan kedalam variabel bil1 sbg integer
bil2 = int(file.readline())

#hitung dan tampilkan hasil bagi
hasil = bil1/bil2
print(bil1,"dibagi", bil2,"sama dengan",hasil)
