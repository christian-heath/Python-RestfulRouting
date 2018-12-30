from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User

def index(request):
    context = {
        'users': User.objects.all().values()
    }
    return render(request, 'semi_restful/users.html', context)

def new(request):
    return render(request, 'semi_restful/new.html')

def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'semi_restful/edit.html', context)

def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request,'semi_restful/show.html', context)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')

def create(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/new')
        else:
            User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            id = User.objects.last().id
            print(id)
            messages.success(request, "User successfully created!")
        return redirect('/users/'+str(id))    
    else:
        return redirect('/users/new')

def update(request, id):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/'+str(id)+'edit')
        else:
            user = User.objects.get(id= id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            messages.success(request, "User successfully updated")
        return redirect('/users/'+str(id))    
    else:
        return redirect('/users')