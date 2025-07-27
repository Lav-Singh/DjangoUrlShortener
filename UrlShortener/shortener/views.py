from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import URLForm
from .models import Link,models

def shorten_view(request):
    form = URLForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        cd = form.cleaned_data
        original = cd['original_url']
        slug = cd['custom_slug'] or None

        if slug:
            link = Link(original_url=original, slug=slug)
        else:
            link = Link(original_url=original)
        link.save()
        short_url = request.build_absolute_uri(reverse('redirect_view', args=[link.slug]))
        return render(request, 'shortener/result.html', {'short_url': short_url, 'link': link})
    return render(request, 'shortener/shorten.html', {'form': form})

def redirect_view(request, slug):
    link = get_object_or_404(Link, slug=slug)
    #update access count and timestamp
    link.access_count = models.F('access_count')+1
    link.last_accessed = timezone.now()
    link.save(update_fields=['access_count', 'last_accessed'])
    return redirect(link.original_url)
