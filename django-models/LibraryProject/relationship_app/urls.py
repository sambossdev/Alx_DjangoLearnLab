from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_user,
    login_user,
    logout_user,
)

urlpatterns = [
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),

    # Authentication routes
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
