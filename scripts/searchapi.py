from serpapi import GoogleSearch
import datetime
from decouple import config
from pytz import utc

def date_range():
    dates = []
    date = datetime.date(2015,1,1)
    while date != datetime.date(2018,1,1):
        dates.append(date)
        date = date + datetime.timedelta(days=1)
    return dates

def get_prior_date():
    return datetime.datetime.now(utc).date() - datetime.timedelta(days=7)

def get_search_results(date_string,page_start):
    print(date_string,'PAGE START', page_start)
    search = GoogleSearch({
    "api_key": config('SERP_API_KEY'),
    "engine": "google",
    "q": "site:https://www.cbc.ca/news",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en",
    "tbs": f"cdr:1,cd_min:{date_string},cd_max:{date_string}",
    'start': f'{page_start}',
    "num": "100"
    })
    return search.get_dict()

def all_search_results(date):
    date_string = f'{date.month}/{date.day}/{date.year}'
    results = get_search_results(date_string,0)
    urls = [link['link'] for link in results['organic_results']]
    page_end = 100
    if 'pagination' in results:
        page_end = int(list(results['pagination']['other_pages'].keys())[-1]) * 100
        print(results['pagination'])
        print(f'{date} PAGE_ENDS: {page_end}')
        for page_start in range(100,page_end,100):
            results = get_search_results(date_string,page_start)
            if 'organic_results' in results:
                urls = urls + [link['link'] for link in results['organic_results']]
    return urls
