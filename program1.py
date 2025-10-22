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
    print("|",baslik," "*(94-(len(baslik)+1)),"|x|")
    print("-"*100)

    ogrenci_adi = input("Öğrenci adını giriniz: ")
    ogrenci_soyadi = input("Öğrenci soyadını giriniz: ")
    ogrenci_no = input("Öğrenci numarasını giriniz: ")

    print("-"*100)
    print("|","İsim"," "*(94-(len(baslik)+1)),"|x|")
    print("-"*100)



    '''
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    print("|"," "*96,"|")
    '''