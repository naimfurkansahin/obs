'''
yazar : nAİm
mail: naimfurkansahin@gmail.com
tarih: 22.10.2025

açıklama: python programa dilini bir öğrenci
bilgi sistemi senaryosu ile öğreten bir repo
(anaprogram dosyası)

'''

if __name__ == "__main__":
    
    
    baslik = "Öğrenci Bilgi Sistemi (v1)"

    print("-"*100)
    print(f"| {baslik:^94} |x|")
    print("-"*100)

    ogrenci_adlari = []
    ogrenci_soyadlari = []
    ogrenci_nolari = [] 

    ogrenci_sayisi = int(input("Öğrenci sayısını giriniz: "))

    for sıra in range(ogrenci_sayisi):
        ogrenci_adlari.append(input(f"{sıra+1} . Öğrenci adını giriniz: "))        
        ogrenci_soyadlari.append(input(f"{sıra+1} . Öğrenci soyadını giriniz: "))  
        ogrenci_nolari.append(input(f"{sıra+1} . Öğrenci numarasını giriniz: "))   

    print("-"*100)
    print(f"| {" "*8}| {"İsim":<35} | {"Soyisim":<25} | {"Numara":<20} |")
    print("-"*100)

    for sıra in range(ogrenci_sayisi):
        print(f"| {sıra+1:^7} | {ogrenci_adlari[sıra]:<35} | {ogrenci_soyadlari[sıra]:<25} | {ogrenci_nolari[sıra]:<20} |")
