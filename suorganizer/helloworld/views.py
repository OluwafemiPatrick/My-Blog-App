from django.http import HttpResponse


def greeting(request):
    return HttpResponse('Hello world, it\'s Oluwafemi...')