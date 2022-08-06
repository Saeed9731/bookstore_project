from django.urls import path

from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, book_detail_view  # BookDetailView,

urlpatterns = [
    path('', BookListView.as_view(), name='book_list_view'),
    # path('<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
    path('<int:pk>/', book_detail_view, name='book_detail_view'),
    path('create/', BookCreateView.as_view(), name='book_create_view'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update_view'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete_view'),
]
