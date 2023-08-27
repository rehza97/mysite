from django.shortcuts import redirect, render

from .models import Profile
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('myapp:products')
    context = {
        'form' : form
    }
    return render(request , 'users/register.html',context)

@login_required(login_url='users:login')
def profile(request):
    context = {
    
    }
    return render(request , 'users/profile.html',context)

@login_required(login_url='users:login')
def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(
            
            contact_number = contact_number,
            image = image,
        )
        profile.user = user
        profile.save()
 
    return render(request , 'users/createprofile.html')
