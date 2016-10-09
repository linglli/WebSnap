'''
Created on Oct 7, 2016

@author: liling
'''
# coding:utf8
import urllib2
import cookielib

url = "http://www.baidu.com"

print 'The first way'
response1 = urllib2.urlopen(url)
print 'status code: ' + str(response1.getcode())
print 'content length: ' + str(len(response1.read()))

print 'The second way'
request  = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print 'status code: ' + str(response2.getcode())
print 'content length: ' + str(len(response2.read()))

print 'The third way'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print 'status code: ' + str(response3.getcode())
print 'content length: ' + str(len(response3.read()))
print 'cookie: ' + str(cj)
print 'content: ' + response3.read()

