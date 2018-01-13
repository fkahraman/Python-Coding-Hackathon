#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                               #
#                      FATİH   KAHRAMAN                         #
#                                                               #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

"""
                                        İDDİA

    Semre ile Kemre, sayı tabanlarında uzman olduğunu düşünen Yemreyi bir iddiaya
    sürüklemişlerdir. İddiaya göre Yemre, Semre’nin istediği tabanda( B ) Kemre’nin istediği
    basamaklı( N ) bütün sayıları defterine yazacaktır.

    Prensiplerini bozmak istemeyen Yemre, bir sayfa dolmadan diğer sayfaya geçmiyor ve her
    sayfaya C adet sayı sığabiliyor.

    Sizden istenen, Yemre’nin son sayfaya kaç tane sayı yazacağını bulmanız.

    Girdi Biçimi:

    Tek satırda sırasıyla B (Sayı tabanı), N (Sayıların uzunluğu) ve C (Bir sayfayı kaç sayının
    dolduracağı) sayıları verilmektedir.

    Çıktı Biçimi:

    Yemre’nin son sayfaya kaç adet sayı yazdığı.

    Örnek Girdi 1:
    2 3 3

    Örnek Çıktı 1:
    1

    Örnek Girdi 2:
    2 3 4

    Örnek Çıktı 2:
    4

    Sınırlar:
    2 ≤ B ≤ 10^10^6
    1 ≤ N ≤ 10^10^6
    1 ≤ C ≤ 10^9
"""

if __name__ == '__main__':
    dizin = []
    dizin = input("")
    taban = int(dizin[0])
    uzunluk = int(dizin[2])
    sayfa = int(dizin[4])

    uzunluk = uzunluk - 1

    toplam = 0
    sonuc = 0

    toplam = uzunluk**taban
    toplam = toplam * (taban-1)

    sonuc = toplam % sayfa

    if(sonuc == 0):
        sonuc = sayfa

    print(sonuc)

