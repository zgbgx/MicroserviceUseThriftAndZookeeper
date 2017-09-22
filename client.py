# -*- coding: utf-8 -*-

import thriftpy

from thriftpy.rpc import client_context
from zook import ZookWatcher
microservice_thrift = thriftpy.load("microservice.thrift", module_name="microservice_thrift")

class RpcClient():
    def __init__(self,zookhost,appname):
        self.zookhost=zookhost
        self.appname=appname
        self.zookclient=ZookWatcher(hosts=self.zookhost,appname=self.appname)
    def request(self):
        host,port=self.zookclient.getBalanceNode()
        with client_context(microservice_thrift.MicroService, host, port) as c:
            response = c.doResponse(str(port))
            print(response)

if __name__=='__main__':
    client=RpcClient('127.0.0.1:2181','doResponse')
    client.request()