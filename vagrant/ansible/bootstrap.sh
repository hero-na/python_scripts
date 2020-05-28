#! /usr/bin/env bash

##install ansible
yum install epel-release -y
yum install ansible -y

## inint environment for vagrant Only 
mkdir -p /home/vagrant/.vim/autoload /home/vagrant/.vim/bundle
touch /home/vagrant/.vimrc
touch /home/vagrant/.bashrc