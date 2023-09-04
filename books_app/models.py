from django.db import models
from django.core.exceptions import ValidationError


def validate_symbols(value):
    
    '''Function for validation special character(s) or digit(s) or empty data'''
    
    if value == None:
        raise ValidationError('Must not be empty')
    
    symbols = '!@#$%^&*()_+-=<>/\,`~|.][0123456789'
    
    for symbol in symbols:
        for letter in value:
            if symbol == letter:
                raise ValidationError('Must not contain special symbol(s) of digit(s)')
    
    return value

             
class Author(models.Model):
    
    '''
    Class of entity Author
    
    Attributes
    ----------
    name : str
        Full name of author(s)
    
    Methods
    -------    
    __str__()
        Provides textual name(s) of class instances in the admin panel 
    '''
    
    name = models.CharField(max_length=100, unique=True, validators=[validate_symbols])
    
    def __str__(self):
        return self.name

    
class Book(models.Model):
    
    '''
    Class of entity Book
    
    Attributes
    ----------
    title : str
        Title of book(s)
    authors : ManyToManyRelatedManager
        M2M relation
    
    Methods
    -------
    __str__()
        Provides textual title(s) of class instances in the admin panel 
    '''
    
    title = models.CharField(max_length=100, unique=True, validators=[validate_symbols])
    authors = models.ManyToManyField(Author, through='Relation')

    def __str__(self):
        return self.title

    
class Relation(models.Model):
    
    '''
    Class of summary table of relations
    
    Attributes
    ----------
    book : Book
        Foreign Key to Book`s class
    author : Author
        Foreign Key to Author`s class
    '''
    
    book = models.ForeignKey(Book, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)