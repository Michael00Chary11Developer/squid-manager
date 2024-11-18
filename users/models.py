from django.db import models
from django.db import models
import uuid

class BlockedSite(models.Model):
    url = models.URLField(unique=True, help_text="The URL of the blocked site.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
