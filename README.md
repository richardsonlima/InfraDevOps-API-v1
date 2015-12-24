===============================
InfraDevOps-API
===============================

**InfraDevOPS API ** is a Python API written with Flask Micro Framework to collect servers health data.

Follow me on Twitter: `@InfraDevOps`

Installation
============

Install over Git
---------------------------

git clone https://github.com/richardsonlima/InfraDevOps-API-v1.git 


System Requirements:
---------------------------
- ``Centos Linux 7.1`` 

Install Epel repo:
---------------------------

    $ wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
   
    $ sudo rpm -Uvh epel-release-latest-7.noarch.rpm
   
Database Requirements:
---------------------------


* Install MySQL Server:
---------------------------

    $ wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
   
    $ sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
   
    $ sudo yum update
   
    $ sudo yum install mysql-server
   
    $ sudo systemctl start mysqld
   
    $ sudo mysql_secure_installation
    

* Create Database Environment:
---------------------------  

    mysql -u root -p
    
    CREATE DATABASE api;
    
    CREATE USER 'apiuser'@'localhost' IDENTIFIED BY 'password';
    
    CREATE USER 'apiuser'@'%' IDENTIFIED BY 'password';
    
    GRANT ALL PRIVILEGES ON api.* TO 'apiuser'@'localhost';
  
    GRANT ALL PRIVILEGES ON api.* TO 'apiuser'@'%';
  
    FLUSH PRIVILEGES;
  
    use api;
    
    CREATE TABLE `api`.`servermonitor` (`id` INT NOT NULL AUTO_INCREMENT, `sistema` VARCHAR(45) NULL, `hostname` VARCHAR(45) NULL, 
  `percentual_memoria` VARCHAR(45) NULL, `percentual_cpu` VARCHAR(45) NULL, `percentual_disco` VARCHAR(45) NULL, 
  `carga` VARCHAR(45) NULL, PRIMARY KEY (`id`));


* Create Database Dump:
---------------------------
  
   $ mysqldump -u root -p api > apidb_dump_bkp_orig.sql


* Python Requirements:
---------------------------

* Install ``pip`` , ``CentOS Development Tools (gcc ...), ``python-devel``, ``mysql-devel``, ``MySQL-python``, ``Flask Micro Framework`` :
````````    

    $ sudo yum -y install python-pip
    $ sudo pip install --upgrade pip
    $ sudo yum group install "Development Tools"
    $ sudo yum install python-devel mysql-devel
    $ sudo pip install MySQL-python
    $ sudo pip install flask

* Firewall Requirements:
---------------------------

    $ sudo systemctl status firewalldsu
    $ sudo firewall-cmd --state 
    $ sudo  firewall-cmd --zone=public --permanent --add-port=5000/tcp
    $ sudo firewall-cmd --reload

* Run API:
---------------------------

    $ python test_api_4.py
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
