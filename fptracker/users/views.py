from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group, User
from pens.views import  index
from users.forms import UserForm, ProfileForm
from users.models import Profile
# Create your views here.


def sign_up(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            group = Group.objects.get(name='normal')
            new_user.groups.add(group)
            new_user.save()
            profile = profile_form.save(commit = False)
            profile.user = new_user
            profile.save()
            if new_user:
                login(request, new_user)
            return redirect(index)
    else:
        form = UserCreationForm()
        profile_form = ProfileForm()

    
    context = {
        'form':form,
        'profile_form':profile_form,
    }

    return render(request, 'signup.html', context)

def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect(index)

    context = {
        'user_object':user
    }
    return render (request, "user_profile.html", context)


def edit_user(request, username):
    profile = None
    try:
        user = User.objects.get(username=username)
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            pass
    except User.DoesNotExist:
        return redirect(index)

    if ((request.user.has_perm('users.change_user')) or (request.user.username == username)):
        if request.method == "POST":
            form = UserForm(request.POST, instance = user)

            if profile:
                profile_form = ProfileForm(request.POST, instance = profile)
            else:
                profile_form=ProfileForm(request.POST)
            if form.is_valid():
                updated_user = form.save()
                if profile_form.is_valid():
                    new_profile = profile_form.save(commit = False)
                    new_profile.user = updated_user
                    new_profile.save()
                return redirect(user_profile, username =username)
        else:
            form = UserForm(instance=user)
            if profile:
                profile_form = ProfileForm(instance = profile)
            else:
                profile_form = ProfileForm()

        context = {
            'form':form,
            'username':username,
            'profile_form':profile_form
            }
        return render(request, "edit_user.html", context)
    
    return HttpResponse('No Permission')