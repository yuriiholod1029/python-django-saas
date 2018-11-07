import time

def getNowTime():
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return nowTime