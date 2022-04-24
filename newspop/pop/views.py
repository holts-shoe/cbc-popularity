from django.http import HttpResponse
from django.template import loader
from .models import Article
from django.shortcuts import render
import datetime

def index(request):
    month = request.GET.get("month", None)
    year = request.GET.get("year", None)
    if year and month:
        print(year, month)
        articles = Article.objects.all().filter(date_created__year = year, date_created__month = month)
    elif year:
        print(year)
        articles = Article.objects.all().filter(date_created__year = year)
    else:
        articles = Article.objects.all()
    latest_article_list = articles.order_by('-num_replies')[:50]
    years = list(range(2022,2020,-1))
    months = {month: datetime.date(1900, month, 1).strftime('%B') for month in range(1,12+1)}
    context = {'latest_article_list':latest_article_list, 'years': years, 'months': months, 'selected_year': year, 'selected_month': month}
    return render(request, 'pop/index.html', context)

def detail(request, article_id):
    return HttpResponse(f"You're looking at article {article_id}")
