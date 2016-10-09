# coding:utf8
'''
Created on Oct 7, 2016

@author: liling
'''
#目标：百度百科Python词条相关词条网页－标题和简介
#入口页：http://baike.baidu.com/view/21087.htm
#URL格式：
#－－词条页面URL：/view/125370.htm
#数据格式：
#－－标题：<dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1></dd>
#－－简介：<div class="lemma-summary">***</div>
#页面编码：UTF-8
from baike_spider import url_manager, html_downloader, html_parser, html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d: %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                
                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'
            
        self.output.output_html()
    
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)