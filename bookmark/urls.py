from django.urls import path

from bookmark.views import BookmarkAddView, BookmarkListView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkAddView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]