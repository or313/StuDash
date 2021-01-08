from django.urls import path
from forumMessages.views import ViewMessages, ViewCategories


app_name = 'forumMessages'

urlpatterns = [
    path("", ViewMessages, name="view_messages"),
    path("categories/", ViewCategories, name="view_categories"),
]
