print("\nWelcome To Your Personal Library Manager!")   

# books list
books = [
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publication_year": 2015,
        "genre": "Programming",
        "read_status": "Read"
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publication_year": 2015,
        "genre": "Programming",
        "read_status": "Unread"
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publication_year": 2008,
        "genre": "Software Development",
        "read_status": "Read"
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "publication_year": 1999,
        "genre": "Software Engineering",
        "read_status": "Unread"
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publication_year": 2015,
        "genre": "Programming",
        "read_status": "Reading"
    }
]

# menu options
options = ["\n1. Add a book", "2. Remove a book", "3. Search for a book", "4. Display all books", "5. Display statistics", "6. Exit"]

condition = True

while condition:
    score = 0
    total = len(books)
    print("\nWhat would you like to do?")

    for option in options:
        print(option)

    user_input = input("\nEnter your choice:  ")

# add book
    if user_input == "1" or user_input == "add a book":
        user_title = input("\nEnter the book title: ").strip()

        user_author = input("\nEnter the author: ").strip()
        while user_author.isdigit():
            print("Author name can't be a number. Please enter a valid name.")
            user_author = input("\nEnter the author: ").strip()

        user_year = input("\nEnter the publication year: ").strip()     
        while user_year.isalpha():
            print("Please enter year in digits.")
            user_year = input("Enter the publication year: ").strip()

        user_genre = input("\nEnter the genre: ").strip()

        read_status = ['read', 'unread', 'reading']
        user_read = input("\nHave you read this book? (Read/Unread/Reading): ").lower()
        while user_read not in  read_status:
            print("\nPlease enter one of this (Read or Unread or Reading).")
            user_read = input("\nHave you read this book? (Read/Unread/Reading): ").lower()

        books.append(dict(title = user_title, author = user_author, publication_year = int(user_year), genre = user_genre, read_status = user_read))
        print(f"\nBook '{user_title}' added successfully!")

# remove book
    elif user_input == "2" or user_input == "remove a book":
        remove_book = input("\nEnter the book title: ").strip().lower()
        found = False
        for book in books[:]:
            if remove_book == book['title'].lower():
                books.remove(book)
                print(f"Book '{remove_book.title()}' removed successfully!")
                found = True
                break
        if not found:
            print(f"The book '{remove_book}' does not exist in your library.")

# search book         
    elif user_input == "3" or user_input == "search for a book":
        print("\nSearch by:\n 1. Title\n 2. Author")
        search_by = input("\nEnter your choice: ").lower()

        valid_choices = ['1', 'title', '2', 'author']

        while search_by not in valid_choices:
            print("Please search by valid choice.")
            search_by = input("\nEnter your search: ").lower()

        if search_by == "1" or search_by.lower() == "title":
            search_title = input("\nEnter the title: ").lower()
            found = False
            for book in books:
                if search_title in book["title"].lower():
                    print(f"\nMatching Books:\n {book['title']} by '{book['author']}' ({book['publication_year']}) - {book['genre']} - {book['read_status']}")
                    found = True
            if not found:
                print(f"The book title '{search_title}' does not exist in your library.")

        elif search_by == "2" or search_by == "author":
            search_author = input("Enter the author: ").lower()
            found = False
            for book in books:
                if search_author in book["author"].lower():
                    print(f"\nMatching Books:\n {book['title']} by '{book['author']}' ({book['publication_year']}) - {book['genre']} - {book['read_status']}")
                    found = True
            if not found:
                print(f"No book found by '{search_author}'.")

# display all books
    elif user_input == "4" or user_input == "display all books":
        if books:
            print("\nHere is Your Library:")
            for index, book in enumerate(books, start=1):
                print(f"\n{index}. {book['title']} by '{book['author']}' ({book['publication_year']}) - {book['genre']} - {book['read_status']}")
        else:
            print("Your library is empty.")

# display library stats
    elif user_input == "5" or user_input == "display statistics":
        for book in books:
            if book['read_status'].lower() == 'read':
                score += 1
        percentage_read = (score / total) * 100
        print(f"""\nYour Library Stats:\n
Total books: {len(books)}
Percentage read: {percentage_read:.2f}%""")

# exit
    elif user_input == "6" or user_input == "exit":
        print("\nThank You for using your Personal Library Manager!")
        condition = False

    else:
        print("\nPlease enter a valid choice.")
