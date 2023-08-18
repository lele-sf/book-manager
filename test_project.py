from unittest.mock import patch, mock_open
from project import add_book, delete_book, update_book

def test_add_book():
    with patch('builtins.input', side_effect=['The Hobbit', 'J. R. R. Tolkien', 'Fantasy', '1937']), \
         patch('builtins.open', mock_open()):
        expected_output = 'Book added successfully!'
        assert add_book() == expected_output

def test_delete_book():
    with patch('builtins.input', side_effect=['1']), \
         patch('builtins.open', mock_open()):
        books = [{'ID': 1, 'Title': 'The Hobbit', 'Author': 'J. R. R. Tolkien', 'Genre': 'Fantasy', 'Year': '1937'}]
        expected_output = 'Book "The Hobbit" deleted successfully!'
        assert delete_book(books) == expected_output

def test_update_book():
    with patch('builtins.input', side_effect=['1', 'The Hobbit Updated', 'J. R. R. Tolkien', 'Fantasy', '1950']), \
         patch('builtins.open', mock_open()):
        books = [{'ID': 1, 'Title': 'The Hobbit', 'Author': 'J. R. R. Tolkien', 'Genre': 'Fantasy', 'Year': '1937'}]
        expected_output = 'Book "The Hobbit Updated" updated successfully!'
        assert update_book(books) == expected_output
