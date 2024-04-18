#Kitap işlemleri dosyasını çekiyor.
import book_transaction 

#üye işlemleri dosyasını çekiyor.
import member_transaction

#json kütüphanesi
import json

#time dosyasını çekiyor.
import time
import datetime


while True:
    try: # try hata ayıklama için kullanıyor.
        print("""
    |===========Library  Management System=====[-][o][x]
    |            P U B L İ C   L İ B R A R Y           |
    |                 W  E  L  K  O  M                 |
    |                                                  |
    |   1- MEMBER TRANSACTİONS => 1                    |
    |   2- BOOK TRANSACTİONS ===> 2                    |
    |   3- EXİT ================> 0                    | 
    |                                                  |       
    |       copyright@vit4 group2  version 1.04        |
    |==================================================| """)
        #Kullanıcıdan ana menü için seçim yapması isteniyor.
        main_menu_choise= input("Please make a selection:")

        #Kullanıcı üye işlemlerine giriyor.
        if main_menu_choise == "1":

            print("""
    |===========Library  Management System=======[-][o][x]
    |         M E M B E R   T R A N S A C T İ O N        |
    |                 W  E  L  K  O  M                   |
    |                                                    |
    |   1- MEMBERS ======>1   |  5- BOOK LOADİNG=====>5  |
    |   2- ADD MEMBER====>2   |  6- BOOK RETURN======>6  | 
    |   3- SEARCH MEMBER=>3   |  7- BOOK TRACKING====>7  |
    |   4- DELETE MEMBER=>4   |  8- EXİT ============>0  | 
    |                                                    | 
    |                  version 1.04                      |       
    |              copyright@vit4 group2                 |
    |====================================================| """)

            #Kullanıcıya üye işlemleri için seçim yaptırılıyor.
            menu_member_transaction= input("Please make a selection:")

            #Kayıtlı tüm üye listesini sıralıyor.
            if menu_member_transaction=="1": 
                member_transaction.members()

            #Üye ekle fonsiyonunu çekiyoruz.(Üye işlemlerinde tanımlı)
            elif menu_member_transaction=="2":
                member_transaction.add_member()
                
             #Üye arama fonsiyonunu çekiyoruz.(Üye işlemlerinde tanımlı)
            elif menu_member_transaction=="3":
                member_transaction.search_member()

            #Üye silme fonsiyonunu çekiyoruz.(Üye işlemlerinde tanımlı)
            elif menu_member_transaction== "4":
                member_transaction.delete_member()

            #Kitap ödünç verme fonksiyonunu çekiyoruz.(Üye işlemlerinde tanımlı)
            elif menu_member_transaction=="5":
                member_transaction.borrow_book()

            # Kitap iade verme fonsiyonunu çekiyoruz.(Üye işlemlerinde tanımlı)
            elif menu_member_transaction=="6":
                member_transaction.return_book()

            #Kitap takibi fonsiyonunu çekiyoruz.(Üye işlemlerinde tanımlı)
            elif menu_member_transaction == "7":
                member_transaction.book_tracking()

            # Üye  işlemlerinden çıkış yapıyoruz.
            elif menu_member_transaction =="0": 
                print("You are logged out of member transactions")
                break

            # Yanlış değer girdiği için tekrar seçim yapılması isteniyor.
            else:
                print("Invalid selection! Please make a valid choice.") 

        #Kullanıcı Kitap işlemleri menüsüne giriyor.   
        elif main_menu_choise == "2": 

            print("""
    |=========Library  Management System=======[-][o][x]
    |           B O O K   T R A N S A C T İ O N        |
    |                 W  E  L  K  O  M                 |
    |                                                  |
    |   1- BOOKS =========>1    5- EXİT=====>0         |
    |   2- ADD BOOK=======>2                           | 
    |   3- SEARCH BOOK ===>3                           |
    |   4- DELETE BOOK ===>4                           | 
    |                                                  | 
    |               version 1.04                       |       
    |           copyright@vit4 group2                  |
    |==================================================| """)

            #Kullanıcıdan menü için seçim yaptırılıyor.
            menu_book_transactioni= input("Please make a selection:") 

            #Bütün kitap listesini çağırıyoruz.(Kitap işlemlerinde tanımlı)
            if menu_book_transactioni=="1":
                book_transaction.list_of_books()

            #Kitap ekleme fonsiyonunu çağırıyoruz.(Kitap işlemlerinde tanımlı)
            elif menu_book_transactioni=="2":
                book_transaction.add_book()

            #Kitap arama Fonsiyonunu çağırıyoruz.(Kitap işlemlerinde tanımlı)
            elif menu_book_transactioni=="3":
                book_transaction.search_book()

            #Kitap silme fonksiyonunu çağırıyoruz.(Kitap işlemlerinde tanımlı)
            elif menu_book_transactioni== "4":
                book_transaction.delete_book()

            # Kitap işlemleri Çıkış 
            elif menu_book_transactioni =="0":
                print("You are logged out of book transactions")
                break
            #Kitap işlemleri menüsündeyYanlış değer girdiği için tekrar seçim yapılması isteniyor.
            else:
                print("Invalid selection! Please make a valid choice.")
        
        # Ana menü çıkış
        elif main_menu_choise == "0":

            print("Cikis yaptiniz.")
            print("Tekrar Kütüphanemize bekleriz..")
            break
        
        # ana menüye yanlış değer girildiğinde seçimin düzeltilmesi isteniyor.
        else:
            print("Invalid selection! Please make a valid choice.")

    #programda istisna hata oluştuğunda devreye giriyor.
    except Exception as mistake: 
        print("Error: ",mistake, end="\n\n")


    