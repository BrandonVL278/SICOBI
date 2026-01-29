from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


def sign_in(request):
    form = AuthenticationForm(data=request.POST or None)

    form.fields['username'].label = 'Usuario'
    form.fields['password'].label = 'Contraseña'
    form.fields['username'].widget.attrs.update({
        'placeholder': 'Usuario'
    })
    form.fields['password'].widget.attrs.update({
        'placeholder': 'Contraseña'
    })

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('library:index')
        else:
            form.errors.clear()
            form.add_error(None, 'Usuario o contraseña incorrectos')

    return render(request, 'account/sign_in.html', {'form': form})

def sign_out(request):
	logout(request)
	return redirect('master:index')