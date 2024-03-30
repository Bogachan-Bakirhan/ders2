import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifreuzunlugu = int(input("Şifreniz kaç karakterden oluşsun: "))

sifre = ""

for i in range(sifreuzunlugu):
    sifre += random.choice(karakterler)

print(sifre)
