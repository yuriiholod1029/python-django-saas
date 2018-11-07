# -*- coding: UTF-8 -*-
from django.shortcuts import render
from saas1.models import BigBang,movieInfo, MessageBox
from django.http import HttpResponseRedirect
from saas1 import grabData,utils
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

def communicate(request):
    data = {}
    #info = grabData.grabDataFromUrl("http://movie.douban.com/chart")
    #data['webInfo'] = info.replace('\n', '\\n')
    data['dbWebInfo'] = movieInfo.objects.all()
    #print(type(info))
    return render(request, 'communicate.html', data)

def msgForm(request):
    title = request.GET['title']
    movieContent = request.GET['contents']
    print(title)
    context={}
    #movieInfos = movieInfo.objects.filter(title=title)
    context['title'] = title
    context['contentInfo'] = movieContent
    context['friends'] = BigBang.objects.all()
    return render(request, 'msgForm.html', context)

def msgBox(request):
    title = request.GET['title']
    message = request.GET['message']
    info = request.GET['info']
    msgFrom = ''
    msgTo = request.GET['msgTo']
    time = utils.getNowTime()
    msg = MessageBox(title=title, content=message, info=info, msgFrom=msgFrom, msgTo=msgTo, time=time)
    msg.save()
    return HttpResponseRedirect('msgCenter')

def msgCenter(request):
    context = {}
    context['msgInfo'] = MessageBox.objects.all()
    return render(request, 'message.html', context)