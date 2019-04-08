#Bir işletmenin müşterilerle çalışma süresi aşağıdaki formül ile bulunmaktadır.
#Müşterilerle çalışma süresi=Çalışılan süre / Toplam Müşteri Sayısı
#2016 yılında çalışılan süre 170 saat ve toplam müşteri sayısı 50 dir. 2017 yılında çalışılan süre 50 saat artmış ve müşteri sayısı 20 kişi artmıştır.
#Buna göre 2016 ve 2017 yılı müşterilerle çalışma  sürelerini fonksiyon kullanarak hesaplayınız ve 2017 ve 2016 yılları müşterilerle çalışma süreleri arasındaki farkı bulan python kodunu yazınız.

def ilkYıl():
    cs=170
    tms=50
    global mcs
    mcs=cs/tms
    return mcs
def ikinciYıl():
    cs=220
    tms=70
    global mcs
    mcs=cs/tms
    return mcs
ilk=ilkYıl()
ikinci=ikinciYıl()
fark=ikinci-ilk
print("2017 ve 2016 yılları arasındaki müşteri çalışma süresi farkı:",fark,"saattir.")

###################

#Bir işletmenin 25 çalışanı bulunmaktadır. Buna göre toplam ciro değerini hesaplayarak adambaşı
#ciro değerini bulunuz. (hesaplamalar fonksiyon kullanılarak yapılacaktır)
#Ciro: Satış Miktarı x Birim Satış Fiyatı
#Adambaşı Ciro: Toplam Ciro / Toplam Çalışan Sayısı


def adamBasiCiroHesapla():
    a=int(input("satis miktarini giriniz:"))
    b=int(input("birim satis fiyatini giriniz:"))
    c=int(25)
    adamBasiCiro=(a*b)/c
    print("adam basi ciro:",adamBasiCiro)
    return
adamBasiCiroHesapla()
