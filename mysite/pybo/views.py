from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")

