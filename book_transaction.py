import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as f:
            json.dump([], f)
    with open(BOOKS_FILE, "r") as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

def add_book():
    books = load_books()
    Barcode = input("Enter the Barcode: ")
    Language = input("Enter the Language: ")
    Price = input("Enter the Price: ")
    Book_Name = input("Enter the book name: ")
    Publisher = input("Enter the Publisher: ")
    Author = input("Enter the Author: ")

    new_book = {
        "Barcode": Barcode,
        "Language": Language,
        "Price": Price,
        "Book_Name": Book_Name,
        "Publisher": Publisher,
        "Author": Author
    }
    books.append(new_book)
    save_books(books)
    print("Book added successfully.")

def delete_book():
    books = load_books()
    Barcode = input("Enter the Barcode of the book to delete: ")

    for book in books:
        if book["Barcode"] == Barcode:
            books.remove(book)
            save_books(books)
            print("Book deleted successfully.")
            return

    print("Book not found.")

def search_book():
    books = load_books()
    Barcode = input("Enter the Barcode of the book to search: ")

    for book in books:
        if book["Barcode"] == Barcode:
            print("Book found:")
            print(book)
            return

    print("Book not found.")

def update_book():
    books = load_books()
    Barcode = input("Enter the Barcode of the book to update: ")

    for book in books:
        if book["Barcode"] == Barcode:
            print("Enter new information (leave blank to keep unchanged):")
            Language = input("Enter the new Language: ")
            if Language:
                book["Language"] = Language
            Price = input("Enter the new Price: ")
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

            save_books(books)
            print("Book updated successfully.")
            return

    print("Book not found.")

def book_menu():
    while True:
        print("\nBook Transactions Menu:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Return to Main Menu")
        choice = input("Enter your choice: ")

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

