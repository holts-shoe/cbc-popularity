from django import template

register = template.Library()

@register.filter
def local_image(image_url):
    return image_url.replace('/','').replace(':','')