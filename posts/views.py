from django.http import HttpResponse


def index(request):
    return HttpResponse('main page')


def group_posts(request, name):
    return HttpResponse(f'{name} page')
