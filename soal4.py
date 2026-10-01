books = {}

while True:
    command = input("Enter command:    1-add\n 2-search\n 3-show\n 4-exit ")

    if command == "add":
        book = input("Book name: ")
        author = input("Author: ")
        books[book] = author

    elif command == "search":
        book = input("Book name: ")

        if book in books:
            print(books[book])
        else:
            print("Book not found")

    elif command == "show":
        for book, author in books.items():
            print(book, "-", author)

    elif command == "exit":
        break