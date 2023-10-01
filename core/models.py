from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class ActivitedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Artwork(models.Model):

    """Название"""
    title = models.CharField(max_length=256, verbose_name='Название')
    alternative_title = models.ManyToManyField('AlternativeName', verbose_name='Альтернативные названия', blank=True)

    """Пренадлежит серии"""
    series = models.ForeignKey('SeriesArtwork', on_delete=models.PROTECT)
    season = models.IntegerField(verbose_name="Номер тома или сезона", null=True, blank=True)

    """Обложка"""
    image = models.ImageField(upload_to="artwork_covers/%Y/", verbose_name='Обложка', null=True, blank=True)

    """Количество эпизодов в произведении"""
    episodes = models.IntegerField(verbose_name="Количество глав/серий", null=True, blank=True)

    """К какой категории принадлежит работа, книга/сериал/новела/..."""
    category = models.ManyToManyField('CategoryArtwork', verbose_name='Категория/Жанры')

    """Год выхода"""
    year = models.IntegerField(verbose_name="Год", blank=True, null=True)

    """Описание"""
    description = models.TextField(blank=True, verbose_name="Описание")

    """Автор"""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, verbose_name='Автор', blank=True, null=True)

    """Пользовательские данные"""
    creator = models.ManyToManyField(User, verbose_name='Автор записи')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи", blank=True)

    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    activeted = ActivitedManager()

    type_artwork = models.ForeignKey('TypeArtwork', on_delete=models.PROTECT, verbose_name="Тип произведения", blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artwork_by_slug', kwargs={'art_slug': self.slug})


class AlternativeName (models.Model):
    title = models.CharField(max_length=256, verbose_name='Альтернативное название')

    def __str__(self):
        return self.title


class CategoryArtwork (models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")

    def __str__(self):
        return self.name


class SeriesArtwork(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name="Имя/Псевданим")

    def __str__(self):
        return self.name


class TypeArtwork(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название типа произведения")

    def __str__(self):
        return self.title
