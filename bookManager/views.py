from django.shortcuts import render
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.contrib import messages

# Create your views here.
# mit der Unten aufgeführten Methode, rendern wir die HTML seite
def showAuthors(request):
    authors = Author.objects.all()
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author succsessfully added')
    return render(request, 'bookManager/showAuthors.html', {'authors': authors, 'form': form})

def showBooks(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'bookManager/showBooks.html', {'books': books, 'form': form})