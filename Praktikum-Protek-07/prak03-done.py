file = open("d:/data_2.txt","r")
sum = 0
for data in file:
    try : #ini buat mulai nandain blok yang mau dihandling
        sum = sum + int(data)
    except ValueError: #ini handlingnya, kalo ada error tsb perintah dibawahnya akan dijalankan
        continue
print(sum)
