from django.db import models
from django.utils import timezone
from .utils import generate_unique_slug

# Create your models here.
class Link(models.Model):
    original_url = models.URLField(max_length=2000)
    slug = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True, blank=True)
    access_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=128, blank=True)  # optional hashed password

    def __str__(self):
        return f"{self.slug} → {self.original_url}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug()
        super().save(*args, **kwargs)