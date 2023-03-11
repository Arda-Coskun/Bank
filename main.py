import pickle

import os

from termcolor import colored

import curses

from random import randint, choice

import random

from termcolor import cprint

import time

from time import sleep

import colorama

from colorama import Fore, Back, Style

import sys

import os

import pathlib


class Account:

    accNo = 0

    name = ''

    deposit = 0

    type = ""

    def createAccount(self):
        clear()
        self.accNo = int(input("Hesap numaranızı giriniz : "))

        self.name = input("Hesap sahibinin ismini giriniz : ")

        self.type = input("Hesap tipini giriniz : ")

        self.deposit = int(
            input("Açılacak hesaba yatırılacak miktarı giriniz : "))

        islem_animation()

        print(Fore.GREEN)
        print("\n\n\nHesap oluşturuldu.")
        print(Style.RESET_ALL)

    def showAccount(self):
        clear()
        print("Hesap numarası : ", self.accNo)

        print("Hesap sahibinin ismi : ", self.name)

        print("Hesap tipi", self.type)

        print("Yatırılan para miktarı : ", self.deposit)

    def modifyAccount(self):
        clear()
        print("Hesap numarası : ", self.accNo)

        self.name = input("Modify Account Holder Name :")

        self.type = input("Hesap tipini düzenle :")

        self.deposit = int(input("Yatırılan para miktarını düzenleyin :"))

    def depositAmount(self, amount):

        self.deposit += amount

    def withdrawAmount(self, amount):

        self.deposit -= amount

    def report(self):
        clear()
        print(self.accNo, " | ", self.name, " | ", self.type, " | ",
              self.deposit)

    def getAccountNo(self):

        return self.accNo

    def getAcccountHolderName(self):

        return self.name

    def getAccountType(self):

        return self.type

    def getDeposit(self):

        return self.deposit
mikv = 0
mika = 0

def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.033)
    
  print()

sleep_time = 0.05
sleep_time1 = 1

def warning():
        print(Fore.WHITE)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()
        print(Fore.RED)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()        
        print(Fore.WHITE)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()
        print(Fore.RED)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()
        print(Fore.WHITE)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()
        print(Fore.RED)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()        
        print(Fore.WHITE)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()
        print(Fore.RED)
        print("\n\n\n\n\t\t\t\tBirkaç saniye sonra banka sistemimizden ayrılacaksınız.")
        print(Style.RESET_ALL)
        time.sleep(sleep_time1)
        clear()

        sys.exit()



def intro():

    print(Fore.RED)

    sp("\t\t\t\t**********************")

    sp("\t\t\t\t       ARC BANK")

    sp("\t\t\t\t     HOŞ GELDİNİZ")

    sp("\t\t\t\t**********************")

    print(Style.RESET_ALL)

    sp("\t\tSistemimize girmek için Enter tuşuna basınız.")
    input()
    print("\t\t\tBanka sistemimize giriş yapmaktasınız.")
    time.sleep(1)
    consol_animation()
    begin()


def clear():
    """
        Bu fonksiyon terminal penceresini ilk haline getirir.
    """
    # İşletim Sistemi Windows ise
    if os.name == 'nt':
        _ = os.system('cls')
    # İşletim sistemi Linux veya Mac ise
    else:
        _ = os.system('clear')

def islem_animation():
  clear()
  spin = [ '|', '/', '-', '\\' ]
  
  for i in range(10):
    for b in spin:
      print(Fore.GREEN)
      print(str(b))
      sleep(0.01)
      
      clear()



def consol_animation():
    clear()
    print(Fore.RED)
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |           # %1 #            |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |           # %3 #            |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |           # %7 #            |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |          ## %11 ##          |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |          ## %13 ##          |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |          ## %15 ##          |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |          ## %16 ##          |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |          ## %19 ##          |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |         ### %20 ###         |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |         ### %22 ###         |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |         ### %23 ###         |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |         ### %25 ###         |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |        #### %30 ####        |<<")
    time.sleep(sleep_time)
    clear()
    print(Fore.YELLOW)
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |        #### %35 ####        |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |       ##### %45 #####       |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |     ####### %60 #######     |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |    ######## %75 ########    |<<")
    time.sleep(sleep_time)
    clear()
    print(Fore.GREEN)
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |   ######### %90 #########   |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |   ######### %91 #########   |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |   ######### %92 #########   |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |  ########## %93 ##########  |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |   ######### %94 #########   |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> | ########### %95 ########### |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> | ########### %97 ########### |<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |############ %99 ############|<<")
    time.sleep(sleep_time)
    clear()
    print(
        "          YÖNLENDİRİLİYORSUNUZ >> |############ %100 ###########|<<")
    print(Style.RESET_ALL)
    time.sleep(sleep_time)
    clear()


