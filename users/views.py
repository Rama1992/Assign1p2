from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegiserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegiserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created! You can now login.')
            return redirect('login')
    else:
        form = UserRegiserForm()
        return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')
