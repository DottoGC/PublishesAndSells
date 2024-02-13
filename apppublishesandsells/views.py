from django.template import RequestContext
from apppublishesandsells.models import Web
from django.shortcuts import get_object_or_404,redirect,render
from django.contrib.auth import logout,authenticate,login
from apppublishesandsells.forms import LoginForm

# Create your views here.
def index_view(request):
    miweb = get_object_or_404(Web, pk=1)
    return render(request, 'index.html', {'miweb':miweb})

def login_view(request):
    miweb = get_object_or_404(Web, pk=1)
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Bienvenido! Te has identificado de modo correcto!"
                else:
                    message = "Tu cuenta no esta activada."
            else:
                message = "Username y/o Password Incorrecto!"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'message': message, 'form': form, 'miweb': miweb})

def logout_view(request):
    logout(request)
    return redirect('index')
