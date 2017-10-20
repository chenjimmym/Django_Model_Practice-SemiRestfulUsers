from django.shortcuts import render, redirect, HttpResponse
from models import *
# Create your views here.
def index(request):
    response = 'connected no problem'
    return HttpResponse(response)

def users(request):
    return render(request, 'users/user_dash.html', {'all_users':User.objects.all()})

def show(request, user_number):
    response = 'connected to show', user_number
    return render(request, 'users/user.html', {'user':User.objects.get(id=user_number)})

def new(request):
    return render(request, 'users/user_create.html')

def create(request):
    if request.method == "POST":
        print request.POST['inputted_name']
        print request.POST['inputted_email']
        User.objects.create(name=request.POST['inputted_name'], email=request.POST['inputted_email'])
    return redirect('/users')

def edit(request, user_number):
    return render(request, 'users/user_update.html', {'user':User.objects.get(id=user_number)})

def update(request, user_number):
    if request.method == "POST":
        temp = User.objects.get(id=user_number)
        if request.POST['inputted_name']:
            temp.name = request.POST['inputted_name']
        if request.POST['inputted_email']:
            temp.email = request.POST['inputted_email']
        temp.save()
        temp_url = '/users/' + user_number
    return redirect(temp_url)

def delete(request, user_number):
    User.objects.get(id=user_number).delete()
    return redirect('/users')