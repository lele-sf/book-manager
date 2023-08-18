# Book Management System

This is a simple command-line application for managing a collection of books. It allows users to add, delete, update, and display books. The book information is stored in a CSV file.

[Video Demo](https://youtu.be/dVGJfOoGEao)

## Features

- **Add Book:** Add new books to your collection by providing essential details like title, author, genre, and publication year.
- **Delete Book:** Remove books from your collection using their unique ID.
- **Update Book:** Modify book details such as title, author, genre, and publication year for specific books.
- **Display Books:** Explore your collection using various options, including searching by title or author, displaying books by genre, and viewing all books.
- **Save and Load:** Save your book collection to a CSV file to maintain your progress between sessions, and load your existing collection when starting the application.

## Prerequisites

- Python 3.x
- Required packages: `tabulate`

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the package `tabulate`
```
$ pip install tabulate
```

## How to Run
Clone this repository to your local machine
```
$ git clone https://github.com/lele-sf/BookManager.git
```
Use [python](https://www.python.org/) to run the main program
```
$ python project.py
```
Use [pytest](https://docs.pytest.org/en/7.2.x/) to run the unit tests for the functions
```
$ pytest test_project.py
```

## Note
The application uses a CSV file named books.csv to store book information. Make sure the file is in the same directory as the script.

## Author
[Letícia Fernandes](https://github.com/lele-sf)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.