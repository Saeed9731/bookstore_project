from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book
from .forms import CommentsForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = 'books/books_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/books_detail.html'

def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comment
    book_comments = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentsForm()
    else:
        comment_form = CommentsForm()
    return render(request, 'books/books_detail.html', {
        'book': book,
        'comments': book_comments,
        'comment_form': comment_form
    })


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list_view')
