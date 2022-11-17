from django.shortcuts import render
from .forms import NewUserForm
# Create your views here.
def home(request):
    return render(request,'home.html') 

def users(request):
    form = NewUserForm()
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
           form.save(commit=True)
           return home(request)
        else:
            print('Error from INVALID')
    return render (request,'second_app\signup_form.html',context={'form':form})


