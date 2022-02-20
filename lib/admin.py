from django.contrib import admin
from .models import *

for model in BookInstance, Genre, Comment:
    admin.site.register(model)

class BookInliner(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'born']
    list_filter = ['last_name']
    inlines = [BookInliner]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ['author']