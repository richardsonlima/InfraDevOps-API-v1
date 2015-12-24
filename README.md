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

    $ sudo yum -y install python-pip
    $ sudo pip install --upgrade pip
    $ sudo yum group install "Development Tools"
    $ sudo yum install python-devel mysql-devel
    $ sudo pip install MySQL-python
    $ sudo pip install flask

### Provisioning with Docker


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
    CREATE TABLE `api`.`servermonitor` (`id` INT NOT NULL AUTO_INCREMENT, `sistema` VARCHAR(45) NULL, `hostname` VARCHAR(45) NULL, 
  `percentual_memoria` VARCHAR(45) NULL, `percentual_cpu` VARCHAR(45) NULL, `percentual_disco` VARCHAR(45) NULL, 
  `carga` VARCHAR(45) NULL, PRIMARY KEY (`id`));
  
Firewall Requirements::

    $ sudo systemctl status firewalld
    $ sudo firewall-cmd --state
    $ sudo  firewall-cmd --zone=public --permanent --add-port=5000/tcp
    $ sudo firewall-cmd --reload

Run API::

    $ python api.py  
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
