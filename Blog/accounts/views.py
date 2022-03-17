from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

#
def register(request):
    if request.method == "POST":
        #complete registration
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'registration/register_complete.html', {'new_user': new_user})
    else:
        #input the registration form.
        user_form = RegistrationForm()

    return render(request, "registration/register.html", {'form': user_form})