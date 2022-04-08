#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
#hozirgi_zamon_shaxslar=["Steave Jobs","Shavkat Mirziyeyev","Jony deep","Khabib"]
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib 
#olib (.pop()), quyidagi ko'rinishda chiqaring:
#print("Men tarixiy shaxslardan",tarixiy_shaxslar.pop(0),"bilan , zamonaviy shaxslardan esa", hozirgi_zamon_shaxslar.pop(0),"bilan suxbat qurishni xoxlardim")
#friends=[]
#friends.append("Abdulaziz")
#friends.append("Amirxon")
#friends.append("Jaxongir")
#friends.append("Abror")
#friends.append("Jasur")
#print(friends)
#mehmonga_kela_olmaydiganlari=friends.remove("Abdulaziz")
#mehmonga_kela_olmaydiganlari=friends.remove("Amirxon")
#print("Bugun mehmonga kela olmaydigan dustlarimning ruyxati:",friends)
#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari 
#yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar 
#ro'yxatiga qo'shing.
#mehmonlar=[]
#mehmonlar.append("Rustam")
#mehmonlar.append("Botir")
#mehmonlar.append(friends.pop())
#mehmonlar.append(friends.pop())
#mehmonlar.append(friends.pop())
#print(mehmonlar)
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#davlatlar=["UZBEKISTAN","RUSSIA","UK","USA","CHINA","JAPAN","AUSTRALIA","NORWEY"]
#davlatlar_soni=len(davlatlar)
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#sonlar=list(range(120,1200,2))
#print(max(sonlar)-min(sonlar))
#Ro'yxatdagi elementlar sonini hisoblang
#print(len(sonlar))
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#print(list(sonlar[0:20]))
#print(list(sonlar[260:280]))
#print(list(sonlar[-20:]))
#taomlar=[]
#taomlar.append("shurva")
##taomlar.append("osh")
#taomlar.append("kabob")
#taomlar.append("jiz")
#taomlar.append("manti")
#taomlar.append("norin")
#nonushta=taomlar[:]
#nonushta.remove("kabob")
#nonushta.remove("jiz")
#nonushta.remove("manti")
#nonushta.remove("norin")
#nonushta.remove("osh")
#nonushta.insert(0, "blinchik")
#nonushta.insert(3, "Sut")
#print(nonushta + taomlar)
#nonushta=tuple(nonushta)
#nonushta[0]="qaymoq va nonx`"
#ismlar=["ABROR","AMIRXON","JAXONGIR","ABDULAZIZ","QUTLUGMUROD"]
#for ism in ismlar:
 #   print(f"Salom  {ism}")
#print("Kod" ,len(ismlar), "marta takrorlandi")
#sonlar=list(range(11,100,2))
#for son in sonlar:
 #   print(son**3)
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga
# saqlab oling. Natijani konsolga chiqaring
#kinolar=[]
#for n in range(5):
#    kinolar.append(input(f"{n+1}-yoqtirgan filmingiz \n" ) )
#print(kinolar)    
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir
#suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
##suhbatlashganlar_soni=int(input("Bugun nechta odam bilan suhbatlashdingiz?>>>")
#cars=["toyota","mazda","hyundai","gm","kia","bmw"]
#for car in cars:
  #  if car=="gm" or car=="bmw":
 #       print(car.upper())
   # else:
    #.    print(car.title())
#         
#for car in cars:
#    if car != "gm" and car!="bmw":
#        print(car.title())
#    else:
#        print(car.upper())
#foydalanuchi_logini=input("Login parolingizni kiriting \n")
#if foydalanuchi_logini=="admin":
#    print('"Xush kelibsiz", Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
#else:
#    print(f"Xush  kelibsiz {foydalanuchi_logini}")
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
#"Sonlar teng" ekan degan yozuvni konsolga chiqaring          
#x=float(input("Birinchi sonni kiriting>>>"))
#y=float(input("Ikkinchi sonni kiriting>>>"))
#if x==y: print(f"Sonlar bir biriga teng:{x}={y}")          
#son=int(input("son kiriting>>>"))
#if son<0:
#    print(f"{son} manfiy son")
#elif son==0:print(f"{son} manfiy xam musbat xam emas")    
#else:    
#    print(f"{son} musbat son")
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini
# hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring
#son=int(input("Son kiriting>>>"))
#if son>0:
#    print(son**(1/2))
#else:
#    print("Musbat son kiriting")    
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa 
#"Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
#son_kiriting=float(input("Juft son kiriting>>>"))
#if son_kiriting%2==0:
#    print("Rahmat")
#else: 
#    print("Juft son kiriting")    
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#gar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#yosh=int(input("Yoshingiz nechida\n "))
#if yosh<=4 or yosh>60:
#    print("Sizga muzeyga kirish bepul")
#elif yosh<18:
#    print("Sizga muzeyga kirish 10000 so'm")
#else:
#    print("Sizga muzeyga kirish 20000 so'm")    
 #Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va 
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring   
#x,y=input("1-sonni son kiriting:"),input("2-sonni kiriting:") 
#if x>y:
#    print(f"{x} > {y}") 
#elif x==y:
#    print(f"{x} < {y} ")
#else:
#    print(f"{x} = {y} 4")    
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
#Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
#5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda 
#yo'q" degan xabarlarni chiqaring.
#mahsulotlar=["olma","shaftoli","banan","uzum","nok","anjir","gilos","o'rik","bexi","anjir","piyola","non","saryog","gusht","shakar"]
#savat=[]
#bor_mahsulotlar=[]
#yoq_mahsulotlar=[]
#for n in range(5) :
#   savat.append(input(f"{n+1}-maxsulot kiriting:"))
#print("Do'konimizda quyidagi maxsulotlar yoq")    
#for xarid in savat:
#    if xarid not in bor_mahsulotlar:
#        print(xarid)
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        yoq_mahsulotlar.append(mahsulot)
#if yoq_mahsulotlar:
#    print("Do'konimizda quyidagi mahsulotlar yoq:")
#    for mahsulot in yoq_mahsulotlar:
#        print(mahsulot)
#else:
#    print("Bizda barcha maxsulotlar bor")     
#if bor_mahsulotlar:
#    if len(bor_mahsulotlar)!=5:
#        print("Bizda quyidagi mahsulotlar bor")    
#        for mahsulot in bor_mahsulotlar:
#            print(mahsulot)
#foydalanuvchilar=["anvar","abror","rustam","botir","alisher"] 
#login_kirit=input("login kiriting\n>>>")
#if login_kirit in foydalanuvchilar:
#    print(f"{login_kirit} bunday login band, boshqa login kiriting.")
#else:
#    print("Xush kelibsiz!",login_kirit)    
#butun_son_kirit=int(input("Butun son kiriting"))
#bulinuvchilar=list(range(2,11))
#for bulinuvchi in bulinuvchilar:
#    if butun_son_kirit%bulinuvchi==0:
#        print(f"{butun_son_kirit} {bulinuvchi} ga qoldiqsiz bulinadi")
    
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10
# gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.       
print(2//2)
print(2/2)
print(2%2)

    

    






