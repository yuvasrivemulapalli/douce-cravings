from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from actions.models import Action
from .forms import RegistrationForm, ProfileForm
from .models import Details

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']

            user = User.objects.create(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

            details, created = Details.objects.get_or_create(user=user)
            details.gender = gender
            details.save()

            request.session['username'] = user.username
            request.session['role'] = user.details.role
            messages.success(request, f"You have successfully registered with username: {user.username}")
            return redirect('doucecravingsnew_app:home')
        # Removed the else block for error messages
    else:
        form = RegistrationForm()

    return render(request, "users/user/register.html", {'form': form})

#Profile View
def profile(request, username):
    user = get_object_or_404(User, username=username)
    details, created = Details.objects.get_or_create(user=user)
    request.session['user_id'] = user.id
    actions = Action.objects.filter(user_id=request.session['user_id']).order_by('-created')

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            role = form.cleaned_data['role']

            # Update user and details objects
            user.username = username
            user.password = password
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            details.gender = gender
            details.role = role

            # Save changes
            print(details.role)
            user.save()
            details.save()

            return redirect('users:profile', username=username)
    else:
        form = ProfileForm(request.POST)
        # Populate the form with current user data
        print(form.errors)
        form = ProfileForm(initial={'username': user.username,
                                    'password': user.password,
                                    'email': user.email,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'gender': details.gender,
                                    'role': details.role})

    return render(request, 'users/user/profile.html', {'form': form, 'user': user, 'actions': actions})

def user_details(request, username):
    # Retrieve the user object based on the provided username
    user = get_object_or_404(User, username=username)

    # You can add more logic or retrieve additional data related to the user here

    return render(request, 'users/user/user_details.html', {'user': user})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and (password == user.password):
            request.session['username'] = user.username
            request.session['role'] = user.details.role
            messages.add_message(request, messages.SUCCESS, "You have logged in successfully")
            return redirect('doucecravingsnew_app:home')
        else:
            messages.add_message(request, messages.ERROR, "Invalid Username or Password")

    return render(request, 'users/user/login_page.html')


def users_edit(request):
    users_names = User.objects.values_list('username', flat=True)
    return render(request, 'users/user/users_edit.html', {'users_names': users_names})


# Logout View
def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('doucecravingsnew_app:main')