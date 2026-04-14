#Richa Mallampalli - Assignment 6

#Intro & Short Description
Hi! I'm Richa Mallampalli, and I've created a bookstore for you to enjoy!
I've included some of my favorite books like The Selection, Harry Potter, and Magpie Murders, along with books on my reading list, such as Murder on the Orient Express!

The genres included are Fantasy, Romance, Science Fiction, Historical Fiction, and Mystery.
Users are able to view, search, add, and delete books, as well as view the cheapest book in a selected genre.

This project creates a bookstore database using SQLite and then utilizes Python to interact with it through a command line interface (CLI).

#Files
In order to create the database, you will need to utilize createTables.sql which creates all of the database tables, and insertRows.sql which inserts all of the data into the database.
The other files in this project are bookstore.db which is the database that is created after running the SQL files, and bookstore_cli.py which is the Python program that performs CRUD operations.

#Instructions to create the database
Open the terminal, and run:
sqlite3 bookstore.db < createTables.sql
sqlite3 bookstore.db < insertRows.sql

If the database file does not exist already, it will be created automatically. These commands will create the database, create the tables, and insert data into them.

#Instructions to run the Python program
After creating the database, run the following line in the terminal to run the Python CLI to interact with the SQLite database:
python3 bookstore_cli.py

#General Notes
1. The CLI supports the following features: View all categories, View all books, View books by category, Search books by title, Add new books, Update book prices, Delete books, View the cheapest book in a genre, and Quit.
2. The project utilizes parameterized queries in Python
3. In the image field, only the filename is stored, not the actual file.

