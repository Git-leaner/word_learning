from .db import DbConnection
import time

class WordModel(DbConnection):
    def get_word_by_name(self, word):
        try:
            self.connect()
            sql='select * from word where word = %s'
            self.cursor.execute(sql, (word))
            row=self.cursor.fetchone()
            if row:
                return row
        except  Exception as e:
            print(e)

    def save_word(self, **kwargs):
        try:
            print(kwargs, type(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())));
            c_time=time.strftime('%Y/%m/%d %H:%M:%S', time.localtime());
            self.connect()
            sql='insert into word (id,word, means, ph, c_time) VALUES (%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (0,kwargs['word'], kwargs['means'], kwargs['ph'],c_time ))
            self.close()
            return self.cursor.lastrowid
            print('成功插入', self.cursor.rowcount, '条数据')
        except Exception as e:
            print('word',e)

    def create_sign(self, **kwargs):
        try:
            self.connect()
            sql = 'insert into sing (word,department,num,time) VALUES (%s,%s,%s,%s)'
            self.cursor.execute(sql, (kwargs['word'], kwargs['department'], kwargs['num'], time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print('sing', e)