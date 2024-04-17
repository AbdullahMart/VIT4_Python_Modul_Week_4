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
    barcode = input("Enter the barcode: ")
    language = input("Enter the language: ")
    price = input("Enter the price: ")
    book_name = input("Enter the book name: ")
    publisher = input("Enter the publisher: ")
    author = input("Enter the author: ")

    new_book = {
        "barcode": barcode,
        "language": language,
        "price": price,
        "book_name": book_name,
        "publisher": publisher,
        "author": author
    }
    books.append(new_book)
    save_books(books)
    print("Book added successfully.")

def delete_book():
    books = load_books()
    barcode = input("Enter the barcode of the book to delete: ")

    for book in books:
        if book["barcode"] == barcode:
            books.remove(book)
            save_books(books)
            print("Book deleted successfully.")
            return

    print("Book not found.")

def search_book():
    books = load_books()
    barcode = input("Enter the barcode of the book to search: ")

    for book in books:
        if book["barcode"] == barcode:
            print("Book found:")
            print(book)
            return

    print("Book not found.")

def update_book():
    books = load_books()
    barcode = input("Enter the barcode of the book to update: ")

    for book in books:
        if book["barcode"] == barcode:
            print("Enter new information (leave blank to keep unchanged):")
            language = input("Enter the new language: ")
            if language:
                book["language"] = language
            price = input("Enter the new price: ")
            if price:
                book["price"] = price
            book_name = input("Enter the new book name: ")
            if book_name:
                book["book_name"] = book_name
            publisher = input("Enter the new publisher: ")
            if publisher:
                book["publishing_house"] = publisher
            author = input("Enter the new author: ")
            if author:
                book["author"] = author

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

