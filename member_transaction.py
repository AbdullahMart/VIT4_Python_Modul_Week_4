import book_transaction
import json
import os



def open_member_file():
    if os.path.exists("member.json"):
        with open("member.json", "r") as members_file:
            try:
                members = json.load(members_file)
            except json.decoder.JSONDecodeError:
                members = []
    else:
        members = []
    return members


def members():
    members = open_member_file()

    for member in members:
        print("id:", member["id"], "Member name:", member["Member name"])


def update_member():
    id = int(input("Please enter the id number of the member you want to update:"))
    members = open_member_file()
    for member in members:
        if member["id"] == id:
            new_member_name = input("Please enter the updated member name: ")
            new_member_address = input("Please enter the updated member address: ")
            new_phone_number = input("Please enter the updated phone number of the member: ")
            member["Member name"] = new_member_name
            member["Tel"] = new_phone_number
            member["Address"] = new_member_address
            save_member(members)


def member_check(members, id):
    for member in members:
        if member["id"] == id:
            return True
    else:
        return False


def save_member(members):
    with open("member.json", "w") as members_file:
        json.dump(members, members_file, indent=4)
        print("Successfully updated.")


def add_member():
    members = open_member_file()
    id = int(input("Enter an ID number: "))
    if member_check(members, id):
        print(f"{id} id number already exists in the system.")
        return

    member_name = input("Please enter the member name: ")
    member_address = input("Please enter the member address: ")
    phone_number = input("Please enter the phone number of the member: ")

    new_member = {"id": id, "Member name": member_name, "Tel": phone_number, "Address": member_address}
    members.append(new_member)

    save_member(members)


def search_member():
    members = open_member_file()
    try:
        search_member_id = int(input("Enter the id number of the member you want to search:"))
    except ValueError:
        print("Please enter a valid integer for the member ID.")
        return search_member()

    for member in members:
        if member["id"] == search_member_id:
            print("Information of the member you are searching for:", member)
            return
    else:
        print("Cannot find the id you are searching for.")
        return search_member()

def delete_member():
    members = open_member_file()

    try:
        member_to_delete = int(input("Please enter the id you want to delete:"))
    except ValueError:
        print("Please enter a valid integer for the member ID.")
        return delete_member()


    for member in members:
        if member["id"] == member_to_delete:
            members.remove(member)
    save_member(members)
    print(f"Member with id {member_to_delete} has been successfully deleted.")


def borrow_book():
    while True:
        book_borrow_choice = input("Which book do you want to borrow (Press 0 to go back to the main page):")
        if book_borrow_choice == "0":
            return  # Return to the main page

        with open("book.json", "r", encoding="utf-8") as file:
            books = json.load(file)

        book_found = False
        for book in books:
            if book["book_name"] == book_borrow_choice:
                book_found = True
                break

        if not book_found:
            print("Book not found. Please try again.")
            continue

        while True:
            try:
                id = int(input("Please enter your id number:"))
                members = open_member_file()
                for member in members:
                    if member["id"] == id:
                        track = read_track()
                        track.append({"Member": member, "Book": book, "borrow_date": current_time(),
                                      "return_date": fourteen_days_later()})
                        write_track(track)

                        new_books = [k for k in books if k["book_name"] != book_borrow_choice]
                        record(new_books)
                        print("Book borrowed successfully.")
                        return
                else:
                    print("This member cannot be found. Please try again.")
            except ValueError:
                print("Please enter a valid ID number.")


def write_track(track):
    for loan in track:
        loan["borrow_date"] = datetime.strptime(loan["borrow_date"], "%Y-%m-%d").strftime("%Y-%m-%d")
        loan["return_date"] = datetime.strptime(loan["return_date"], "%Y-%m-%d").strftime("%Y-%m-%d")

    with open("track.json", "w") as track_file:
        json.dump(track, track_file, indent=4)
        print("Successfully updated.")


def read_track():
    if os.path.exists("track.json"):
        with open("track.json", "r") as track_file:
            try:
                track = json.load(track_file)
            except json.decoder.JSONDecodeError:
                track = []
    else:
        track = []
    return track


def return_book():
    members = open_member_file()
    try:
        id = int(input("Please enter your id number:"))
    except ValueError:
        print("Please enter a valid integer for the member ID.")
        return return_book()


    while True:

        if member_check(members, id):
            print("Thank you for logging in..")
            break
        if not member_check(members, id):
            print("No member found with this id number")
            return return_book()

    track_file = read_track()
    n = 0

    for loan in track_file:
        if loan["Member"]["id"] == id:
            n += 1
            print("Books in your possession:")
            print("-" * 30)
            book_info = loan["Book"]
            print(
                f"Book in your possession: Book Title: {book_info['book_name']} - Author: {book_info['author']} - Publisher: {book_info['publisher']}")
            print("-" * 30)

    while True:
        return_book_name = input("Which book would you like to return:\nPress 0 to go back. ")
        if return_book_name == "0":
            return
        for loan in track_file:
            if loan["Member"]["id"] == id and loan["Book"]["book_name"].lower() == return_book_name.lower():
                books = read()
                books.append(loan["Book"])
                track_file.remove(loan)
                record(books)
                write_track(track_file)
                print(f"{return_book_name} book has been successfully returned.")
                return
        else:
            print("The book you entered does not appear to be in your possession.")
            continue


def book_tracking():
    members = open_member_file()
    try:
        id = int(input("Please enter your id number:"))
    except ValueError:
        print("Please enter a valid integer for the member ID.")
        return book_tracking()



    while True:

        if member_check(members, id):
            print("Thank you for logging in..")
            break
        if not member_check(members, id):
            print("No member found with this id number")
            return book_tracking()

    track_file = read_track()
    n = 0
    for loan in track_file:
        if loan["Member"]["id"] == id:
            n += 1
            print("-" * 30)
            book_info = loan["Book"]
            print(
                f"Books in your possession: Book Title: {book_info['book_name']} - Author: {book_info['author']} - Publisher: {book_info['publisher']}")
            print("-" * 30)
        else:
            print("The book you borrowed does not exist.")
            return


if __name__ == "__main__":
    pass