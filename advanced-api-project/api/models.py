from django.db import models

# Author model represents a book author
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model with a foreign key to Author (One-to-many)
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    class Meta:
        # Added for clarity in admin
        ordering = ["title"]

    def __str__(self):
        return self.title
