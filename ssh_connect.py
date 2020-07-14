#!/bin/env python

#-*- coding: utf-8 -*-

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# <원격지 시스템주소>
host=""
# <원격지 시스템 포트>
port_num =""
#<관리자 ID>
user = ""
#<관리자 암호>
pw = ""
client.connect(hostname=host,port=port_num,username=user,password=pw)
print(client)
client.close()