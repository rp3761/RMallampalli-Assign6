PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage)
VALUES (1, 'Fantasy', 'fantasy_category.jpg'),
(2, 'Romance', 'romance_category.jpg'),
(3, 'Science Fiction', 'science_fiction_category.jpg'),
(4, 'Historical Fiction', 'historical_fiction_category.jpg'),
(5, 'Mystery', 'mystery_category.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Harry Potter and the Half-Blood Prince', 'J.K. Rowling', 9780439785969, 13.00, 'hp6.jpg', 1),
(2, 1, 'The Fellowship of the Ring', 'J.R.R. Tolkien', 9780547928210, 11.00, 'lotr1.jpg', 0),
(3, 1, 'A Game of Thrones: A Song of Ice and Fire', 'George R.R. Martin', 9780553593716, 20.00, 'got1.jpg', 1),
(4, 2, 'Pride and Prejudice', 'Jane Austen', 9780141439518, 10.00, 'prideprejudice.jpg', 0),
(5, 2, 'Wuthering Heights', 'Emily Bronte', 9780141439556, 13.00, 'wutheringheights.jpg', 1),
(6, 2, 'The Selection', 'Kiera Cass', 9780062059949, 14.00, 'selection.jpg', 1),
(7, 3, 'Brave New World', 'Aldous Huxley', 9780060850524, 12.00, 'bravenewworld.jpg', 1),
(8, 3, 'Ender''s Game', 'Orson Scott Card', 9780812550702, 13.50, 'endersgame.jpg', 0),
(9, 3, 'Dune', 'Frank Herbert', 9780441172719, 12.00, 'dune.jpg', 0),
(10, 4, 'The Book Thief', 'Markus Zusak', 9780375842207, 19.00, 'bookthief.jpg', 1),
(11, 4, 'All the Light We Cannot See', 'Anthony Doerr', 9781501173219, 12.00, 'allthelight.jpg', 0),
(12, 4, 'The Nightingale', 'Kristin Hannah', 9781250080400, 14.50, 'nightingale.jpg', 0),
(13, 5, 'Thirteen', 'Steve Cavanagh', 9781250297624, 12.00, 'thirteen.jpg', 1),
(14, 5, 'Murder on the Orient Express', 'Agatha Christie', 9780062693662, 10.00, 'orientexpress.jpg', 0),
(15, 5, 'Magpie Murders', 'Anthony Horowitz', 9780062645227, 16.00, 'magpiemurders.jpg', 1);
