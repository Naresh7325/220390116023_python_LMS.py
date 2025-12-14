import os
import json

DATA_FILE = "library_data.json"

USERNAME = "admin"
PASSWORD = "123"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def login():
    attempts = 3
    while attempts > 0:
        print(f"\nAttempt {4 - attempts}:")
        user = input("Username: ")
        pwd = input("Password: ")

        if user == USERNAME and pwd == PASSWORD:
            print("Login successful.")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid credentials. Attempts left: {attempts}")
            else:
                print("Too many failed login attempts. Program terminated.")
                return False


def add_book(books):
    book_id = input("Enter Book ID: ")

    for b in books:
        if b["id"] == book_id:
            print("Duplicate Book ID not allowed.")
            return

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity,
        "price": price,
        "active": True
    }

    books.append(book)
    save_data(books)
    print("Book added successfully.")


def display_books(books):
    active_books = [b for b in books if b["active"]]

    if not active_books:
        print("No active books available.")
        return

    print("\n1. Sort by Book ID")
    print("2. Sort by Book Title")
    choice = input("Choose sorting option: ")

    if choice == "1":
        active_books.sort(key=lambda x: x["id"])
    elif choice == "2":
        active_books.sort(key=lambda x: x["title"])

    print("\nID | Title | Author | Qty | Price")
    print("-" * 40)
    for b in active_books:
        print(f"{b['id']} | {b['title']} | {b['author']} | {b['quantity']} | {b['price']}")


def search_book(books):
    print("\n1. Search by Book ID")
    print("2. Search by Book Title")
    choice = input("Enter choice: ")

    if choice == "1":
        key = input("Enter Book ID: ")
        for b in books:
            if b["id"] == key and b["active"]:
                print(b)
                return
    elif choice == "2":
        key = input("Enter Book Title: ")
        for b in books:
            if b["title"].lower() == key.lower() and b["active"]:
                print(b)
                return

    print("Book not found.")


def issue_book(books):
    book_id = input("Enter Book ID to issue: ")

    for b in books:
        if b["id"] == book_id and b["active"]:
            if b["quantity"] > 0:
                b["quantity"] -= 1
                save_data(books)
                print("Book issued successfully.")
                return
            else:
                print("Book out of stock.")
                return

    print("Book not found.")


def return_book(books):
    book_id = input("Enter Book ID to return: ")

    for b in books:
        if b["id"] == book_id and b["active"]:
            b["quantity"] += 1
            save_data(books)
            print("Book returned successfully.")
            return

    print("Book not found.")


def delete_book(books):
    print("\n1. Delete by Book ID")
    print("2. Delete by Book Title")
    choice = input("Enter choice: ")

    if choice == "1":
        key = input("Enter Book ID: ")
        for b in books:
            if b["id"] == key and b["active"]:
                b["active"] = False
                save_data(books)
                print("Book deleted logically.")
                return

    elif choice == "2":
        key = input("Enter Book Title: ")
        for b in books:
            if b["title"].lower() == key.lower() and b["active"]:
                b["active"] = False
                save_data(books)
                print("Book deleted logically.")
                return

    print("Book not found.")

def main_menu():
    books = load_data()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            print("Program terminated safely.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    if login():
        main_menu()

