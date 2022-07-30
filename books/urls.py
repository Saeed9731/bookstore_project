from django.urls import path

from .views import BookListView,BookDetailView
urlpatterns = [
    path('', BookListView.as_view(), name='book_list_view'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
]
