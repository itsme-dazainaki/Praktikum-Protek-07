print ("-----------------------------------")
print ("    PROGRAM HITUNG RATA-RATA       ") #ini buat inputan
print ("-----------------------------------")


sum = 0 #mari deklarasikan nilai awal variabel
jumlah = 0 #ini juga
a= True #ini variabel buat dicek perulangan
while ( a == True): #ini mulai blok perulangan
    try : #mari mulai blok pengecekan exception
        bil = int(input("Masukkan Bilangan Bulat : ")) #buat nginput bilangan
        sum += bil #ini jumlahin data bilangan
        jumlah +=1 #ini increment

        lagi = input("Lagi (y/n) ? : ") #konfirm kalau mau ngisi lagi
        if(lagi=="y"): #cek kondisi kalo yg dipilih y
            a = True
        elif(lagi=="n"): #cek kondisi kalo ygdipilih n
            a = False
        else :
            print ("Input Tidak Valid") #ini buat inputan selain y/n
            break #hop selesai ngulang
        
    except ValueError : #ini buat handling kalo inputan bukan bilangan
        print("Bukan Bilangan Bulat") #ini yang ditampilkan
        continue
    
rata = sum / jumlah
print("Rata-ratanya adalah : ", rata)
