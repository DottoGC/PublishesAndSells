from django.shortcuts import render_to_response,get_object_or_404,redirect,render
from apppublishesandsells.models import Web
from appusers.forms import CustomerMultiForm

def registro_view(request):
    miweb = get_object_or_404(Web, pk=1)
    if request.method == "POST":
        form = CustomerMultiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerMultiForm()

    return render(request, 'registro.html', {'form': form, 'miweb': miweb})

