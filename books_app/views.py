from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Author, Book

def home_page(request):
    
    '''
    Function for rendering homepage. 
    Show amount of all authors and books
    '''
    
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    
    return render(request, 'home.html', 
                  {'num_authors': num_authors, 
                   'num_books': num_books})

def author_list(request):
    
    '''
    Function for rendering page of authors. 
    Show all names of available authors
    '''
    
    authors = Author.objects.all().order_by('name')
    return render(request, 'all_authors.html', 
                  {'authors': authors})


def note(request):
    
    '''Function for rendering notepage if something went wrong
    with validation of data or with data which already exist
    '''
    
    return render(request, 'note.html')


def add_author(request):
    
    '''
    Function for adding authors to the data base by the POST method.
    Validates data from the user. 
    Redirecting to the note page if not validated 
    '''
    
    if request.method == 'POST':
        author = Author()
        author.name = request.POST.get('name')
        
        try:
            author.full_clean()
            author.save()
            return author_list(request)
        except ValidationError:
            return note(request)
    
    authors = Author.objects.all()
    return render(request, 'add_author.html', 
                  {'authors': authors})


def book_list(request):
    
    '''
    Function for rendering page of books. 
    Show all entered books
    '''
    
    books = Book.objects.all().order_by('title')
    return render(request, 'all_books.html', 
                  {'books': books})


def initialize():
    
    '''Adding several authors if there are no authors at all'''
    
    if Author.objects.all().count() == 0:
        Author.objects.create(name = 'Lev Tolstoy')
        Author.objects.create(name = 'Fyodor Dostoevsky')
        Author.objects.create(name = 'Anton Chekhov')
        

def add_book(request):
    
    '''
    Function for adding books to the data base by the POST method.
    Validates data from the user. 
    Redirecting to the note page if not validated 
    '''
    initialize()
    
    if request.method == 'POST':
        book = Book()
        book.title = request.POST.get('title')
        authors_ids = request.POST.getlist('authors')
        
        try:
            authors = Author.objects.filter(id__in = authors_ids)
            
            if authors:
                book.full_clean()
                book.save()
                book.authors.set(authors)
                return book_list(request)
            else:
                return note(request)
        
        except ValidationError:
            return note(request)
    
    authors = Author.objects.all()
    return render(request, 'add_book.html', 
                      {'authors': authors})