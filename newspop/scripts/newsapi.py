import requests
import json
import datetime
from pop.models import Article
from django.utils import timezone
import re
from scripts.searchapi import *

class API():
    def __init__(self):
        pass
    def get_article(self, url):
        #if '.' not in url[-10:]: #filter garbage
        if not re.search('\d\.\d', url[-10:]) or '/author/' in url:
            return False
        api_url = "https://api.viafoura.co/v2/www.cbc.ca/pages"
        headers={'User-Agent':'Hobby Project: Measuring News Popularity by Number of Comments'}
        payload='{\"url\":\"' + url + '\"}'
        response = requests.request("POST", api_url, headers=headers, data=payload)
        if response.status_code != 200:
            return False
        else:
            response = response.json()['result']
            data = {}
            data['full_page_url'] = response['full_page_url']
            data['title'] = response['title']
            data['description'] = response['description']
            data['date_created'] = timezone.make_aware(datetime.datetime.fromtimestamp(response['date_created']), timezone.get_current_timezone())
            data['num_replies'] = response['num_replies']
            data['image_url'] = response['image_url']
            return data
    def get_search_urls(self, page):
        api_url = f'https://www.cbc.ca/search_api/v1/search'
        params = {
            'q': 'cbc',
            'sortOrder': 'date',
            'media': 'all',
            'page': page,
            'fields': 'feed',
        }
        headers={'User-Agent':'Hobby Project: Measuring News Popularity by Number of Comments'}
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code != 200:
            return False
        medias = response.json()
        urls = []
        for media in medias:
            urls.append('https:'+media['url'])
        return urls
    def get_homepage_urls(self):
        url = 'https://www.cbc.ca/graphql'    
        payload="{\"query\":\"query {\\n        newscanada: allContentItems(lineupSlug: \\\"news-canada\\\",\\n            categorySlug: \\\"news-canada\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 50,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }\\n    } \\nfragment cardNode on ContentItem {\\n    id\\n    url\\n    urlSlug\\n    title\\n    sectionList\\n    sectionLabels\\n    relatedLinks {\\n        url\\n        title\\n        sourceId\\n    }\\n    deck\\n    description\\n    flag\\n    imageLarge\\n    source\\n    sourceId\\n    imageAspects\\n    publishedAt\\n    updatedAt\\n    sponsor {\\n        name\\n        logo\\n        url\\n        external\\n        label\\n    }\\n    type\\n    show\\n    authors {\\n        name\\n        image\\n    }\\n    commentsEnabled\\n    contextualHeadlines {\\n        headline\\n        contextualLineupSlug\\n    }\\n    mediaId\\n    mediaDuration\\n    headlineData {\\n        type\\n        title\\n        mediaId\\n        mediaDuration\\n        publishedAt\\n        image\\n    }\\n    components {\\n        mainContent {\\n            url\\n            urlSlug\\n            sectionList\\n            flag\\n            sourceId\\n            type\\n        }\\n        mainVisual {\\n            ... on ContentItem {\\n                mediaId\\n                mediaDuration\\n                title\\n                imageLarge\\n            }\\n        }\\n        primary\\n        secondary\\n        tertiary\\n    }\\n}\"}"
        #payload="{\"query\":\"query {\\n        newscanada: allContentItems(lineupSlug: \\\"news-canada\\\",\\n            categorySlug: \\\"news-canada\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newsworld: allContentItems(lineupSlug: \\\"news-world\\\",\\n            categorySlug: \\\"news-world\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newsbusiness: allContentItems(lineupSlug: \\\"news-business\\\",\\n            categorySlug: \\\"news-business\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newspolitics: allContentItems(lineupSlug: \\\"news-politics\\\",\\n            categorySlug: \\\"news-politics\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newsentertainment: allContentItems(lineupSlug: \\\"news-entertainment\\\",\\n            categorySlug: \\\"news-entertainment\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newsscience: allContentItems(lineupSlug: \\\"news-science\\\",\\n            categorySlug: \\\"science\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newshealth: allContentItems(lineupSlug: \\\"news-health\\\",\\n            categorySlug: \\\"news-health\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }newsindigenous: allContentItems(lineupSlug: \\\"news-indigenous\\\",\\n            categorySlug: \\\"news-indigenous\\\",\\n            subjectsSet: \\\"\\\",\\n            pageSize: 4,\\n            subjects: \\\"\\\",\\n            excludedCategorySet: \\\"\\\",\\n            tags: \\\"\\\",\\n            source: \\\"Polopoly\\\",\\n            typeSet: CBC_OCELOT) {\\n                nodes {\\n                    ...cardNode\\n                }\\n            }\\n    } \\nfragment cardNode on ContentItem {\\n    id\\n    url\\n    urlSlug\\n    title\\n    sectionList\\n    sectionLabels\\n    relatedLinks {\\n        url\\n        title\\n        sourceId\\n    }\\n    deck\\n    description\\n    flag\\n    imageLarge\\n    source\\n    sourceId\\n    imageAspects\\n    publishedAt\\n    updatedAt\\n    sponsor {\\n        name\\n        logo\\n        url\\n        external\\n        label\\n    }\\n    type\\n    show\\n    authors {\\n        name\\n        image\\n    }\\n    commentsEnabled\\n    contextualHeadlines {\\n        headline\\n        contextualLineupSlug\\n    }\\n    mediaId\\n    mediaDuration\\n    headlineData {\\n        type\\n        title\\n        mediaId\\n        mediaDuration\\n        publishedAt\\n        image\\n    }\\n    components {\\n        mainContent {\\n            url\\n            urlSlug\\n            sectionList\\n            flag\\n            sourceId\\n            type\\n        }\\n        mainVisual {\\n            ... on ContentItem {\\n                mediaId\\n                mediaDuration\\n                title\\n                imageLarge\\n            }\\n        }\\n        primary\\n        secondary\\n        tertiary\\n    }\\n}\"}"
        headers = {'Content-Type': 'application/json', 'User-Agent':'Hobby Project: Measuring News Popularity by Number of Comments'}
        response = requests.request("POST", url, headers=headers, data=payload).json()
        categories = response['data'].keys()
        urls = []
        for category in categories:
            for node in response['data'][category]['nodes']:
                urls.append(node['url'])
        return urls

def run(*args):
    cbc = API()
    #article_url = 'https://www.cbc.ca/news/business/green-bond-explainer-1.6394756'
    #print(cbc.get_article(article_url))
    dates = date_range()#[:50]
    for date in dates:
        urls = all_search_results(date)
        print(f'URLS: {urls}')
        for url in urls:
            print(url)
            a = cbc.get_article(url)
            print(a)
            if a:
                if len(Article.objects.filter(full_page_url=a['full_page_url'])) > 0:
                    print('already in database')
                else:
                    f_p_u = a['full_page_url']
                    if a['full_page_url'] == None:
                        f_p_u = url                        
                    Article.objects.create(full_page_url=f_p_u,
                    title=a['title'],
                    description=a['description'],
                    date_created=a['date_created'],
                    num_replies= a['num_replies'],
                    image_url=a['image_url'])

print('starting')
#run with: manage.py runscript newsapi