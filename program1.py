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

    ogrenci_adlari.append(input("1.Öğrenci adını giriniz: "))        # 0.indeks
    ogrenci_soyadlari.append(input("1.Öğrenci soyadını giriniz: "))  # 0.indeks
    ogrenci_nolari.append(input("1.Öğrenci numarasını giriniz: "))   # 0.indeks

    ogrenci_adlari.append(input("2.Öğrenci adını giriniz: "))        # 1.indeks
    ogrenci_soyadlari.append(input("2.Öğrenci soyadını giriniz: "))  # 1.indeks
    ogrenci_nolari.append(input("2.Öğrenci numarasını giriniz: "))   # 1.indeks

    ogrenci_adlari.append(input("3.Öğrenci adını giriniz: "))        # 2.indeks
    ogrenci_soyadlari.append(input("3.Öğrenci soyadını giriniz: "))  # 2.indeks
    ogrenci_nolari.append(input("3.Öğrenci numarasını giriniz: "))   # 2.indeks

    print("-"*100)
    print(f"| {" "*8}| {"İsim":<35} | {"Soyisim":<25} | {"Numara":<20} |")
    print("-"*100)
    print(f"| {1:^7} | {ogrenci_adlari[0]:<35} | {ogrenci_soyadlari[0]:<25} | {ogrenci_nolari[0]:<20} |")
    print(f"| {2:^7} | {ogrenci_adlari[1]:<35} | {ogrenci_soyadlari[1]:<25} | {ogrenci_nolari[1]:<20} |")
    print(f"| {3:^7} | {ogrenci_adlari[2]:<35} | {ogrenci_soyadlari[2]:<25} | {ogrenci_nolari[2]:<20} |")



    '''
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    '''