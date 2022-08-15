from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)   # associate the post_save with the events related to the User model
def create_profile(sender, instance, created, **kwargs):

    if created:
        user_profile = Profile(user=instance)   # create a new profile and set the user to the user that we are saving
        user_profile.save()     # Save the profile for it to have an id in the database
        user_profile.follows.add(instance.profile.id)
        user_profile.save()  # Save the profile to the database


class Dweet(models.Model):
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at: %Y-%m-%d %H:%M}): "
            f"{self.body[:30]}"
        )

