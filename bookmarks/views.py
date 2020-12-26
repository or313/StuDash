from django.shortcuts import render, redirect
from django.contrib import messages
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm


def Create_Bookmarks(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        user = request.user
        if form.is_valid():
            url = form.cleaned_data['url']
            urlname = form.cleaned_data['urlname']
            course = form.cleaned_data['course']
            bookmark = Bookmark(user=user, course=course, url=url, urlname=urlname)
            bookmark.save()
            messages.success(request, "Bookmark saved successfully")
            return redirect('Bookmarks')
    else:
        form = BookmarkForm()
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks/bookmarks.html', {
        'bookmarks': bookmarks,
        'form': form,
    })
