import logging
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

#__name__ ==> "shop.views"
logger = logging.getLogger(__name__)

#view 호출에 대한 리턴값은 HttpResponse객체
def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q','')
    if q:
        qs.filter(name__icontains=q)

    logger.debug('query : {}'.format(q))

    return render(request, 'shop/item_list.html',{
        'item_list':qs,
        'q' : q,
    })