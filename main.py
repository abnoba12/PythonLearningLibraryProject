from library.utils import operations

def main_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter year: "))
            operations.create_book(title, author, year)
        elif choice == '2':
            books = operations.read_books()
            print("\n\r")
            for book in books:
                book.display()
        elif choice == '3':
            old_title = input("Enter the title of the book to update: ")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_year = int(input("Enter new year: "))
            operations.update_book(old_title, new_title, new_author, new_year)
        elif choice == '4':
            title = input("Enter the title of the book to delete: ")
            operations.delete_book(title)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main_menu()
