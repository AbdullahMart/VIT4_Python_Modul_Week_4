import kitap_işlemleri
import uye_işlemleri
import json
import zaman


while True:
    try:
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

        main_menu_choise= input("Please make a selection:")

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
            menu_member_transaction= input("Please make a selection:")

            if menu_member_transaction=="1":
                pass

            elif menu_member_transaction=="2":
                uye_ekle(Uye_Adi,Tel,Adres)

            elif menu_member_transaction=="3":
                uye_ara(arama)

            elif menu_member_transaction== "4":
                uye_sil(silinecek_uye)

            elif menu_member_transaction=="5":
                kitap_odunc_verme()

            elif menu_member_transaction=="6":
                kitap_iade()

            elif menu_member_transaction == "7":
                pass
            elif menu_member_transaction =="0":
                print("You are logged out of member transactions")
                break
            else:
                print("Invalid selection! Please make a valid choice.")

            
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

            menu_book_transactioni= input("Please make a selection:")
            
            if menu_book_transactioni=="1":
                pass

            elif menu_book_transactioni=="2":
                kitap_ekle(Kitap_Adi, Yazar, Yayinevi, Barkod)

            elif menu_book_transactioni=="3":
                kitap_arama(arama)
            
            elif menu_book_transactioni== "4":
                kitap_sil(silinecek_veri)

            elif menu_book_transactioni =="0":
                print("You are logged out of book transactions")
                break

            else:
                print("Invalid selection! Please make a valid choice.")
        
        elif main_menu_choise == "0":

            print("Cikis yaptiniz.")
            print("Tekrar Kütüphanemize bekleriz..")
            break

        else:
            print("Invalid selection! Please make a valid choice.")


    except Exception as mistake:
        print("Error: ",mistake, end="\n\n")


    