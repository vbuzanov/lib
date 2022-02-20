# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import timedelta

from .models import *


def index(request):

    # data = Comment.objects.filter(book__author__id__exact=4)
    # print('-' * 20)
    # for item in data:
    #     print(item.text, item.book, item.book.author)
    # print('-' * 20)

    return render(request, template_name='lib/index.html')


# def book_list(request):
#     context = {
#         'books': Book.objects.order_by('title'),
#     }
#     return render(request, template_name='lib/book_list.html', context=context)


class BookListView(ListView):
    model = Book


# def author_list(request):
#     context = {
#         'authors': Author.objects.all(),
#     }
#     return render(request, template_name='lib/author_list.html', context=context)

class AuthorListView(ListView):
    model = Author
    template_name = 'lib/authors.html'
    context_object_name = 'authors'
    # queryset = Author.objects.filter(last_name__istartswith='d')

# def genre_list(request):
#     context = {
#         'genres': Genre.objects.all(),
#     }
#     return render(request, template_name='lib/genre_list.html', context=context)

class GenreListView(ListView):
    model = Genre

# def book_detail(request, pk):
#     context = {
#         'book': Book.objects.get(id__exact=pk),
#     }
#     return render(request, template_name='lib/book_detail.html', context=context)

class BookDetailView(DetailView):
    model = Book

# def author_detail(request, pk):
#     context = {
#         'author': Author.objects.get(pk=pk),
#     }
#     return render(request, template_name='lib/author_detail.html', context=context)


class AuthorDetailView(DetailView):
    model = Author


def add_comment(request):
    author = request.POST.get('author')
    text = request.POST.get('text')
    book_id = request.POST.get('book_id')
    if author and text:
        new_comment = Comment(author=author, text=text, book_id=book_id)
        new_comment.save()
    return HttpResponseRedirect(reverse('lib:book-detail', kwargs={'pk': book_id}))


def edit_order(request):
    bi_id = request.POST.get('bi_id')
    bi = BookInstance.objects.get(id=bi_id)
    due_back = datetime.datetime.now() + timedelta(days=7)
    bi.status = 'o'
    bi.due_back = due_back
    book_id = bi.book_id
    bi.save()
    return HttpResponseRedirect(reverse('lib:book-detail', kwargs={'pk': book_id}))
