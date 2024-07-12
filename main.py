# Answers to Lesson 5
from library.data_operations.book_operations import InvalidYearError, add_book, remove_book, update_book_year, list_books, find_book_by_title, print_book_details, check_book_year

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book Year")
        print("4. List Books")
        print("5. Find Book by Title")
        print("6. Print Book Details")
        print("7. Check Book Year")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book year: "))
            print(add_book(books, title, author, year))
        elif choice == '2':
            title = input("Enter book title to remove: ")
            print(remove_book(books, title))
        elif choice == '3':
            title = input("Enter book title to update: ")
            new_year = int(input("Enter new year: "))
            print(update_book_year(books, title, new_year))
        elif choice == '4':
            print("List of books:")
            for title in list_books(books):
                print(title)
        elif choice == '5':
            title = input("Enter book title to find: ")
            book = find_book_by_title(books, title)
            if book:
                print(f"Found book: {book}")
            else:
                print("Book not found")
        elif choice == '6':
            print("Printing all book details:")
            print_book_details(books)
        elif choice == '7':
            title = input("Enter book title to check year: ")
            book = find_book_by_title(books, title)
            if book:
                try:
                    print(check_book_year(book))
                except InvalidYearError as e:
                    print(f"Error: {e}")
            else:
                print("Book not found")
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()
