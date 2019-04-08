"""Return On Investment (ROI), yaptığınız yatırımın size geri dönüşünün nasıl olacağını gösteren bir çeşit veridir.
Bir SEO ajansıyla çalışmayı düşünüyorsanız, bu çalışmanın size ne kadara mal olacağı ve sonucunda ne kadar kazanç sağlayacağınızı merak edebilirsiniz.
Formül : ((Aylık Arama hacmi / Tıklama Oranı) / Satın alma oranı) x Ürün Fiyatı = Kazanç """
def roiHesapla(ah,tık,sam,uf):
    roi=((ah/tık)/sam)*uf
    return roi
ah=int(input("Aylık arama hacminiz:"))
tık=int(input("Tıklama oranı:"))
sam=int(input("Satın alma oranı:"))
uf=int(input("Ürün Fiyatı:"))
kazanc=roiHesapla(ah,tık,sam,uf)
print("Yatırımınızın geri dönüşü:",kazanc,"dir.")
