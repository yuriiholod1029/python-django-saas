# -*- coding: UTF-8 -*-
import urllib,urllib2
import BeautifulSoup
import sys
import json
from saas1 import models
reload(sys)
sys.setdefaultencoding('utf-8')
def grabDataFromUrl(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    result = soup.findAll('td')
    dict = {}
    list = []
    for li in result:
        if li.find('a', attrs={"class": ""}) is not None:
            title = li.find('a', attrs={"class": ""}).text.split(' ')[0]
            content = li.find('p', attrs={"class": "pl"}).text
            movieInfos = models.movieInfo.objects.filter(title=title);
            if(movieInfos):
                movieInfos.update(content=content)
            else:
                movieInfos = models.movieInfo(title=title, content=content)
                movieInfos.save()
            #dict.append({'title': title, 'content': content})
            #dict['title'] = title
            #dict['content'] = content
            #json.dumps(dict, encoding="UTF-8", ensure_ascii=False)
            #list.append(json.dumps(dict).decode("unicode-escape"))
    #print dict
    #json.dumps(dict, encoding="UTF-8", ensure_ascii=False)
    #str(list).replace('u\'', '\'')
    #list = str(list).decode('unicode-escape')
    #print list
    #return list
#grabDataFromUrl("http://movie.douban.com/chart")