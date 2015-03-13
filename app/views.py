from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from app.models import Toner

# Create your views here.


@login_required
def index(request):
    return redirect('toners')

@login_required
def toners(request):
    toners = Toner.objects.order_by('identificador')
    context = {'toners': toners}
    return render(request, 'toners.html', context)

@login_required
def logout(request):
    logout(request)
    return redirect('toners')
#    return render(request, 'login.html')

def login(request):
    if request.POST.get('username') and request.POST.get('password'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('toners')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return render(request, 'login.html')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

