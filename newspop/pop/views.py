from django.http import HttpResponse
from django.template import loader
from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-num_replies')[:50]
    template = loader.get_template('pop/index.html')
    context = {'latest_article_list': latest_article_list}
    return HttpResponse(template.render(context, request))

def detail(request, article_id):
    return HttpResponse(f"You're looking at article {article_id}")
