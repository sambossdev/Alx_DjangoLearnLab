# relationship_app/urls.py
from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based view

    # Authentication routes
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# append to urlpatterns
path('role/admin/', views.admin_view, name='admin_view'),
path('role/librarian/', views.librarian_view, name='librarian_view'),
path('role/member/', views.member_view, name='member_view'),
