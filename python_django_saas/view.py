from django.shortcuts import render
from saas1.models import BigBang
from django.http import HttpResponseRedirect
def hello(request):
    context = {}
    context['bigBangInfo'] = BigBang.objects.all()
    return render(request, 'hello.html', context)

def form(request):
    context = {}
    context['type'] = 'add'
    if 'nameInfo' in request.GET:
        context['type'] = 'update'
        context['nameInfo'] = request.GET['nameInfo']
        bigBangInfo = BigBang.objects.get(name=context['nameInfo'])
        context['age'] = bigBangInfo.age
        context['sex'] = bigBangInfo.sex
        context['score'] = bigBangInfo.score
    return render(request, 'form.html', context)

def addInfo(request):
    name = request.GET['username']
    age = request.GET['age']
    sex = request.GET['sex']
    score = request.GET['score']
    bigBangInfo = BigBang.objects.filter(name=name)
    if (bigBangInfo):
        bigBangInfo.update(age=age, sex=sex, score=score)
    else:
        bigBangInfo = BigBang(name=name, age=age, sex=sex, score=score)
        bigBangInfo.save()
    return HttpResponseRedirect('hello')

def delInfo(request):
    name = request.GET['username']
    bigBangInfo = BigBang.objects.filter(name=name)
    bigBangInfo.delete()
    return hello(request)

def updateForm(request):
    return form(request)
