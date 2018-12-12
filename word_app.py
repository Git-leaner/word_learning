__author__='levi'
from tornado import web,ioloop,httpserver
from  word_learning.functions import spider_word_by_name
from  word_learning.dbmodel import models

import os,json

class MainPageHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('欢迎使用单词助记系统！')
        self.render('index.html')

class ListPageHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('list.html')
# 查询单词
class SearchHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        word=self.get_argument('word');
        print(word);
        module = models.WordModel()
        word_info = module.get_word_by_name(word)
        if word_info:
            print(word_info['means'])
            print('ph', word_info['ph'])
            self.write({
                'word':word,
                'means':word_info['means'].split('/'),
                'ph':word_info['ph'].split('/')
            })
        else:
            means, ph = spider_word_by_name(word)
            print(means, ph)
            word_id = module.save_word(word=word, means=means, ph=ph)
            if word_id:
                print('保存成功', word, ph)
                print(means)
                self.write({
                    'word':word,
                    'means':means.split('/'),
                    'ph':ph.split('/')
                })
            else:
                self.write('保存失败')
    def post(self, *args, **kwargs):
        print(self.get_argument('word'));
        # data = json.loads(self.request.body)
        word=self.get_argument('word');
        # word=self.get_body_argument('word');
        # sign=self.get_body_argument('sign');
        # token=self.get_body_argument('token');
        module=models.WordModel()
        word_info=module.get_word_by_name(word)
        if word_info:
            print(word_info['means'])
            print('ph',word_info['ph'])
            self.render('search.html',
                       word=word,
                       means=word_info['means'].split('/'),
                       ph=word_info['ph'].split('/')
                       )
        else:
            means,ph=spider_word_by_name(word)
            print(means,ph)
            word_id=module.save_word(word=word, means=means, ph=ph)
            if word_id:
                print('保存成功',word,ph)
                print(means)
                self.render('search.html',
                            word=word,
                            means=means.split('/'),
                            ph=ph.split('/')
                            )
            else:
                self.write('保存失败')

settings={
    # "static_path": os.path.join(os.path.dirname(__file__),"static")
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),  #静态文件
    'template_path': os.path.join(os.path.dirname(__file__),'template')  #模板文件
    }#配置静态文件路径
application=web.Application([
    (r'/',MainPageHandle),
    (r'/search', SearchHandler),
    (r'/list', ListPageHandle)
],**settings)

if __name__ == '__main__':
    httpserver = httpserver.HTTPServer(application)
    httpserver.listen(8087)
    ioloop.IOLoop.current().start()