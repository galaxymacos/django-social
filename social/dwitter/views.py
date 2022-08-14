from django.shortcuts import render

from dwitter.models import Profile


def dashboard(request):
    return render(request, "base.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile_object = Profile.objects.get(pk=pk)  # The first pk can be id
    return render(request, "dwitter/profile.html", {"profile": profile_object})
