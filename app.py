print("\nWelcome To Your Personal Library Manager!")

books = books = [
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

options = ["\n1. Add a book", "2. Remove a book", "3. Search for a book", "4. Display all books", "5. Display statistics", "6. Exit"]

condition = True

while condition:
    score = 0
    total = len(books)
    print("\nWhat would you like to do?")

    for option in options:
        print(option)

    user_input = input("\nEnter your choice:  ")

    if user_input == "1" or user_input.lower() == "Add a book".lower():
        user_title = input("Enter the book title: ")
        user_author = input("Enter the author: ")
        user_year = input("Enter the publication year: ")
        user_genre = input("Enter the genre: ")
        user_read = input("Have you read this book? (Read/Unread/Reading): ") 

        books.append(dict(title = user_title, author = user_author, publication_year = user_year, genre = user_genre, read_status = user_read))
        print("Book added successfully!")

    elif user_input == "2" or user_input.lower() == "Remove a book".lower():
        remove_book = input("Enter the book title: ")
        found = True
        for book in books[:]:
            # title = book["title"]
            if remove_book == book['title']:
                # print(remove_book)
                # print(title)
                books.remove(book)
                print("Book removed successfully!")
                break
        if not found:
            print("This book does not exist in your library.")
                # break

    elif user_input == "3" or user_input.lower() == "Search for a book".lower():
        print("Search by:\n 1. Title\n 2. Author")
        search_by = input("Enter your choice: ")
        if search_by == "1" or search_by == "Title":
            search_title = input("Enter the title: ")
            for book in books:
                title = book["title"]
                if search_title in title:
                    print(f"Matching Books:\n {book['title']} by '{book['author']}' ({book['publication_year']}) - {book['genre']} - {book['read_status']}")
                    # print(search_title)
                    break
                else:
                    print("This book does not exist in your library.")
                    # break

        elif search_by == "2" or search_by == "Author":
            search_author = input("Enter the author: ")
            for book in books:
                author = book["author"]
                if search_author in author:
                    print(f"Matching Books:\n {book['title']} by '{book['author']}' ({book['publication_year']}) - {book['genre']} - {book['read_status']}")
                    # print(search_author)
                    break
                else:
                    print("This book does not exist in your library.")
                    # break
        else:
            print("Please enter a valid search")

    elif user_input == "4" or user_input.lower() == "Display all books".lower():
        if books:
            print("Your Library:")
            for index, book in enumerate(books, start=1):
                print(f"{index}. {book['title']} by '{book['author']}' ({book['publication_year']}) - {book['genre']} - {book['read_status']}")

    elif user_input == "5" or user_input.lower() == "Display statistics".lower():
        for book in books:
            read_status = book['read_status']
            if read_status == 'Read':
                score += 1
        percentage_read = (score / total) * 100
        print(f"""Your Library Stats:
    Total books: {len(books)}
    Percentage read: {percentage_read}%""")

    elif user_input == "6" or user_input.lower() == "Exit".lower():
        condition = False
        print("Goodbye!")

    else:
        print("Please enter a valid choice.")
