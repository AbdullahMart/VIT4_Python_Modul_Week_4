import json
import os

# Dosya adını sabit bir değişkene atayarak kodun her yerinde kullanımını kolaylaştırıyoruz.
BOOKS_FILE = "books.json"

# Kitapları yüklemek için dosyayı kontrol eden bir fonksiyon.
def load_books():
    # Eğer dosya yoksa, boş bir liste oluşturup dosyaya yazıyoruz.
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w",encoding="utf-8") as f:
            json.dump([], f)
    # Dosyayı okuyup içeriği JSON formatında döndürüyoruz.
    with open(BOOKS_FILE, "r",encoding="utf-8") as f:
        return json.load(f)

# Kitapları kaydetmek için dosyaya yazan bir fonksiyon.
def save_books(books):
    # Kitap listesini JSON formatında dosyaya yazıyoruz.
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

# Yeni bir kitap ekleyen fonksiyon.
def add_book():
    # Mevcut kitapları yüklüyoruz.
    books = load_books()
    # Kullanıcıdan kitap bilgilerini alıyoruz.
    Barcode = int(input("Enter the Barcode: "))
    Language = input("Enter the Language: ")
    Price = float(input("Enter the Price: "))
    Book_Name = input("Enter the book name: ")
    Publisher = input("Enter the Publisher: ")
    Author = input("Enter the Author: ")

    # Yeni kitabı oluşturup listeye ekliyoruz.
    new_book = {
        "Barcode": Barcode,
        "Language": Language,
        "Price": Price,
        "Book_Name": Book_Name,
        "Publisher": Publisher,
        "Author": Author
    }
    books.append(new_book)
    # Güncellenmiş kitap listesini kaydediyoruz.
    save_books(books)
    print("Book added successfully.")

# Bir kitabı silen fonksiyon.
def delete_book():
    books = load_books()
    Barcode = int(input("Enter the Barcode of the book to delete: "))

    for book in books:
        if book["Barcode"] == Barcode:
            # Kitabı listeden kaldırıyoruz.
            books.remove(book)
            # Güncellenmiş kitap listesini kaydediyoruz.
            save_books(books)
            print("Book deleted successfully.")
            return

    print("Book not found.")

# Bir kitabı arayan fonksiyon.
def search_book():
    books = load_books()
    Barcode = int(input("Enter the Barcode of the book to search: "))

    for book in books:
        if book["Barcode"] == Barcode:
            # Kitabı bulup ekrana yazdırıyoruz.
            print("Book found:")
            print(book)
            return

    print("Book not found.")

# Bir kitabı güncelleyen fonksiyon.
def update_book():
    books = load_books()
    Barcode = int(input("Enter the Barcode of the book to update: "))

    for book in books:
        if book["Barcode"] == Barcode:
            print("Enter new information (leave blank to keep unchanged):")
            Language = input("Enter the new Language: ")
            if Language:
                book["Language"] = Language
            Price = float(input("Enter the new Price: "))
            if Price:
                book["Price"] = Price
            Book_Name = input("Enter the new book name: ")
            if Book_Name:
                book["Book_Name"] = Book_Name
            Publisher = input("Enter the new Publisher: ")
            if Publisher:
                book["Publisher"] = Publisher
            Author = input("Enter the new Author: ")
            if Author:
                book["Author"] = Author

            # Güncellenmiş kitap listesini kaydediyoruz.
            save_books(books)
            print("Book updated successfully.")
            return

    print("Book not found.")

# Kitaplari listeleyen fonksiyon.
def list_of_books():
    books = load_books()
    print("List of Books:")
    for book in books:
        print("Barcode:", book["Barcode"])
        print("Language:", book["Language"])
        print("Price:", book["Price"])
        print("Book Name:", book["Book_Name"])
        print("Publisher:", book["Publisher"])
        print("Author:", book["Author"])
        print()  # Boş bir satır ekleyerek kitaplar arasında boşluk bırakıyoruz.

# Kitap işlemlerinin yapıldığı menüyü gösteren fonksiyon.
def book_menu():
    while True:
        print("\nBook Transactions Menu:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Return to Main Menu")
        choice = input("Enter your choice: ")

        # Kullanıcının seçimine göre ilgili fonksiyonu çağırıyoruz.
        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    book_menu()
   
