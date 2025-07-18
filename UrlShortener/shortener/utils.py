import string
import random

BASE62 = string.ascii_letters + string.digits

def generate_random_slug(length=6):
    return ''.join(random.choice(BASE62) for _ in range(length))

def generate_unique_slug(length=6):
    from .models import Link
    slug = generate_random_slug(length)
    while Link.objects.filter(slug=slug).exists():
        slug = generate_random_slug(length)
    return slug
