import csv
from tabulate import tabulate

books = []

###### User Interface ######
def display_menu():
    menu = [
        ['1', 'Add Book'],
        ['2', 'Delete Book'],
        ['3', 'Update Book'],
        ['4', 'Display Books'],
        ['5', 'Save and Exit'],
    ]

    headers = ['Option', 'Description']
    print(tabulate(menu, headers=headers, tablefmt='rounded_grid'))

def main():
    load_books()

    while True:
        display_menu()
        try:
            choice = int(input('Your choice: '))

            if choice == 1:
                add_book()
            elif choice == 2:
                delete_book(books)
            elif choice == 3:
                update_book(books)
            elif choice == 4:
                display_books()
            elif choice == 5:
                save_and_exit()
            else:
                print('Invalid choice. Please enter a valid option.')
        except ValueError:
            print('Invalid input. Please enter a valid option.')

###### Books Functions ######
def add_book():
    book = {}
    book['ID'] = len(books) + 1
    book['Title'] = input('Book Title: ')
    book['Author'] = input('Book Author: ')
    book['Genre'] = input('Genre: ')
    book['Year'] = input('Publication Year: ')

    books.append(book)
    save_books_to_csv()

    return 'Book added successfully!'

def delete_book(books):
    display_all_books()
    id = int(input('Enter the ID of the book to delete: '))

    deleted_book = None
    for book in books:
        if book['ID'] == id:
            deleted_book = book
            break

    if deleted_book:
        books.remove(deleted_book)
        recreate_ids()
        save_books_to_csv()
        return f'Book "{deleted_book["Title"]}" deleted successfully!'
    else:
        return f'Book with ID "{id}" not found.'

def update_book(books):
    display_all_books()
    id = int(input('Enter the ID of the book to update: '))
    updated_book = None
    for book in books:
        if book['ID'] == id:
            updated_book = book
            break

    if updated_book:
        print(f'Updating book "{updated_book["Title"]}": ')
        updated_book['Title'] = input('New Title: ')
        updated_book['Author'] = input('New Author: ')
        updated_book['Genre'] = input('New Genre: ')
        updated_book['Year'] = input('New Publication Year: ')
        save_books_to_csv()
        return f'Book "{updated_book["Title"]}" updated successfully!'
    else:
        return f'Book with ID "{id}" not found.'

def recreate_ids():
    for i, book in enumerate(books, start=1):
        book['ID'] = i

###### Display Functions ######
def display_books():
    while True:
        display_options = [
            ['1', 'Show a Specific Book by Title or Author'],
            ['2', 'Show All Books in a Specific Genre'],
            ['3', 'Show All Books'],
            ['4', 'Back to Main Menu']
        ]

        headers = ['Option', 'Description']
        print('\nDisplay Options:')
        print(tabulate(display_options, headers=headers, tablefmt='rounded_grid'))

        choice = int(input('Enter your choice: '))

        if choice == 1:
            search_criteria = input('Enter book title or author name: ')
            search_and_display_books(search_criteria)
        elif choice == 2:
            genre = input('Enter genre: ')
            display_books_by_genre(genre)
        elif choice == 3:
            display_all_books()
        elif choice == 4:
            break
        else:
            print('Invalid choice. Try again!')

def search_and_display_books(criteria):
    matching_books = []
    for book in books:
        if criteria.lower() in book['Title'].lower() or criteria.lower() in book['Author'].lower():
            matching_books.append(book)

    if matching_books:
        display_books_table(matching_books)
    else:
        print('No matching books found.')

def display_books_by_genre(genre):
    genre_books = [book for book in books if book.get('Genre').lower() == genre.lower()]

    if genre_books:
        display_books_table(genre_books)
    else:
        print(f'No books found in the "{genre}" genre.')

def display_all_books():
    display_books_table(books)

def display_books_table(book_list):
    table = []
    for book in book_list:
        table.append([book['ID'], book['Title'], book['Author'], book['Genre'], book['Year']])

    headers = ['ID', 'Title', 'Author', 'Genre', 'Year']
    print(tabulate(table, headers=headers, tablefmt='rounded_grid'))

###### File CSV ######
def save_books_to_csv():
    try:
        with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['ID', 'Title', 'Author', 'Genre', 'Year'])
            csv_writer.writeheader()
            for book in books:
                csv_writer.writerow(book)
        print('Books saved to the file successfully.')
    except Exception as e:
        print('An error occurred while saving the books:', e)

def load_books():
    try:
        with open('books.csv', 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            books.clear()
            for row in csv_reader:
                books.append(row)
            recreate_ids()
        print('Books loaded from the file successfully.')
    except FileNotFoundError:
        print('File not found. No books loaded.')
    except Exception as e:
        print('An error occurred while loading the books:', e)

def save_and_exit():
    save_books_to_csv()
    print('Exiting the program.')
    exit()

if __name__ == "__main__":
    main()