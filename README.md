===============================
InfraDevOps-API
===============================

**InfraDevOPS API ** is a Python API written with Flask Micro Framework to collect servers health data.

Follow me on Twitter: `@InfraDevOps`

### Installation

Instructions on this page will guide you through installation process.  

git clone https://github.com/richardsonlima/InfraDevOps-API-v1.git 

### Dependencies

Supported python version is 2.7, below is the list of packages required to run project:

.. include:: ../requirements.txt
   :literal:

### Provisioning with Docker


### Create the environment
Below are listed commands which will setup full-stack API instance on a cloud server::

    $ wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    $ sudo rpm -Uvh epel-release-latest-7.noarch.rpm
    
Database environment::

    $ wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
    $ sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
    $ sudo yum update
    $ sudo yum install mysql-server
    $ sudo systemctl start mysqld
    $ sudo mysql_secure_installation
    
