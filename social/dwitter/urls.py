from django.urls import path

from dwitter.views import dashboard, profile_list

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list", profile_list, name="profile_list")
]