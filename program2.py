if __name__ =='__main__':

    print('''
          -----------------------------------
          | Ögrenci bilgi sistemi v.1       |
          -----------------------------------
          | Komut Listesi                   |
          -----------------------------------
          | kapat   | Uygulamayi sonlandir  |
          | ekle    | Ogrenci ekle          |
          | sil     | Ogrenci siler         |
          | listele | Ogrencileri listeler  |
          -----------------------------------
          ''')
    ogrenci_adlari = ['Furkan','İlknur','Sima']
    ogrenci_soyadlari = ['Şahin','Üzüm','Bostan']
    ogrenci_numaralari = ['1234','1235','1236']
    

    
    komut = input("Komut giriniz:").strip().lower()
    while komut != 'kapat':
        if komut == 'ekle':
            print('------------------------------------------------------')
            Ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

            for sira in range(Ogrenci_sayisi):
                ogrenci_adlari.append(input(f'{sira+1}.ogrencinin adini giriniz:'))      
                ogrenci_soyadlari.append(input(f'{sira+1}.ogrencinin soyadini giriniz:')) 
                ogrenci_numaralari.append(input(f'{sira+1}.ogrencinin numaranizi giriniz:')) 
            print('------------------------------------------------------')
        elif komut == 'sil':
            print('------------------------------------------------------')
            Ogrenci_numarasi = (input('Ogrenci numarasini giriniz:'))
            #index = -1
            #for i, numara in enumerate(ogrenci_numaralari):
            #    if numara == Ogrenci_numarasi:
            #        index = i
            try:
                index = ogrenci_numaralari.index(Ogrenci_numarasi)
                ogrenci_numaralari.pop(index)
                ogrenci_adlari.pop(index)
                ogrenci_soyadlari.pop(index)
                print(f'{Ogrenci_numarasi} numarali ogrenci silindi!')
            except ValueError:
                print(F'{Ogrenci_numarasi} numarali bir ogrenci yok!')
            
            #if index == -1:
            #    print(F'{Ogrenci_numarasi} numarali bir ogrenci yok!'),
            #else:
            #    ogrenci_numaralari.pop(index)
            #   ogrenci_adlari.pop(index)
            #   ogrenci_soyadlari.pop(index)
             #   print(f'{Ogrenci_numarasi} numarali ogrenci silindi!')
                

            print('------------------------------------------------------')
        elif komut == 'listele':
            print('-' * 54)
            print(f'|{' '*3}| {"Isim":<15} | {"Soyisim":<15} | {"Numara":<10} |')
            print('-' * 54)
            for sira in range(len(ogrenci_adlari)):
                print(f'| {(sira+1):^1} | {ogrenci_adlari[sira]:<15} | {ogrenci_soyadlari[sira]:<15} | {ogrenci_numaralari[sira]:<10} |')
                
            print('------------------------------------------------------')
        else:
            print('------------------------------------------------------')
            print(f'"{komut} seklinde tanimli bir komut bulunmamaktadir.')
            print('------------------------------------------------------')
   
        komut = input('Komut giriniz:').strip().lower()
        
    print('------------------------------------------------------')
    print('Program sonlandirildi.')
   
   
   
    
    # baslik = 'Ogrenci Bilgi Sistemi (v1)'

    # print(baslik)
    # print(len(baslik))

    # print('-' * 100)
    # print(f'| {baslik:^94} |x|')
    # print('-' * 100)
     
    # ogrenci_adlari = []
    # ogrenci_soyadlari = []
    # ogrenci_nuamaralari = []

    # Ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

    # for sira in range(Ogrenci_sayisi):
    #     ogrenci_adlari.append(input(f'{sira+1}.ogrencinin adini giriniz:'))      
    #     ogrenci_soyadlari.append(input(f'{sira+1}.ogrencinin soyadini giriniz:')) 
    #     ogrenci_nuamaralari.append(input(f'{sira+1}.ogrencinin numaranizi giriniz:')) 
    
    
    
    # print('-' * 100)
    
    # print(f'|{' '*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    # print('-' * 100)
    # for sira in range(Ogrenci_sayisi):
    #     print(f'| {(sira+1):>7d} | {ogrenci_adlari[sira]:<35} | {ogrenci_soyadlari[sira]:<25} | {ogrenci_nuamaralari[sira]:<20} |')
  
   



