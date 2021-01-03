from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .filters import CategoryFilter
from .models import Film, Contact
from django.conf import settings
from .forms import contactForm
from django.db.models import Q
import os
import re

def mobile(request):
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

# Create your views here.
def homePage(request):

    films = Film.objects.all().order_by('-id')
    topFilms = Film.objects.all().order_by('-Views')[:15]

    q = request.GET.get('q')
    if q:
        films = Film.objects.filter(Q(Title__icontains=q))

    query = request.GET.get('Category__contains')
    myCatFilter = CategoryFilter(request.GET, queryset=films)
    films = myCatFilter.qs

    paginator = Paginator(films, 36)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        films = paginator.page(page)
    except(EmptyPage, InvalidPage):
        films = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = contactForm()

    if mobile(request):
        is_mobile = 1
    else:
        is_mobile = 2

    is_mobile_negative = is_mobile * -1

    context = {
        'films': films,
        'topFilms': topFilms,
        'myCatFilter': myCatFilter,
        'form': form,
        'query': query,
        'tquery': q,
        'is_mobile': is_mobile,
        'is_mobile_negative': is_mobile_negative,
    }

    return render(request, 'index.html', context)

def prodDetail(request, slug):

    film = Film.objects.get(Slug=slug)
    Film.objects.filter(Slug=slug).update(Views=film.Views + 1)

    context = {
        'film': film
    }

    return render(request, 'singleMovie.html', context)