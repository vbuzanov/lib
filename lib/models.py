from django.db import models
import datetime

from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    born = models.DateField(null=True, blank=True)
    portrait = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def genres(self):
        genre_list = []
        for book in self.books.all():
            for genre in book.genres.all():
                if genre not in genre_list:
                    genre_list.append(genre)
        return sorted(genre_list, key=lambda g: g.name)


    # def comments(self):
    #     comments_list = []
    #     for book in self.books.all():
    #         for comment in book.comments.all():
    #             comments_list.append(comment)
    #     return sorted(comments_list, key=lambda c: c.published, reverse=True)


    def comments(self):
        return Comment.objects.filter(book__author__id__exact=self.id).order_by("-published")


    def url(self):
        return reverse('lib:author-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['last_name', 'first_name']


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def url(self):
        return reverse('lib:genre-list') + f'#section{self.id}'


class Book(models.Model):
    title = models.CharField(max_length=258)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='books')
    cover = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def url(self):
        return reverse('lib:book-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['title']


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='instances')
    LOAN_STATUS = (
        ('a', 'available'),
        ('o', 'on loan'),
        ('m', 'maintenance'),
        ('r', 'reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m')
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.book} - "{self.status}"'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=128)
    text = models.TextField()
    published = models.DateTimeField(default=datetime.datetime.now)