u = ["dbmstr","1"]
p = ["db1923db","1"]


def begin():
    choice = input(
        "GİRİŞ MENÜSÜ\n1.GİRİŞ\n2.ÇIKIŞ\nBir Opsiyon Seçiniz. (1-2) \n")
    if choice == "1":
        clear()
        login()
    elif choice == "2":
        warning()
    else:
        print("Lütfen geçerli bir opsiyon giriniz.\n")
        begin()


def login():
    clear()
    print("")
    global enter_username
    enter_username = input("Kullanıcı adınızı giriniz:")
    username_check()


def username_check():
    if enter_username in u:
        clear()
        password_check()

    else:
        print("Girdiğiniz kullanıcı adında bir kayıt bulunmamaktadır.\n\n")
        begin()


def password_check():
    global enter_password
    enter_password = input("Şifrenizi giriniz:")
    clear()
    if enter_password in p:
        print(Fore.GREEN)
        sp("Bilgiler doğrulandı.")
        print(Style.RESET_ALL)
        time.sleep(2)
        consol_animation()

    else:
        print("That is the incorrect username or password\n")
        begin()


def writeAccount():

    account = Account()

    account.createAccount()

    writeAccountsFile(account)


def displayAll():

    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        mylist = pickle.load(infile)

        for item in mylist:
            print(Fore.YELLOW)
            print(item.accNo, " | ", item.name, " | ", item.type, " | ",
                  item.deposit)
            print(Style.RESET_ALL)

        infile.close()

    else:
        clear()
        print(Fore.RED)
        print("Gösterelecek bir veri bulunmamaktadır.")
        print(Style.RESET_ALL)


def displaySp(num):

    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        mylist = pickle.load(infile)

        infile.close()

        found = False

        for item in mylist:

            if item.accNo == num:

                print("\tHesabınızdaki para miktarı = ", item.deposit)

                found = True

    else:

        print("Aranacak bir kayıt bulunmamaktadır")

    if not found:

        print("Girdiğiniz numarayla bir kayıt bulunamadı")

mik=0

def depositAndWithdraw(num1, num2):

    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        mylist = pickle.load(infile)

        infile.close()

        os.remove('accounts.data')

        for item in mylist:

            if item.accNo == num1:

                if num2 == 1:
                    clear()
                    amount = int(input("Yatırılacak miktarı giriniz : "))

                    item.deposit += amount
                    islem_animation()
                    print(Fore.GREEN)
                    print("Hesabınız güncellenmiştir.")
                    print(Style.RESET_ALL)

                elif num2 == 2:
                    clear()
                    amount = int(input("Çekilecek miktarı giriniz : "))

                    if amount <= item.deposit:

                        item.deposit -= amount
                        islem_animation()
                        print(Fore.GREEN)
                        print("Hesabınız güncellenmiştir.")
                        print(Style.RESET_ALL)

                    else:

                        print(
                            "Hesabınızda bulunan miktardan daha fazla çekemezsiniz."
                        )

    else:
        clear()
        print("Aranacak bir kayıt bulunmamaktadır.")

    outfile = open('newaccounts.data', 'wb')

    pickle.dump(mylist, outfile)

    outfile.close()

    os.rename('newaccounts.data', 'accounts.data')



def transfer(num1, num2):
  
    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        mylist = pickle.load(infile)

        infile.close()

        os.remove('accounts.data')

        for item in mylist:
           
            if item.accNo == num1:
          
                if num2 == 1:
                    clear()

                    mikv = int(input("Transfer edilecek mikatrı giriniz : "))  

                    item.deposit += mik 
                    islem_animation()
                
                elif num2 == 2:
                     mika = int(input("Doğrulamak için tekarar transfer edilecek mikatrı giriniz : "))
                  

                     if mik <= item.deposit:
                    

                        item.deposit -= mik
                        islem_animation()
                        print(Fore.GREEN)
                        print("Alıcıya para transfer edilmiştir.")
                        print(Style.RESET_ALL)

                else:

                        print(
                            "Hesabınızda bulunan miktardan daha fazla transfer edemezsiniz."
                        )
    else:
        clear()
        print("Girilen hesap numarası bir kayıt bulunmamaktadır.")

    outfile = open('newaccounts.data', 'wb')

    pickle.dump(mylist, outfile)

    outfile.close()

    os.rename('newaccounts.data', 'accounts.data')

