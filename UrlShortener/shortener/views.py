from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import URLForm
from .models import Link

def shorten_view(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            link = Link(original_url=cd['original_url'], slug=cd.get('custom_slug') or None)
            link.save()
            return redirect('result_view', slug=link.slug)
    else:
        form = URLForm()

    return render(request, 'shortener/shorten.html', {'form': form})


def result_view(request, slug):
    link = get_object_or_404(Link, slug=slug)
    short_url = request.build_absolute_uri(reverse('redirect_view', args=[slug]))
    return render(request, 'shortener/result.html', {
        'link': link,
        'short_url': short_url
        })


def redirect_view(request, slug):
    link = get_object_or_404(Link, slug=slug)
    from django.utils import timezone
    from django.db.models import F
    link.access_count = F('access_count') + 1
    link.last_accessed = timezone.now()
    link.save(update_fields=['access_count', 'last_accessed'])
    return redirect(link.original_url)

def api_stats(request,slug):
    link = get_object_or_404(Link, slug = slug)
    return JsonResponse({
        'access_count': link.access_count,
        'last_accessed': link.last_accessed.isoformat() if link.last_accessed else None
    })