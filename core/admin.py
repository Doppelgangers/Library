from django.contrib import admin

from core.models import *


# Register your models here.

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    pass


@admin.register(AlternativeName)
class AlternativeNameAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryArtwork)
class CategoryArtworkAdmin(admin.ModelAdmin):
    pass


@admin.register(SeriesArtwork)
class SeriesArtworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeArtwork)
class TypeArtworkAdmin(admin.ModelAdmin):
    pass

