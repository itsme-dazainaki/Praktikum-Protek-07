try : #taruh tuisan try, buat nandain blok yg mau dieksekusi dan dicek exception nanti
    #membuka dan mau membaca file d:/data.txt
    file = open("d:/data.txt","r")

    #baca baris pertama dari file
    #simpan ke dalam variabel bil1 sebagai integer
    bil1 = int(file.readline())

    #baca baris kedua dari file
    #simpan kedalam variabel bil1 sbg integer
    bil2 = int(file.readline())

    #hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1,"dibagi", bil2,"sama dengan",hasil)

except FileNotFoundError : #ini buat nyegah exception file not found(disini karna lokasinya salah)
    print("File tidak ditemukan") #ini pesan buat exception filenotfound

except ZeroDivisionError : # ini buat nyegah exception pembagian dgn 0, karena bil2 disini adalah 0
    print("Tidak boleh pembagian dengan nol") #ini pesan buat pembagian dgn 0 (kalo hasil bisa dirun, nanti muncul ini)
