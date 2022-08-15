from django.shortcuts import render, redirect

from dwitter.forms import DweetForm
from dwitter.models import Profile


def dashboard(request):
    form = DweetForm(request.POST or None)  # instantiate an bounded form if we have POST data
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect('dwitter:dashboard')    # reset the request.method to get to prevent double posts
        else:
            # if the form is not valid, we will resubmit the form with the post data (that way the form
            # can display error message because we render the form {{ form.is_p }}
            pass
    return render(request, "dashboard.html", {"form": form})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    # Visit the profile page with the id = pk
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile_object = Profile.objects.get(pk=pk)  # The first pk can be id
    if request.method == "POST":    # submit the data to the same page
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile_object)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile_object)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile_object})
