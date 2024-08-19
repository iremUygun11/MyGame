
import random
def tas_kagit_makas_iREM_UYGUN():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar: \n Taş makası yener. \n Makas kağıdı yener. \n Kağıt taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır. İyi şanslar!")

    secenekler = ["taş", "kağıt", "makas","kağit"]
    oyun_sayisi = 0
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0

    while True:
        oyun_sayisi += 1
        tur_sayisi = 0
        oyuncu_tur_galibiyet = 0
        bilgisayar_tur_galibiyet = 0

        while oyuncu_tur_galibiyet < 2 and bilgisayar_tur_galibiyet < 2:
            tur_sayisi += 1
            print(f"\n{tur_sayisi}. Tur")
            
            oyuncu_secimi = input("Taş, kağıt, makas seçiminizi yapın: ").lower()
            #not in kullanarak bir koşulu da içinde olmaması durumu için yapıyoruz.
            while oyuncu_secimi not in secenekler:
              #kullanıcı girişi verilen karakterlere eş değer olsun diye .lower ile hepsini küçük yaptırıyoruz.
                oyuncu_secimi = input("Geçersiz seçim! Lütfen tekrar taş, kağıt veya makas seçin: ").lower()

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi} \nSizin seçiminiz: {oyuncu_secimi}")
             
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_tur_galibiyet += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_tur_galibiyet += 1

            print(f"Tur Durumu: Oyuncu {oyuncu_tur_galibiyet} - Bilgisayar {bilgisayar_tur_galibiyet}")

        if oyuncu_tur_galibiyet == 2:
            print("\nTebrikler, oyunu kazandınız!")
            oyuncu_galibiyet += 1
        else:
            print("\nMaalesef oyunu bilgisayar kazandı.")
            bilgisayar_galibiyet += 1

        print(f"Oyun Durumu: Oyuncu {oyuncu_galibiyet} - Bilgisayar {bilgisayar_galibiyet}")
        seçim=["hayır","hayir","evet"]
        devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayır"]).lower()
        #Büyük harf .lower() metodu ile ingilizce karaktere geçtiği için o koşulları da kodun çalışması için ekleyeceğiz.
        #Benim geçersiz karakter girmeme rağmen bilgisayar seçimini hayır olarak yapmışsa bu şarta girerek direkt oyunu bitirmesini istedim.
        if bilgisayar_devam== "hayır" and devam not in seçim:
            print("Geçersiz seçim yaptınız fakat bilgisayar devam etmek istemiyor.\nTeşekkürler! Bir sonrakı oyuna görüşmek üzere :)!")
            break
        while devam  not in seçim:
              #kullanıcı girişi verilen karakterlere eş değer olsun diye .lower ile hepsini küçük yaptırıyoruz.
                devam = input("Geçersiz seçim! Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
            
        if devam == "hayır" or devam == "hayir":
            print("Oyun sona erdi.Siz oyuna  devam etmek istemiyorsunuz. \nTeşekkürler! Bir sonrakı oyuna görüşmek üzere :)!")
            break
        elif bilgisayar_devam== "hayır":
            print("Oyun sona erdi.Bilgisayar devam etmek istemiyor. \nTeşekkürler! Bir sonrakı oyuna görüşmek üzere :)!")
            break       
        
        else :
            print("İkinizde oyuna devam etmek istediniz. \nYeni bir oyun daha!")
        
                
    
# Fonksiyonu çalıştırmak için:
tas_kagit_makas_iREM_UYGUN()

