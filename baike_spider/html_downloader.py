# coding:utf8
'''
Created on Oct 7, 2016

@author: liling
'''
import urllib2
class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None or len(url) == 0:
            return None
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    
