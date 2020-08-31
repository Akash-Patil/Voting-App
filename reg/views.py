from django.shortcuts import render, redirect, HttpResponseRedirect
from reg.models import Member
from poll.models import Question, Choice
# Create your views here.

def index(request):              #add a new one
    if request.method == 'POST':
        if Member.objects.filter(Email = request.POST['Email']).exists():
            return render(request, 'reg/index.html',{'msg': 'Error: User already exists, change email'})
        else:
            member = Member(Name = request.POST['Name'], Email = request.POST['Email'],Password = request.POST['Password'])
            member.save()
        return redirect('/')
    else:
        return render(request, 'reg/index.html') #redirect to the signup page


def login(request):
    return render(request, 'reg/login.html')

def home(request):  #check if it exists to move onto the next page.
    if request.method == 'POST':
        if Member.objects.filter(Name=request.POST['Name'], Email = request.POST['Email'], Password = request.POST['Password']).exists():
            member = Member.objects.get(Name=request.POST['Name'], Email = request.POST['Email'], Password = request.POST['Password']) 
            return render(request, 'reg/switch.html') #have changed
        else:
            context = {'msg': 'Invalid Username, Email or Password'}
            return render(request, 'reg/login.html', context)


