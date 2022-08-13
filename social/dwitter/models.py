from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,  # Users don't have the mutual following with the one who follow them
        blank=True
    )

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):

    if created:
        user_profile = Profile(user=instance)   # create a new profile and set the user to the user that we are saving
        user_profile.save()     # Save the profile for it to have an id in the database
        user_profile.follows.add(instance.profile.id)
        # user_profile.follows.set([instance.profile.id])  # set the follows property of the profile to the current user instance
        user_profile.save()  # Save the profile to the database


post_save.connect(create_profile, sender=User)  # Connect a model's saving action to trigger a function
