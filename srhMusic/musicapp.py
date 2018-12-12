__author__  = 'levi'
from tornado import web, httpserver, ioloop;
from musicProject.functions import get_music_info_by_name;

class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.write('欢迎来到音乐网站公开主页！')
        self.render('index.html');

class GetMusicInfoHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        query = self.get_argument('query')
        music_info =  get_music_info_by_name(query)
        self.render('music.html',music=music_info)
application=web.Application([
    (r"/index", MainPageHandler),
    (r"/query", GetMusicInfoHandler),
])

if __name__ == '__main__':
    httpserver=httpserver.HTTPServer(application)
    httpserver.listen(8080)
    ioloop.IOLoop.current().start();