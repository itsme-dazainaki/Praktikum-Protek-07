import os #ini buat ngimport modul, biar bisa masuk ke so dan nyari file dilokasi yg diketik

try : #yok mulai blok buat dicek exception
    nama = str(input("Masukkan Nama File (contoh = d:/namafile.txt):  ")) #ini buat nginput lokasi dan nama file
    if os.path.exists(nama): #ini kalo si inputan diatas ada
        mode = "a"
    else :     #ini kalo gaada
        mode = "r" 

    file = open(nama,mode) #ini buat buka si file
    
    ulang = True #ini variabel buat dicek perulangan 
    while(ulang==True):   #ini mulai blok perulangannya     
        tmbh = input("Masukan Data Yang Ingin Ditambahkan : ") #buat nginput 
        file.write(tmbh) #buat masukkin tambahannya
        lagi = input("Apakah Masih Ada Lagi? (y/n): ") #mari konfirmasi
        
        if lagi == "y" : #ini buat ngecek inputan diatas
            ulang=True
        elif lagi == "n" : #ini juga
            ulang=False
        else :
            print("Input Tidak valid") #ini kalo ada yg nginput selain y/n
            break
        
    file.close() #ini buat nutup file yg kita tambahin tadi

    file = open(nama, "r") #ini buat mbuka file yg udah ditambahi
    print(file.read()) #ini buat nampilin isinya
    
except FileNotFoundError : #ini buat handling kalo ada salah di inputan nama file
    print("Maaf ! File tidak ditemukan")

