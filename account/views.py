from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm


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
	return redirect('account:sign_in')

@login_required
def user_profile(request):
    user = request.user
    return render(request)

@login_required
def user_record(request):
    user = User.objects.all()
    return render(request, 'user/record.html', {'user': user})

@login_required
def user_form(request, id=None):
    if id:
        user = get_object_or_404(User, id=id)
        form = CreateUserForm(request.POST or None, instance=user)
    else:
        form = CreateUserForm(request.POST or None)
        
    if request.method == 'POST' and form.is_valid():
        user_obj = form.save(commit=False)
        user_obj.set_password(form.cleaned_data['password'])
        user_obj.save()
        return redirect('account:user_record')
    
    return render(request,'user/form.html', {
		'form': form,       
	})