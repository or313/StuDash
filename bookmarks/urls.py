from django.urls import path
from bookmarks.views import create_bookmarks
from bookmarks.views import delete_bookmark


app_name = 'bookmarks'

urlpatterns = [
    path("", create_bookmarks, name="create"),
    path("delete_bookmark/<int:pk>/", delete_bookmark, name="delete"),
]
