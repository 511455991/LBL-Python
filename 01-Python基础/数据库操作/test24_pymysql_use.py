# encoding=utf-8

"""
使用pymysql封装操作mysql数据库的功能，增删改查
author：LBL
date:2023-2-13
"""
import pymysql


class DBUtil():
    """ 工具类，其他程序可直接调用 """
    # 初始化变量,避免脏数据
    __conn = None
    __cursor = None


    @classmethod
    def __get_conn(cls):
        """ 私有类方法，创建游标对象 """
        # 如果没有连接对象才会创建，指定地址、端口、用户名、密码、数据库
        if cls.__conn == None:
            cls.__conn = pymysql.connect(host='localhost',
                                         port=3306,
                                         user='root',
                                         password='123456',
                                         database='db1')
        return cls.__conn

    @classmethod
    def __get_cursor(cls):
        """ 私有类方法，创建游标对象 """
        # 如果没有游标对象才会创建
        if cls.__cursor == None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor


    @classmethod
    def exec_sql(cls,sql):
        """ 类方法，执行传入的sql语句 """
        try:
            cursor = cls.__get_cursor()
            cursor.execute(sql)
            # 如果sql语句是查询语句，直接返回所有查询结果
            if sql.split()[0].lower == "select":
                return cursor.fetchall()
            # 如果不是查询语句，就需要手动提交语句，返回被影响行数
            else:
                cls.__conn.commit()
                return cursor.rowcount
        # 出现异常，打印异常信息，回滚事务
        except Exception as e:
            print(e)
            cls.__conn.rollback()
        # 关闭游标、关闭连接
        finally:
            cls.__cursor.close()
            cls.__cursor = None
            cls.__conn.close()
            cls.__conn = None



# 程序主入口
if __name__ == "__main__":
    """ pymysql可操作mysql数据库，安装 pip install pymysql ，
    操作过程：1、创建链接对象conn
            2、获取游标对象cursor
            3、执行sql
            4、关闭游标、关闭连接
    pymysql默认开启了事务，即：所有修改数据库的操作不会自动提交，执行后需要手动提交或回滚
    """
    pass
    sql1 = "insert into tb_user(id,username,password) values(3 ,'xiaohong','123')"    # 插入语句
    sql2 = "update tb_user set password='789' where id='3' ;"  # 更新表中数据
    sql3 = "delete from tb_user where id='3';"                 # 删除表中数据
    sql4 = "select * from tb_user;"
    DBUtil.exec_sql(sql4)