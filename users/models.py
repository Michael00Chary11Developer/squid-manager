from django.db import models
# from django.core.exceptions import ValidationError
from uuid import uuid4


class BlockedSite(models.Model):

    url = models.URLField(unique=True, help_text="The URL of the blocked site.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

class UserAccess(models.Model):
    user_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    blocked_sites = models.ManyToManyField(BlockedSite, blank=True, related_name="users", help_text="Blocked sites for this user.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Access settings for User {self.user_id}"