from django import template
from time import  time
from django.conf import settings
from django.templatetags.static import StaticNode

register = template.Library()

class FreshStaticNode(StaticNode):
    #url 계산
    def url(self, context):
        url = super().url(context)
        if settings.DEBUG:
            url += '?_={}'.format(int(time())) #Dummy Query String 추가
        return url

@register.tag('fresh_static')
def do_static(parser, token):
    return FreshStaticNode.handle_token(parser, token)