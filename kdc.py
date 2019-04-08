#Bir firmanın katma değer cirosunu fonksiyon kullanarak hesaplayınız.
#Eğer katma değer cirosu 1000’ den yüksek ise “İşletme katma değer cirosu yüksek”, 500-999 arasında ise “işletme katma değer cirosu normal” ,
#500 den küçük ise “işletme katma değer cirosu düşük” olarak yazdırınız. (Değerler dışarıdan girilecektir
#Katma Değer Ciro = Toplam Satış Miktarı – (Hammadde maliyeti + Bakım Onarım Giderleri + Sevkiyat Giderleri + Satın Alınan Hizmet Giderleri)
def katmaDegerCiro():
    print("Lütfen istenilen degerleri giriniz:")
    a = int(input("toplam satis miktari:"))
    b = int(input("hammadde maliyeti:"))
    c = int(input("bakim onarim giderleri:"))
    d = int(input("sevkiyat giderleri:"))
    e = int(input("satin alinan hizmet giderleri:"))
    katmaDegerCiro = a - (b + c + d + e)
    if (katmaDegerCiro > 1000):
        print("Isletme katma deger cirosu yüksek.")
    elif (500 < katmaDegerCiro < 999):
        print("Isletme katma deger cirosu normal")
    else:
        print("Isletme katma deger cirosu düsük")

    print("İşletmenizin Katma Değer Cirosu:", katmaDegerCiro)
    return
katmaDegerCiro()