def deleteAccount(num):

    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        oldlist = pickle.load(infile)

        infile.close()

        newlist = []

        for item in oldlist:

            if item.accNo != num:

                newlist.append(item)

        os.remove('accounts.data')

        outfile = open('newaccounts.data', 'wb')

        pickle.dump(newlist, outfile)

        outfile.close()

        os.rename('newaccounts.data', 'accounts.data')


def modifyAccount(num):

    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        oldlist = pickle.load(infile)

        infile.close()

        os.remove('accounts.data')

        for item in oldlist:

            if item.accNo == num:
                clear()
                item.name = input("Hesap sahibinin adını giriniz : ")

                item.type = input("Hesap birimini giriniz : ")

                item.deposit = int(
                    input("Açılacak hesaba yatırılacak miktarı giriniz : "))

        outfile = open('newaccounts.data', 'wb')

        pickle.dump(oldlist, outfile)

        outfile.close()

        os.rename('newaccounts.data', 'accounts.data')
        

def writeAccountsFile(account):

    file = pathlib.Path("accounts.data")

    if file.exists():

        infile = open('accounts.data', 'rb')

        oldlist = pickle.load(infile)

        oldlist.append(account)

        infile.close()

        os.remove('accounts.data')

    else:

        oldlist = [account]

    outfile = open('newaccounts.data', 'wb')

    pickle.dump(oldlist, outfile)

    outfile.close()

    os.rename('newaccounts.data', 'accounts.data')


# kodun başlangıç kısmı

ch = ''

num = 0

intro()

while ch != 9:

    #system("cls");
    #clear()
    print("\n\n\tANA MENÜ")

    print("\t1. YENİ HESAP")

    print("\t2. YATIRILACAK MİKTAR")

    print("\t3. ÇEKİLECEK MİKTAR")

    print("\t4. HESAP SORGULAMA")

    print("\t5. HESAP LİSTELERİ")

    print("\t6. HESAP KAPATMA")

    print("\t7. HESAP DÜZENLEME")

    print("\t8. TRANSFER",Fore.RED, "#Beta sürecinde#",Style.RESET_ALL)

    print("\t9. GERİ")
        
    print("\t0. ÇIKIŞ")

    print("\tBir Opsiyon Seçiniz. (0-9) ")

    ch = input()

    #system("cls");

    if ch == '1':
        clear()
        writeAccount()

    elif ch == '2':
        clear()
        num = int(input("\tHesap numaranızı giriniz : "))

        depositAndWithdraw(num, 1)

    elif ch == '3':
        clear()
        num = int(input("\tHesap numaranızı giriniz : "))

        depositAndWithdraw(num, 2)

    elif ch == '4':
        clear()
        num = int(input("\tHesap numaranızı giriniz : "))
        consol_animation()
        displaySp(num)

    elif ch == '5':
        clear()
        consol_animation()
        displayAll()

    elif ch == '6':
        clear()
        sp("Hesap Listeleri:")
        displayAll()
        num = int(input("\nHesap numaranızı giriniz : "))
        islem_animation()
        print(Fore.GREEN)
        print("\t", num, "numaralı hesap silinmiştir.")
        print(Style.RESET_ALL)
        deleteAccount(num)

    elif ch == '7':
        clear()
        num = int(input("\tHesap numaranızı giriniz : "))

        modifyAccount(num)

    elif ch == '8':
      clear()
      displayAll()
      hesapv = int(input("Verici hesap numaranızı giriniz : "))
      transfer(hesapv , 2)
      print(Style.RESET_ALL)
      

      clear()
      hesapa = int(input("\tAlıcı hesap numaranızı giriniz : "))
      transfer(hesapa , 1)
      displayAll()
      #print(Fore.RED,"Yatırılacak miktar 0'dan büyük olmalı.",Style.RESET_ALL)

      
    elif ch == '9':
        clear()
        print(Fore.RED)
        print("\tGeri dönülüyor.")
        print(Style.RESET_ALL)
        consol_animation()

    elif ch == '0':
        clear()
        print("\tBizi tercih ettiğiniz için teşekkürler.")
        clear()
        warning()