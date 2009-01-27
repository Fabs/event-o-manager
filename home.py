from django import http

def home_page(request):
    return http.HttpResponse("Hello World!")