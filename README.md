===============================
InfraDevOps-API (Test)
===============================

**InfraDevOPS API ** is a Python API written with Flask Micro Framework to collect servers health data.

Follow me on Twitter: `@InfraDevOps`
Project Web Site: http://richardsonlima.github.io/InfraDevOps-API-v1

### Installation

Instructions on this page will guide you through installation process.  

git clone https://github.com/richardsonlima/InfraDevOps-API-v1.git 

### Dependencies

Supported python version is 2.7, below is the list of packages required to run project:

    $ sudo yum -y install python-pip
    $ sudo pip install --upgrade pip
    $ sudo yum group install "Development Tools"
    $ sudo yum install python-devel mysql-devel
    $ sudo pip install MySQL-python
    $ sudo pip install flask

### Provisioning with Docker

Comming soon =D

### System Dependencies (Centos 7.1)
Below are listed commands which will preper on a cloud server::

    $ wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    $ sudo rpm -Uvh epel-release-latest-7.noarch.rpm
    
Database environment::

    $ wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
    $ sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
    $ sudo yum update
    $ sudo yum install mysql-server
    $ sudo systemctl start mysqld
    $ sudo mysql_secure_installation
    
Create Database::

    $ mysql -u root -p
    CREATE DATABASE api;
    CREATE USER 'apiuser'@'localhost' IDENTIFIED BY 'password';
    CREATE USER 'apiuser'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON api.* TO 'apiuser'@'localhost';
    GRANT ALL PRIVILEGES ON api.* TO 'apiuser'@'%';
    FLUSH PRIVILEGES;
    use api;

Import Database Dump::

    $ wget https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/db_dump.sql
    $ mysql-u root -p api < db_dump.sql
  
Firewall Requirements::

    $ sudo systemctl status firewalld
    $ sudo firewall-cmd --state
    $ sudo  firewall-cmd --zone=public --permanent --add-port=5000/tcp
    $ sudo firewall-cmd --reload

Run API::
    
    $ wget https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/api.py .
    $ python api.py  
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!

Terminal session test::

[![asciicast](https://asciinema.org/a/32758.png)](https://asciinema.org/a/32758?autoplay=1)


Insert a new server test::

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"sistema": "LINUX", "hostname":"LNXSRV-TESTE005", "percentual_memoria":"50%", "percentual_cpu":"45%", "percentual_disco":"20%", "carga":"25%"}' http://10.101.0.7:5000/api/v1/collector/add
    
    OR 
    
    $ wget https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/agent_pycurl.py .
    $ python ./agent_pycurl.py

Request servers again to see what you just added::

    $ curl -i -X GET http://localhost:5000/api/v1/collector/view
    
Web browser access::

![alt tag](https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/docs/images/web_access_1.jpg)        
    
Using php to see your database inserts ::

    $ sudo yum install httpd
    $ sudo systemctl enable httpd.service
    $ sudo systemctl restart httpd.service
    $ sudo yum install php php-pear
    $ sudo yum install php-mysql
    $ sudo systemctl reload httpd
    $ sudo  firewall-cmd --zone=public --permanent --add-port=80/tcp
    $ sudo firewall-cmd --reload
    $ sudo systemctl reload httpd
    $ cd /var/www/html && wget https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/dash.php .
    
