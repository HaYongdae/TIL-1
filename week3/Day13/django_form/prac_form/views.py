from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book
from IPython import embed

def index(request):
    books = Book.objects.all()

    context= {
        "books":books
    }
    return render(request, 'prac_form/index.html', context)

def new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
     
        if form.is_valid():
            book = form.save()
            return redirect(book)
    else:
        form = BookForm()

    context={
        'form':form,
    }
    return render(request, 'prac_form/new.html', context)

def detail(request, b_id):
    # book = Book.objects.get(id=b_id)
    book = get_object_or_404(Book, id=b_id)

    context = {
        'book': book
    }
    return render(request, 'prac_form/detail.html', context)

def edit(request, b_id):
    book = get_object_or_404(Book, id=b_id)

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            b = form.save()
            return redirect(b)
    else:
        form = BookForm(initial=book.__dict__)

    context={
        'form':form
    }
    return render(request, 'prac_form/new.html', context)

def delete(request, b_id):
    book = get_object_or_404(Book, id=b_id)
    if request.method == "POST":
        book.delete()
    return redirect("prac:index")