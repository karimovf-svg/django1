from django.http import HttpResponse

def bye(request):
    return HttpResponse("xayr django")

def bye2(request):
    return HttpResponse("xayr world")

def bye3(request):
    return HttpResponse("apple")