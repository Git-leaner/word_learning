__author__='levi'
from tornado import httpserver,web,ioloop
import os,json,random
# import face_recognition
from Array_Face_login.py_mysql import InsertTable,updTable,delTable,selectTable,closeConnect
# from py_mysql import execute_queries

class MainPageHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class RegistPageHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')
    def post(self, *args, **kwargs):
        print(self.request.headers.get("Content-Type"))  # 获取请求数据类型
        # imgBase64=self.request.body;
        imgBase64=self.get_argument('imgBase64')
        print(imgBase64);
        sql = "INSERT INTO face_login (id, base64) VALUES ( %.2f , '%s')"
        data = (0 , imgBase64)
        InsertTable(sql,data)
        self.redirect('/')

class AjaxReqHandle(web.RequestHandler):
    def post(self, *args, **kwargs):
        sql = "SELECT id,base64 FROM face_login WHERE id = '%s' "
        data = (0)
        selectTable(sql,data)
        self.write('123')

class SuccessHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('success.html')

settings={"static_path": os.path.join(os.path.dirname(__file__),"static")}#配置静态文件路径
application=web.Application([
    (r'/',MainPageHandle),
    (r'/register',RegistPageHandle),
    (r'/faceck',AjaxReqHandle),
    (r'/success', SuccessHandle)
],**settings)

if __name__ == '__main__':
    httpserver = httpserver.HTTPServer(application)
    httpserver.listen(8086)
    ioloop.IOLoop.current().start()