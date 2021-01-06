from django.shortcuts import render, redirect
from .models import Message, Category
from .forms import MessageForm, CategoryForm

def ViewMessages(request):
    messages = Message.objects.order_by('-date')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ViewMessages)
    else:
        form = MessageForm()
    return render(request, 'forumMessages/messagelist.html', {'messages': messages, 'form': form,})

def ViewCategories(request):
    categories = Category.objects.order_by('-id')
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ViewCategories)
    else:
        form = CategoryForm()
    return render(request, 'forumMessages/categorylist.html', {'categories': categories, 'form': form,})
