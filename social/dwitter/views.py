from django.shortcuts import render

from dwitter.models import Profile


def dashboard(request):
    return render(request, "dashboard.html")


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
