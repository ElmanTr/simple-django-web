from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ من"

@register.inclusion_tag("portfolio/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.all()
    }