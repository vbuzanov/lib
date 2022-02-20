from django.urls import path
from . import views

app_name = "lib"

urlpatterns = [
    path('', views.index, name='index'),
    # path('book/all/', views.book_list, name='book-list'),
    path('book/all/', views.BookListView.as_view(), name='book-list'),
    # path('author/all/', views.author_list, name='author-list'),
    path('author/all/', views.AuthorListView.as_view(), name='author-list'),
    # path('genre/all/', views.genre_list, name='genre-list'),
    path('genre/all/', views.GenreListView.as_view(), name='genre-list'),
    # path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # path('author/<int:pk>/', views.author_detail, name='author-detail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('comment/add/', views.add_comment, name='add-comment'),
    path('book/order/', views.edit_order, name='edit-order'),
]