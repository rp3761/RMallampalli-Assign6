import sqlite3

connect = sqlite3.connect("bookstore.db")
cursor = connect.cursor()

print("Welcome to Richa's Bookstore!")
print("Please search, look through, and interact with some of Richa's favorite books.")

while True:
    print("\n--- Bookstore Menu ---")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. View cheapest book within a genre")
    print("9. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cursor.execute("SELECT * FROM category")
        for row in cursor.fetchall():
            print(row)

    elif choice == "2":
        cursor.execute("SELECT * FROM book")
        for row in cursor.fetchall():
            print(row)

    elif choice == "3":
        category_name = input("Enter category name: ")
        cursor.execute(
            "SELECT * FROM book JOIN category ON book.categoryId = category.categoryId WHERE categoryName = ?",
            (category_name,)
        )
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)
        else:
            print("No books found in that category.")

    elif choice == "4":
        keyword = input("Enter title keyword: ")
        cursor.execute(
            "SELECT * FROM book WHERE title LIKE '%' || ? || '%'",
            (keyword,)
        )
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)
        else:
            print("No books found with that title keyword.")

    elif choice == "5":
        category_name = input("Category Name: ")
        cursor.execute(
            "SELECT categoryId FROM category WHERE categoryName = ?",
            (category_name,)
        )
        result = cursor.fetchone()
        if result is None:
            print("Category not found.")
        else:
            category_id = result[0]
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            if not isbn.isdigit():
                print("ISBN must be a number.")
                continue
            price = input("Price: ")
            try:
                price = float(price)
                if price < 0:
                    print("Price cannot be negative.")
                    continue
            except ValueError:
                print("Price must be a valid number.")
                continue
            image = input("Image filename: ")
            read_now = input("Read now (0 or 1): ")
            if read_now not in ("0", "1"):
                print("Read now must be 0 or 1.")
                continue
            try:
                cursor.execute(
                    "INSERT INTO book (categoryId, title, author, isbn, price, image, readNow) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (category_id, title, author, int(isbn), price, image, int(read_now))
                )
                connect.commit()
                print("Confirmation: Book has been added!")
            except sqlite3.IntegrityError as e:
                print("Could not add book:", e)

    elif choice == "6":
        book_id = input("Enter book ID: ")
        if not book_id.isdigit():
            print("Book ID must be a number.")
            continue
        new_price = input("Enter new price: ")
        try:
            new_price = float(new_price)
            if new_price < 0:
                print("Price cannot be negative.")
                continue
        except ValueError:
            print("Price must be a valid number.")
            continue
        cursor.execute(
            "UPDATE book SET price = ? WHERE bookId = ?",
            (new_price, int(book_id))
        )
        connect.commit()
        if cursor.rowcount == 0:
            print("No book found with that ID.")
        else:
            print("Confirmation: Price updated!")

    elif choice == "7":
        book_id = input("Enter book ID: ")
        if not book_id.isdigit():
            print("Book ID must be a number.")
            continue
        cursor.execute(
            "DELETE FROM book WHERE bookId = ?",
            (int(book_id),)
        )
        connect.commit()

        if cursor.rowcount == 0:
            print("No book found with that ID.")
        else:
            print("Confirmation: Book has been deleted!")

    elif choice == "8":
        categoryName = input("Enter a genre: ")
        cursor.execute(
            "SELECT * FROM book JOIN category ON book.categoryId = category.categoryId WHERE categoryName = ? ORDER BY price ASC LIMIT 1",
            (categoryName,)
        )
        result = cursor.fetchone()

        if result:
            print(result)
        else:
            print("No books found in that genre.")

    elif choice == "9":
        break
    
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")

connect.close()
print("Goodbye!")
