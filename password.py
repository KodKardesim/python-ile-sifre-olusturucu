from random import choice
def password(uzunluk):
    kucukharfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    buyukharfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    rakamlar = "0123456789"
    karakterler = "#$%&_-*/.,;"
    allchar = ""
    kharf = input("Küçük harf ister misiniz? [e/h] : ")
    if kharf == "e" or kharf == "E":
        allchar += kucukharfler
    bharf = input("Büyük harf ister misiniz? [e/h] : ")
    if bharf == "e" or bharf == "E":
        allchar += buyukharfler
    rakam = input("Rakam ister misiniz? [e/h] : ")
    if rakam == "e" or rakam == "E":
        allchar += rakamlar
    karakter = input("Özel karakter ister misiniz? [e/h] : ")
    if karakter == "e" or karakter == "E":
        allchar += karakterler
    sifre = ""
    if allchar == "":
        print("Hiçbir seçenek seçilmedi.")
    else:
        for char in range(uzunluk):
            sifre += choice(allchar)
        print("Şifreniz : {}".format(sifre))


password(int(input("Kaç harfli şifre istersiniz : ")))
