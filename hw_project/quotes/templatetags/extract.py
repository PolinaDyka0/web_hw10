#
# from django import template
#
# from ..utils import get_mongodb
#
# register = template.Library()
#
#
# def get_author(id_):
#     db = get_mongodb()
#     author = db.authors.find_one({'_id': id_})
#     return author['fullname']
#
#
# register.filter('author', get_author)
#
#
from django import template
from django.db.models import ObjectDoesNotExist

from ..models import Author, Tag

register = template.Library()

@register.filter(name='author')
def get_author(author_id):
    try:
        author = Author.objects.get(id=author_id)
        return author.fullname
    except ObjectDoesNotExist:
        return 'Unknown author'

@register.simple_tag(name='tags')
def get_tags(quote_id):
    tags = Tag.objects.filter(quote__id=quote_id)
    return tags
