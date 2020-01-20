#!/usr/bin/python


try:
	sudo rpm -Uvh https://yum.puppet.com/puppet6-release-el-7.noarch.rpm
	sudo yum install puppet -y
	exec bash -l
	systemctl start puppet
except:
	pass

systemctl restart puppet
