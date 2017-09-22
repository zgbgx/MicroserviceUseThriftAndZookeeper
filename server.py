#coding=utf-8

import thriftpy
from zookclient import ZookClient
from thriftpy.rpc import make_server
microservice_thrift = thriftpy.load("microservice.thrift", module_name="microservice_thrift")


class Dispatcher(object):
    def doResponse(self,a):
        print("doReponse!")
        return 'response is'+a
class RpcServer():
    def __init__(self,host,port,appname,zookhost):
        self.port=port
        self.host=host
        self.appname=appname
        self.zookhost=zookhost
    def startServer(self):
        server = make_server(microservice_thrift.MicroService, Dispatcher(),
                             self.host, self.port)
        client=ZookClient(hosts=self.zookhost)
        client.register(self.appname, self.port, self.host)
        server.serve()#启动服务
if __name__=='__main__':
    server=RpcServer('127.0.0.1',8000,'doResponse','127.0.0.1:2181')
    server.startServer()