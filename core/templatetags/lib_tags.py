from django import template
import core.views as views

register = template.Library()


@register.simple_tag()
def get_menu():
    return views.menu


@register.inclusion_tag("core/navbar.html")
def show_navbar():
    menu = views.menu
    return {'menu': menu}
