# MicroserviceUseThriftAndZookeeper
use kazoo  thriftpy package and zookeeper to build a microservice demo  
this demo  use  thriftpy and  kazoo to build microservice.<br>
about thritfpy you can browse https://github.com/eleme/thriftpy<br>
about kazoo you can browse https://github.com/python-zk/kazoo<br>
also you must install zookeeper in your machine<br>
## about code
when you start server,you will register a app in zookeeper(if the app doesn't exist),and then register a node under the app in zookeeper.<br>
when you request server by client,you will get a random node under the app.

