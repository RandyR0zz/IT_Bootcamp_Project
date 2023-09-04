from django.contrib import admin
from .models import Author, Book

# Adding Author model to the administration panel
admin.site.register(Author)

# Adding Book model to the administration panel
admin.site.register(Book)