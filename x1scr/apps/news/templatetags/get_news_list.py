from x1scr.apps.news.models import News

from django import template
register = template.Library()


@register.inclusion_tag('news.html')
def pull_latest_news(howmany=3):
    news = News.objects.filter(published=True).order_by('-date_published')[:howmany]
    return dict(news=news)
