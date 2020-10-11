# _*_ encoding:utf-8 _*_
# Author: renxk
# date: 2020/10/9 2:59 下午


from pymysql import connect, cursors


class DB:
    def __init__(self, host = 'localhost', port = 3306, db = 'TESTDB', user = 'root', password = 'renxukui123', charset='utf8'):
        #建立连接
        self.conn = connect(host = host, port = port, db = db, user = user, password = password, charset = charset)

        #创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = cursors.DictCursor)

    def __enter__(self):
        #返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        #提交数据库并执行
        self.conn.commit()

        #关闭游标
        self.cur.close()

        #关闭数据库连接
        self.conn.close()

