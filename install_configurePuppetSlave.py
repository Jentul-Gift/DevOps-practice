#!/usr/bin/python
import os

try:
	os.system(sudo rpm -Uvh https://yum.puppet.com/puppet6-release-el-7.noarch.rpm)
	os.system(sudo yum install puppet -y)
	os.system(exec bash -l)
	os.system(systemctl start puppet)
except:
	pass

os.system(systemctl restart puppet)
