'''
    yazar: nAİm
    email: naimfurkan_sahin25@trabzon.edu.tr
    
    aciklama: Python programlama dilini
    bir ogrenci bilgi sistemi senaryosu ile
    ogreten bir repo (anaprogram dosyasi)
'''

if __name__ == "__main__":

    #dictionary ---> demet
    ogrenciler = {  "12345":{'isim':'Furkan','soyisim':'Sahin'},
                    "12346":{'isim':'Ilknur','soyisim':'Uzum'},
                    "12347":{'isim':'Arif','soyisim':'Uysal'},}

    print('''
----------------------------------------
Ogrenci Bilgi Sistemi v.1
----------------------------------------
| Komut Listesi                        |
----------------------------------------
| kapat   | Uygulamayi sonlandir       |
| ekle    | Ogrenci ekle               |
| sil     | Ogrenci siler              |
| guncelle| Ogrenci gunceller          |
| listele | Ogrencileri listeler       |
----------------------------------------        
''')

    komut = input('Komut giriniz:').strip().lower()
    while komut != 'kapat':

        if komut == 'ekle':
            print('----------------------------------------')
            ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

            for sira in range(ogrenci_sayisi):
                key = input(f'{sira+1}. Ogrenci numarasini giriniz:')

                if key in ogrenciler:
                    print(f"{ogrenci_numarasi} numaralı ogrenci zaten var")
                else:
                    isim = input(f'{sira+1}. Ogrenci ismini giriniz:')
                    soyisim = input(f'{sira+1}. Ogrenci soyismini giriniz:')
                    ogrenciler[key] = {'isim': isim, "soyisim" : soyisim}
            print('----------------------------------------')

        elif komut == 'sil':
            print('----------------------------------------')
            ogrenci_numarasi = input('Ogrenci numarasini giriniz:')

            try:
                del ogrenciler[ogrenci_numarasi]
                print(f'{ogrenci_numarasi} numarali ogrenci silindi!')
            except:
                print(f'{ogrenci_numarasi} numarali bir ogrenci yok!')
                print('----------------------------------------')

        elif komut == 'guncelle':
            print('----------------------------------------')
            key = input(f'Ogrenci numarasini giriniz:')

            if key in ogrenciler:
                isim = input(f'Ogrenci ismini giriniz:')
                soyisim = input(f'Ogrenci soyismini giriniz:')

                ogrenciler[key] = {'isim': isim, "soyisim" : soyisim}

                print(f"{key} numaralı öğrenci güncellendi.")

            else:
                print(f"{key} numaralı bir öğrenci bulunamadı.")

        elif komut == 'listele':
            print('----------------------------------------')
            print('-' * 40)
            print(f'|{" "*2}| {"Isim":<13} | {"Soyisim":<8} | {"Numara":<5} |')
            print('-' * 40)
            for sira, key in enumerate(ogrenciler):
                print(f"|{(sira+1):>2}| {ogrenciler[key]['isim']:<13} | {ogrenciler[key]["soyisim"]:<8} | {key:<6} |")
            print('----------------------------------------')

        else:
            print('----------------------------------------')
            print(f'"{komut}" seklinde tanimli bir komut bulanamadi!')
            print('----------------------------------------')
        
        komut = input('Komut giriniz:').strip().lower()

    print('------------------------------------')
    print('Program sonlandirildi!')
    print('------------------------------------')
