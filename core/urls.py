from django.urls import path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitalYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.books, name='books'),
    path('book/<int:book_id>', views.book_for_id, name='book_for_id'),
    path('about/', views.about, name='about'),
    path('auth/', views.auth, name='auth'),

]

