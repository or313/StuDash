from django.shortcuts import render, redirect
from django.contrib import messages
from bookmarks.models import Bookmark
from grades.models import Course
from bookmarks.forms import BookmarkForm


def create_bookmarks(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            urlname = form.cleaned_data['urlname']
            course = form.cleaned_data['course']
            Bookmark.add_bookmark(course, url, urlname)
            messages.success(request, "Bookmark saved successfully!")
            return redirect('bookmarks:create')
    else:
        form = BookmarkForm()
    form.fields["course"].queryset = Course.objects.filter(user=request.user)
    bookmarks = Bookmark.objects.select_related('course').filter(course__user=request.user)
    return render(request, 'bookmarks/bookmarks.html', {
        'bookmarks': bookmarks,
        'form': form,
    })


def delete_bookmark(request, pk):
    bm = Bookmark.objects.get(pk=pk)
    Bookmark.remove_bookmark(bm)
    messages.success(request, "Bookmark Deleted!")
    return redirect('bookmarks:create')
