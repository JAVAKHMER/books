from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from books.models import Books
from books.forms import BookForm
class DisplayBookView(View):
    def get(self,request):
        books = Books.objects.all()
        form = BookForm()
        return render(request, 'books.html', {'books': books,'form': form})
    def post(self,request):
        if request.POST:
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        return render(request, 'books.html', {'form': form})
class updateBookView(View):
    def get(self,request,id_book):
        books = Books.objects.all()
        book = get_object_or_404(Books, id=id_book)
        form = BookForm(request.POST or None, instance=book)
        return render(request, "books.html", {'books': books,'form': form})
                
    def post(self,request,id_book):
        book = get_object_or_404(Books, id=id_book)
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, "books.html", {'form': form})
class deleteBookView(View):
    def get(self,request,id_book):
        book = Books.objects.get(id=id_book)
        book.delete()
        return redirect('book_list')
