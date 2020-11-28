try :    #untuk menandadi blok yang akan dicek exception
    file = input("Masukkan Nama File(contoh D:/namafile.txt) : " ) #buat masukkin  lokasi dan nama file
    file1 = open (file, "r") #untuk membuka file
    print("Isi file", file, "adalah : ")
    print(file1.read()) #untuk menampilkan file yg telah dibuka
    
except FileNotFoundError: #exception handling jika file tidak ditemukan/nama salah
    print("Maaf! File tidak ditemukan")
except UnicodeDecodeError: #exception handling jika file tidak berformat .txt
    print("Maaf, Tidak bisa membuka ! Format file harus .txt")

