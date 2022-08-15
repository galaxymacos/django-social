from django.contrib import admin
from django.contrib.auth.models import Group, User

from dwitter.models import Profile, Dweet


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# Remove (because now we can edit Profile in UserAdmin): admin.site.register(Profile)
admin.site.register(Dweet)
