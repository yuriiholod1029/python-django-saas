from django.shortcuts import render
from saas1.models import BigBang
from django.http import HttpResponse

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['bigBangInfo'] = BigBang.objects.all()
    return render(request, 'hello.html', context)

def form(request):
    return render(request, 'form.html')

def addInfo(request):
    name = request.GET['username']
    age = request.GET['age']
    sex = request.GET['sex']
    score = request.GET['score']
    bigBangInfo = BigBang(name=name, age=age, sex=sex, score=score)
    bigBangInfo.save()
    return hello(request)

def delInfo(request):
    name = request.GET['username']
    bigBangInfo = BigBang.objects.filter(name=name)
    bigBangInfo.delete()
    return hello(request)
