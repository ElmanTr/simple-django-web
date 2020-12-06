from django import template
from ..models import Category, Data
from account.models import User
from django.db.models import Count, Q
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ من"

@register.inclusion_tag("portfolio/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.all(),
    }

@register.inclusion_tag("portfolio/partials/sidebararticles.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "articles": Data.objects.published().annotate(count = Count('hits', filter= Q(articlehit__created__gt=last_month))).order_by("-count","-date")[:5],
        "title": 'مقالات پربازدید ماه'
    }

@register.inclusion_tag("portfolio/partials/sidebararticles.html")
def hot_articles():
    last_month = datetime.today() - timedelta(days=30)
    content_type_id = ContentType.objects.get(app_label='portfolio', model='data').id
    return {
        "articles": Data.objects.published().annotate(count = Count('comments', filter= Q(comments__posted__gt=last_month) and Q(comments__content_type_id=content_type_id))).order_by("-count","-date")[:5],
        "title": 'مقالات داغ ماه'
    }

@register.inclusion_tag("portfolio/partials/best_authors.html")
def best_authors():
    last_month = datetime.today() - timedelta(days=30)
    a = User.objects.all().filter(is_author=True).annotate(count = Count('projects', filter= Q(projects__date__gt=last_month))).order_by("-count")
    b = User.objects.all().filter(is_superuser=True).annotate(count = Count('projects', filter= Q(projects__date__gt=last_month))).order_by("-count")
    return {
        "author": a | b
    }