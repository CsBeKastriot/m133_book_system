from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.contrib import messages


# Create your views here.
# mit der Unten aufgeführten Methode, rendern wir die HTML seite
def list_Authors(request):
    authors = Author.objects.all()
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author succsessfully added')
    return render(request, 'bookManager/list_Authors.html', {'authors': authors, 'form': form})


def list_books(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'bookManager/list_Books.html', {'books': books, 'form': form})


def show_authors(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        form = AuthorForm()
    except Author.DoesNotExist:
        messages.error(request, 'There is no Author with this ID!')
        return redirect(list_Authors)
    return render(request, 'bookManager/showAuthors.html', {'author': author, 'form': form})
