#coding=utf-8
from kazoo.client import KazooClient
#from server import RpcServer
import logging
logging.basicConfig()
class ZookClient():
    def __init__(self,hosts):
        self.kazooclient=KazooClient(hosts=hosts) 
        self.kazooclient.start()
    def foundApp(self,appname):#添加app
        if self.kazooclient.exists('/'+appname):
            pass
        else:
            self.kazooclient.ensure_path('/'+appname)
    def foundNode(self,appname,port,host):#添加节点
        if self.kazooclient.exists('/'+appname+'/'+host+':'+str(port)):
            pass
        else:
            self.kazooclient.create('/'+appname+'/'+host+':'+str(port))
    def close(self):
        self.kazooclient.close()
    def register(self,appname,port,host):
        self.foundApp(appname)
        self.foundNode(appname, port, host)
#         self.close()