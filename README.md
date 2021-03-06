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
    CREATE DATABASE ApiItemDb;
    CREATE TABLE `ApiItemDb`.`tblServers` (
    `IdServidor` INT NOT NULL AUTO_INCREMENT,
    `Sistema` varchar(45) DEFAULT NULL,
    `Hostname` varchar(45) DEFAULT NULL,
    `PercentualMemoria` varchar(45) DEFAULT NULL,
    `PercentualCpu` varchar(45) DEFAULT NULL,
    `PercentualDisco` varchar(45) DEFAULT NULL,
    `Carga` varchar(45) DEFAULT NULL,
    PRIMARY KEY (`IdServidor`));  
    CREATE USER 'apiuser'@'localhost' IDENTIFIED BY 'password';
    CREATE USER 'apiuser'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON ApiItemDb.* TO 'apiuser'@'localhost';
    GRANT ALL PRIVILEGES ON ApiItemDb.* TO 'apiuser'@'%';
    FLUSH PRIVILEGES;
    USE `ApiItemDb`;
    DROP procedure IF EXISTS `StoredProcedureCreateServer`;
    DELIMITER $$
    USE `ApiItemDb`$$
    CREATE PROCEDURE `StoredProcedureCreateServer` (  
    IN p_Hostname varchar(50),
    IN p_Sistema varchar(50),
    IN p_PercentualMemoria varchar(50),
    IN p_PercentualCpu varchar(50),
    IN p_PercentualDisco varchar(50),
    IN p_Carga varchar(50)
    )
    BEGIN
    if ( select exists (select 1 from tblServers where Hostname = p_Hostname) ) THEN
    insert into tblServers
    (
           Sistema,
           PercentualMemoria,
           PercentualCpu,
           PercentualDisco,
           Carga
     )
       values
     (
           p_Sistema,
           p_PercentualMemoria,
           p_PercentualCpu,
           p_PercentualDisco,
           p_Carga
      );

     ELSE
     insert into tblServers
     (
           Hostname,
           Sistema,
           PercentualMemoria,
           PercentualCpu,
           PercentualDisco,
           Carga
     )
     values
     (
           p_Hostname,
           p_Sistema,
           p_PercentualMemoria,
           p_PercentualCpu,
           p_PercentualDisco,
           p_Carga
      );
    END IF;
    END$$
    DELIMITER ;

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

Terminal tests::
[![asciicast](https://asciinema.org/a/32758.png)](https://asciinema.org/a/32758?autoplay=1) 


Insert a new server test::
  
    $ wget https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/agent_linux.py .
    $ python ./agent_linux.py

See the result below::

[![asciicast](https://asciinema.org/a/195341.png)](https://asciinema.org/a/195341)

Linux Agent Requirements (python version is 2.7) ::

    $ sudo pip install psutil
    $ sudo pip install pycurl
    
Linux Agent running::

![alt tag](https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/docs/images/agent_linux_4.jpg) 

MacOSx Agent Requirements (python version is 2.7) :: 

    $ sudo pip install psutil
    $ sudo pip install pycurl
    
MacOSx Agent running::

![alt tag](https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/docs/images/agent_macosx_4.jpg) 


Windows Agent Requirements (python version is 2.7) ::

    > pip install psutil
    > Install pycurl http://pycurl.sourceforge.net/download/pycurl-7.19.0.2.win32-py2.7.msi

Windows Agent running::

![alt tag](https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/docs/images/agent_win_4.jpg) 

See the result on database::

[![asciicast](https://asciinema.org/a/32762.png)](https://asciinema.org/a/32762)

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
    
![alt tag](https://raw.githubusercontent.com/richardsonlima/InfraDevOps-API-v1/master/docs/images/web_access_4.jpg) 

    
