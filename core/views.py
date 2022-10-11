from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import Adduser,FriendsSearchForm
from django.contrib import messages
import datetime

def add_user(request):
    form = Adduser(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('/suggest')
    context = {
        "form": form,
        "title": " Add Friend",
    }
    return render(request, "add.html", context)

def suggest(request,username):
    title = 'Friends List'
    form = FriendsSearchForm(request.POST or None)
    queryset = Friends.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form
    }
    if request.method == 'POST':
        queryset = Friends.objects.filter(item_name__icontains=form['username'].value())
        if form['username'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of client.csv"'
            writer = csv.writer(response)
            writer.writerow(['id', 'username'])
            instance = queryset
            for user in instance:
                writer.writerow([user.id, user.username])
            return response
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "suggest.html", context)

def add_friend(request,pk):
    queryset = User.objects.get(id=pk)
    form = Adduser(request.POST or None)
    if request.method == 'POST':
        form = Adduser(request.POST, instance=queryset)
    if form.is_valid():
        form.save()
        return redirect('/suggest')
    context = {
        "form": form,
        "title": " Add Friend",
    }
    return render(request, "add.html", context)








