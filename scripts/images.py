import requests
import os
from pop.models import Article

def image_download(image_url):
    file_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'images'))
    file_name = image_url.replace('/','').replace(':','')
    if not os.path.exists(f'{file_path}\{file_name}'):
        img_data = requests.get(image_url).content
        with open(f'{file_path}\{file_name}', 'wb') as handler:
            handler.write(img_data)
    else:
        print('exists')

def run(*args):
    for year in range(2015,2018+1):
        for month in range(1,12+1):
            if year == 2022 and month == 5:
                break
            else:
                articles = Article.objects.all().filter(date_created__year=year).filter(date_created__month=month).order_by('-num_replies')[:50]
                for article in articles:
                    print(year,month,article.title)
                    image_download(article.image_url)