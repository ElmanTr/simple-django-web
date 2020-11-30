from django import template
from ..models import Category, Data
from account.models import User
from django.db.models import Count, Q
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ من"

@register.inclusion_tag("portfolio/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.all(),
    }

@register.inclusion_tag("portfolio/partials/popular_articles.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "articles": Data.objects.published().annotate(count = Count('hits', filter= Q(articlehit__created__gt=last_month))).order_by("-count","-date")[:5]
    }

@register.inclusion_tag("portfolio/partials/best_authors.html")
def best_authors():
    last_month = datetime.today() - timedelta(days=30)
    a = User.objects.all().filter(is_author=True).annotate(count = Count('projects', filter= Q(projects__date__gt=last_month))).order_by("-count")
    b = User.objects.all().filter(is_superuser=True).annotate(count = Count('projects', filter= Q(projects__date__gt=last_month))).order_by("-count")
    return {
        "author": a | b
    }