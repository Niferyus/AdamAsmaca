import random

kelimeler = ["bilgisayar","laptop","fare","klayve","monitör","kamera"]
kullanılanharfler = []
secilenkelime = kelimeler[random.randint(0,len(kelimeler)-1)]
sayac = 8
gecicikelime = "_" * len(secilenkelime)
gecicikelimelist = list(gecicikelime)
kelimesayacı = 0


print("Adam asmaca oyununa hoşgeldiniz")
while sayac>0:
     print("Kelime: " + gecicikelime)
     print(f"Kalan deneme hakkı: {sayac}")
     print("Tahmin edilen harfler: ",end=" ")

     for i in range(len(kullanılanharfler)):
          print(kullanılanharfler[i], end=" ")
     tahminharf = input("\nBir harf tahmin edin: ")    
     tahminharf.lower()
     if(kullanılanharfler.count(tahminharf) == 1):
         print("Bu harfi zaten girdin")
     elif(tahminharf.isalpha() and kullanılanharfler.count(tahminharf) == 0):
         kullanılanharfler.append(tahminharf)
         
         baslaindex = 0
         if(secilenkelime.count(tahminharf) > 0):
            
            tekrarsayisi = secilenkelime.count(tahminharf)
            for i in range(tekrarsayisi):    
                index = secilenkelime.index(tahminharf,baslaindex)    
                gecicikelimelist[index] = tahminharf
                baslaindex = index +1
            gecicikelime = "".join(gecicikelimelist)
            print("Doğru tahmin")
         else:
            sayac -= 1
            print("Yanlış tahmin")     
     else:
         print("Program sadece harfleri kabul etmektedir")
     match sayac:
         case 7:
             print("|")
         case 6:
             print("|\n|")
         case 5:
             print("|\n|\n|")
         case 4:
             print("-----")
             print("|\n|\n|")
         case 3:
             print("-----")
             print("|  0\n|\n|")
         case 2:
             print("-----")
             print("|  0")
             print("|  |")
             print("|")
         case 1:
             print("-----")
             print("|  0")
             print("|  |")
             print("| /")
         case 0:
             print("-----")
             print("|  0")
             print("|  |")
             print("| / \\")
             print("\n\n\nKelimeyi Bulamadınız")
     print("////////////////////////////////////////////////////////////\n")
     if(gecicikelime.count("_") == 0):
         print("Kelimeyi buldunuz tebrikler")
         break
         