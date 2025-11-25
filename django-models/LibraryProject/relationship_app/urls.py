from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/add/', views.add_book, name='book_add'),
    path('books/<int:pk>/edit/', views.edit_book, name='book_edit'),
    path('books/<int:pk>/delete/', views.delete_book, name='book_delete'),
]
