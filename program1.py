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
    
    print(len(baslik))
    print(baslik)

    print("-"*100)
    print(f"| {baslik:^94} |x|")
    print("-"*100)

    ogrenci_adi = input("Öğrenci adını giriniz: ")
    ogrenci_soyadi = input("Öğrenci soyadını giriniz: ")
    ogrenci_no = input("Öğrenci numarasını giriniz: ")

    print("-"*100)
    print(f"| {" "*8}| {"İsim":<31} | {"Soyisim":<30} | {"Numara":<20} |")
    print("-"*100)
    print(f"| {1:^7} | {ogrenci_adi:<31} | {ogrenci_soyadi:<30} | {ogrenci_no:<20} |")



    '''
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    '''