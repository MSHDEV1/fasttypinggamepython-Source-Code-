#MSHDEV
import random
dil = str(input("Dil Seçiniz(eng or tur): "))

if dil == "tur":
 
 x = int(input("Hak: "))
 yazı = ["elma","armut","kalem","taş","abajur","abacılık","haber","habersiz","hac","hacı","hadise","kabadayı","kabaklamak","kablosuz","kaçamak","kaçınganlık","zabıta","radyasyon","radyo","raf","rahip","pala","palamut","palazlamak","palyaço","pamuk","obje","objektif","obruk","ocakbaşı","odaklamak","ebeveyn"]
 puan = 0 
 yazıstr = ""

 while x > 0:
  yazıstr += random.choice(yazı)

  print(yazıstr)
  bilgi = str(input("Yazı: "))
    
  if bilgi == yazıstr:
     yazıstr = ""
     puan += 10
     print(puan)
  else:
    yazıstr = ""
    puan -= 10
    print(puan)
  x -= 1

if dil == "eng":
 
 xs = int(input("Hak: "))
 yazı2 = ["yes","no","words","add","admit","approve","arrive","build","check","confirm","connect","create","damage","destroy","discuss","drive","exercise","follow","grow","give","inform","jump","knock","live","manage","open","prefer","remember","respond","say","select","show","travel","understand","watch","agreed","alone","amount","buy","Master"]
 puan2 = 0 
 yazıstr2 = ""

 while xs > 0:
    yazıstr2 += random.choice(yazı2)

    print(yazıstr2)
    bilgi2 = str(input("Yazı: "))
    
    if bilgi2 == yazıstr2:
        yazıstr2 = ""
        puan2 += 10
        print(puan2)
    else:
        yazıstr2 = ""
        puan2 -= 10
        print(puan2)
    xs -= 1
#MSHDEV