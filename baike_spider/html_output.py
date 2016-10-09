# coding:utf8
'''
Created on Oct 7, 2016

@author: liling
'''
class HtmlOutput(object):
    def __init__(self):
        self.datas = []
        
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html><head><meta charset='UTF-8'></head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<th>url</th>")
        fout.write("<th>title</th>")
        fout.write("<th>summary</th>")
        fout.write("</tr>")
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    
    
