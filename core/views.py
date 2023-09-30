from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

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


def books(request):
    books_db = [{'id': 1, 'title': 'Волчина и пряности ', 'description': """«Волчи́ца и пря́ности» (яп. 狼と香辛料 О:ками то ко:синрё:, досл. «Волчица и специи») — популярная японская серия ранобэ, написанная Исуной Хасэкурой, с иллюстрациями Дзю Аякуры. В 2007 году число проданных экземпляров, согласно «Майнити симбун», превысило 500 тысяч, а в 2008 — уже 2,2 млн экземпляров[1]. Всего же выпущено 24 тома «лайт-новел» (14 основных и десять «побочных историй», которые носят название Side Colors и Spring Log. Несмотря на официальное завершение серии на 17 томе, осенью 2016 года продолжился выпуск как спин-оффа основной сюжетной линии «Волчица и пряности» (сборники рассказов Spring Log), так и сиквела «Волчица и пергамент». На апрель 2021 года обе серии насчитывают по 5 томов. Несмотря на то, что «Волчица и пряности» написана в жанре фэнтези, она выделяется из других произведений подобного жанра, так как герои по большей части вращаются в мире торговли и товарно-денежных отношений, а не в мире меча и магии[2]. Манга, нарисованная Кэйто Коумэ, публиковалась в журнале Dengeki Maoh с сентября 2007 года по декабрь 2017-го, а аниме, снятое по мотивам романов, было показано в 2008 году. Позже по сюжету произведения вышла видеоигра в жанре «симулятор свиданий», предназначенная для платформы Nintendo DS. Также на начало 2019 года анонсирована VR-игра от студии Spicy Tails. 25 февраля 2022 года было объявлено о выпуске нового аниме[3].""" }]

    data = {
        'title': 'Книги',
        'menu': menu,
        'books': books_db
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
