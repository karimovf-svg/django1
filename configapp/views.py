from django.http import HttpResponse

def hello1(request):
    return HttpResponse("salom django")

def hello2(request):
    return HttpResponse("hello world")

def hello3(request):
    return HttpResponse("apple")
