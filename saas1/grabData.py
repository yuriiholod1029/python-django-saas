import urllib,urllib2

def grabDataFromUrl(url):
    html = urllib2.urlopen(url).read()
    return html
print grabDataFromUrl("http://www.baidu.com")