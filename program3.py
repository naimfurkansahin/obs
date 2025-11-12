'''
    yazar: nAİm
    email: naimfurkan_sahin25@trabzon.edu.tr
    
    aciklama: Python programlama dilini
    bir ogrenci bilgi sistemi senaryosu ile
    ogreten bir repo (anaprogram dosyasi)
'''

def print_intro(version):
    print(f'''
----------------------------------------
Ogrenci Bilgi Sistemi v.{version}
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


def ogrenci_ekle(odict):
    print('----------------------------------------')
    ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

    for sira in range(ogrenci_sayisi):
        key = input(f'{sira+1}. Ogrenci numarasini giriniz:')
        
        if key in odict: 
            print(f'{key} numarali ogrenci zaten mevcut!')
        else:
            isim = input(f'{sira+1}. Ogrenci adini giriniz:')
            soyisim = input(f'{sira+1}. Ogrenci soyadini giriniz:')
            odict[key] = {'isim':isim,'soyisim':soyisim}
    print('----------------------------------------')

def ogrenci_sil(odict):
    print('----------------------------------------')
    ogrenci_numarasi = input('Ogrenci numarasini giriniz:')

    try:
        del odict[ogrenci_numarasi]
        print(f'{ogrenci_numarasi} numarali ogrenci silindi!')
    except:
        print(f'{ogrenci_numarasi} numarali bir ogrenci yok!')
    print('----------------------------------------')

def ogrenci_guncelle(odict):
    print('----------------------------------------')
    key = input(f'Ogrenci numarasini giriniz:')

    if key in odict:
        isim = input(f'Ogrenci adini giriniz:')
        soyisim = input(f'Ogrenci soyadini giriniz:')
        
        odict[key] = {'isim':isim,'soyisim':soyisim}
        print(f'{key} numarali bir ogrenci guncellendi!')
    else:
        print(f'{key} numarali bir ogrenci yok!')
    print('----------------------------------------')

def ogrenci_listele(odict):
    print('----------------------------------------')
    print('-' * 40)
    print(f'|{" "*2}| {"Isim":<13} | {"Soyisim":<8} | {"Numara":<5} |')
    print('-' * 40)
    for sira, key in enumerate(odict):
        print(f'|{(sira+1):>2}| {odict[key]['isim']:<13} | {odict[key]['soyisim']:<8} | {key:<5} |')    
    print('----------------------------------------')

if __name__ == '__main__':

    ogrenciler = {'12345':{'isim':'Ramazan Ozgur','soyisim':'Dogan'},
                  '12346':{'isim':'Hulya','soyisim':'Yaldiz'},
                  '12347':{'isim':'Yigit Kagan','soyisim':'Caliskan'}}
  
    print_intro('2.3')

    komut = input('Komut giriniz:').strip().lower()

    while komut != 'kapat':
        if komut == 'ekle':            
            ogrenci_ekle(ogrenciler)
            ogrenci_listele(ogrenciler)
        elif komut == 'sil':
            ogrenci_sil(ogrenciler)
            ogrenci_listele(ogrenciler)
        elif komut == 'guncelle':
            ogrenci_guncelle(ogrenciler)
        elif komut == 'listele':
            ogrenci_listele(ogrenciler)
        else:
            print('----------------------------------------')
            print(f'"{komut}" seklinde tanimli bir komut bulanamadi!')
            print('----------------------------------------')
        
        komut = input('Komut giriniz:').strip().lower()

    print('------------------------------------')
    print('Program sonlandirildi!')
    print('------------------------------------')