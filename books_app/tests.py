from django.test import TestCase
from .models import Author, Book


class AuthorModelTest(TestCase):
    
    '''
    Class of testing Author model
    
    Methods
    -------    
    test_name_for_str()
        Check if it converts to textual name     
    
    test_name_max_length()
        Check max length of the author name
    '''
    
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name = 'Alexander Pushkin')
    
    def test_name_for_str(self):
        author = Author.objects.get(id = 1)
        expected_name = f'{author.name}'
        self.assertEquals(expected_name, str(author))
    
    def test_name_max_length(self):
        author = Author.objects.get(id = 1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


class BookModelTest(TestCase):
    
    '''
    Class of testing Book model
    
    Methods
    -------    
    test_title_for_str()
        Check if it converts to textual title     
    
    test_title_max_length()
        Check max length of the book title
    '''
    
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title = 'Harry Potter')
    
    def test_title_for_str(self):
        book = Book.objects.get(id = 1)
        expected_title = f'{book.title}'
        self.assertEquals(expected_title, str(book))
    
    def test_title_max_length(self):
        book = Book.objects.get(id = 1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
    


class ValidationModels(TestCase):
    
    '''
    Class of testing of validation from the models
    
    Methods
    -------    
    test_create_author()
        Check special symbols or digits in the name of author    
    
    test_title_max_length()
        Check special symbols or digits in the title of book
    '''
    
    def test_create_author(self):
        author = Author.objects.create(name="!@#$%^&*()_+-=<>/\,`~|.][0123456789")
        self.assertEqual(author.name, "!@#$%^&*()_+-=<>/\,`~|.][0123456789")
    
    def test_create_book(self):
        book = Book.objects.create(title="!@#$%^&*()_+-=<>/\,`~|.][0123456789")
        self.assertEqual(book.title, "!@#$%^&*()_+-=<>/\,`~|.][0123456789")