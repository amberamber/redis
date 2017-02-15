#!/usr/bin/python
#-*- coding: UTF-8 -*-
#sudo apt-get install py-redis -y
import os
import redis
class RedisHelper(object):
    '''RedisHelper 类用于:
    实现 ,增，删除，改，查
    1.通过单实例连接
    2.通过连接池来连接Redis
    3.通过单实例连接 获取 值
    4.通过连接池连接 获取 值
    5.通过连接池设置  新的 key value
    6.
    '''

    def __init__(self):
        path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
        redisFile = file("%s/utility/redis.ini" % (path),'r')
        lis = redisFile.readlines()
        self.host = lis[0].strip().split('=')[1]
        self.password = lis[1].strip().split('=')[1]
        self.port = lis[2].strip().split('=')[1]
        self.db = lis[3].strip().split('=')[1]
        self.charset = lis[4].strip().split('=')[1]
        print lis
        redisFile.close()
    def connRedis(self):
        try:
            #print self.charset
            self.conn = redis.Redis(host = self.host,password = self.password,port = int(self.port),db = self.db,charset=self.charset)
            return self.conn
        except redis.RedisError as e:
            print ("Redis Error %d: %s"% (e.args[0],e.args[1]))
    def connPool(self):
        try:
            #print self.charset
            #self.conn = redis.Redis(host = self.host,password = self.password,port = int(self.port),db = self.db,charset=self.charset)
            self.Pool = redis.ConnectionPool(host = self.host,password = self.password,port = int(self.port),db = self.db)
            self.rPool = redis.Redis(connection_pool=self.Pool)
            return self.rPool
        except redis.RedisError as e:
            print ("Redis Error %d: %s"% (e.args[0],e.args[1]))

    # #获取string型数据的key  方法  get_One
    # def get_One(self,redsql):
    #     #connredis = self.connRedis()
    #     return self.connRedis().get(redsql)
    # #获取连接池中 string型数据的key   方法 get_Pool
    # def get_Pool(self,redsql):
    #     #connpool = self.connPool()
    #     return self.connPool().get(redsql)
    # #设置连接池中 string 的新的 key: value
    # def set_Key(self,keysql,valuesql):
    #     return self.connPool().set(keysql,valuesql)


redishelp = RedisHelper()
#print  redishelp.connPool()
#print redishelp.get_Pool('a')
#print redishelp.get_One('b')
#print redishelp.get_Pool('c')

#print redishelp.set_Key('chenrui',1000)
#print redishelp.get_Pool('chenrui')

# print redishelp.connPool().get('chenrui')
# print redishelp.connPool().set('chenrui2',2000)
# print redishelp.connPool().save()
# print redishelp.connPool().get('chenrui2')
# print redishelp.connPool().info()

pip = redishelp.connPool() #.pipeline()
#pip.set ('aa',2)
#pip.set('bb',3)
print pip.get('aa')
print pip.get('bb')

#print redishelp.connPool().set('chenrui3',3000).rpush('chenrui4',4000).rpush('chenrui5',5000).execute()


