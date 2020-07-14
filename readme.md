# Ezan Vakitleri
---
#### Flusk-Rest API
  - Öncelikle cihazın ip bilgisinden bulunduğu konum, API aracılığıyla tespit edilir.
  - Tespit edilen bu konuma göre, farklı bir API kullanarak Ezan Vakitleri listelenir.
  - Ayrıca bulunduğumuz konum dışında farklı illerin ezan saatlerine de bakabiliriz.
 
### Kullanılan API'lar:
 * IP bilgisinden konum tespiti API : [ip-Konum API]
 * Ezan Vakitleri API : [Namaz Vakitleri API]
 * Hadisler : [Hadis API]

### Yapılacaklar
 - Vaktin çıkmasına kalan süre, JS kullanılarak sayaç şekline dönüşütürülecek.
 - İller dropdown list'ten seçilebilir.
 - Bu Ezan API'da sadece iller bulunuyor, ilçelerinde bulunduğu farklı bir API kullanılabilir.
 - JS kullanılarak, şuan içerisinde bulunulan Ezan Saati tabloda farklı bir renkle gösterilebilir.
 
## Örnek-1
##### Cihazın IP bilgisinden Konya'da bulunduğu tespit ediliyor. Konya için Ezan Vakitleri Listeleniyor.
![alt text](https://i.ibb.co/Jtch57W/ss1.png)

## Örnek-2
##### İstediğimiz herhangi bir ilin Ezan Vakitlerine bakalım.
![alt text](https://i.ibb.co/J56ypz5/Ezan-Vakitleri2.png)

   [ip-Konum API]: <https://collectapi.com/tr/api/ip/ip-adresi-api>
   [Namaz Vakitleri API]: <https://collectapi.com/tr/api/pray/namaz-vakitleri-api>
   [Hadis API]: <http://berkayertugrul.site/EzanApp/Hadisler.json>
 

