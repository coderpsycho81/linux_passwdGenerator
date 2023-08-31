#!/user/bin/env python
# -*- coding ut-8 -*-

import os
import random
import string
from colorama import Fore, Style

def figlet():
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet coderpsycho")
	
figlet()
print(" ")
print(Fore.YELLOW + "       -- RASTGELE SİFRE ÜRETİCİ -- " + Style.RESET_ALL)
print(" ")

def passwd_generator(uzunluk, buyuk_harf=True, kucuk_harf=True, rakam=True, ozel_karakter=True):
    karakterler = ''
    if buyuk_harf:
        karakterler += string.ascii_uppercase
    if kucuk_harf:
        karakterler += string.ascii_lowercase
    if rakam:
        karakterler += string.digits
    if ozel_karakter:
        karakterler += string.punctuation

    if not karakterler:
        print("Hata: En az bir karakter türü seçmelisiniz.")
        return None

    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

uzunluk = int(input(Fore.GREEN + "Şifrenin uzunluğunu girin: " +  Style.RESET_ALL))
print(" ")
buyuk_harf = input(Fore.YELLOW + ">> Büyük harf içersin mi? (Evet/Hayır): " + Style.RESET_ALL).strip().lower() == 'evet'
print(" ")
kucuk_harf = input(Fore.YELLOW + ">> Küçük harf içersin mi? (Evet/Hayır): " + Style.RESET_ALL).strip().lower() == 'evet'
print(" ")
rakam = input(Fore.YELLOW + ">> Rakam içersin mi? (Evet/Hayır): " + Style.RESET_ALL).strip().lower() == 'evet'
print(" ")
ozel_karakter = input(Fore.YELLOW + ">> Özel karakter içersin mi? (Evet/Hayır): " + Style.RESET_ALL).strip().lower() == 'evet'
print(" ")

if uzunluk > 0:
    sifre = passwd_generator(uzunluk, buyuk_harf, kucuk_harf, rakam, ozel_karakter)
    if sifre:
        print(Fore.GREEN + "-- Oluşturulan Şifre: " +  Style.RESET_ALL, Fore.RED + sifre + Style.RESET_ALL)

