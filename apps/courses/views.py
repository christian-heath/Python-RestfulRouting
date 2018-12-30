from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Product

def index(request):
    context = {
        'products': Product.objects.all().values()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    if request.method == 'POST':
        errors = Course.objects.validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/courses')
        else:
            Course.objects.create(name = request.POST['name'], desc=request.POST['desc'])
            messages.success(request, "User successfully created!")
        return redirect('/courses')    
    else:
        return redirect('/courses')

def checkout(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/confirm.html', context)

def buy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/courses')