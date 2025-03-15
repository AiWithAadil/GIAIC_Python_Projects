import json

Books = []

# add function
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of the book: "))
    genre = input("Enter the genre of the book: ")
    read_or_not = input("Have you read this book? (yes/no): ").strip().lower()
    Books.append({"title": title, "author": author, "year": year, "genre": genre, "read_or_not": read_or_not})

# remove function
def remove_book():
    title = input("Enter the title of the book: ")
    for book in Books:
        if book["title"] == title:
            Books.remove(book)
            print(f"'{title}' has been removed from the library.")
            return
    print("Book not found.")

# search function
def search_book():
    print('''Search by:
          1. By Title
          2. By Author
          ''')
    option = int(input("Enter your choice: "))
    if option == 1:
        title = input("Enter the title of the book: ")
        for book in Books:
            if book["title"].lower() == title.lower():
                print(book)
                return
        print("Book not found.")
    elif option == 2:
        author = input("Enter the author of the book: ")
        for book in Books:
            if book["author"].lower() == author.lower():
                print(book)
                return
        print("No books found by this author.")
    else:
        print("Invalid choice.")

# display books
def display_books():
    if not Books:
        print("No books in the library.")
    else:
        print("Books in the library:")
        for book in Books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {book['read_or_not']}")

# display statistics
def display_statistics():
    total_books = len(Books)
    if total_books == 0:
        print("No books in the library to display statistics.")
        return

    read_books = sum(1 for book in Books if book["read_or_not"] == "yes")
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage of books read: {percentage_read:.2f}%")

# Exit function
def exit_program():
    with open("books.json", "w") as file:
        json.dump(Books, file, indent=4)
    print("Library saved to file. Goodbye!")
    exit()

def library_manager():
    while True:
        print("Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics (total books, percentage read)")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice.")

library_manager()
