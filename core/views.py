from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from core.models import Artwork

# Create your views here.

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Книги', 'url_name': 'books'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Авторизация', 'url_name': 'auth'},


]


def index(request):

    data = {
        'title': 'Главная страница',
        'menu': menu,
            }
    return render(request, 'core/index.html', context=data)


def book_for_id(request, book_id):
    data = {
        'title': 'Книга',
        'menu': menu,
        'book_id': book_id
            }
    return render(request, 'core/post.html', context=data)


def artwork_by_slug(request, art_slug):
    art = Artwork.objects.filter(slug=art_slug).first()

    data = {
        'title': art.title,
        'menu': menu,
        'post': art
    }
    return render(request, 'core/artwork.html', context=data)


def books(request):
    arts = Artwork.objects.filter(is_active=True)
    data = {
        'title': 'Книги',
        'menu': menu,
        'artworks': arts
    }
    return render(request, 'core/books.html', context=data)

def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
            }
    return render(request, 'core/about.html', context=data)


def auth(request):
    data = {
        'title': 'Авторизация',
        'menu': menu,
    }
    return render(request, 'core/auth.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
