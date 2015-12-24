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

Database Dump::

    
-- MySQL dump 10.13  Distrib 5.6.28, for Linux (x86_64)
--
-- Host: localhost    Database: api
-- ------------------------------------------------------
-- Server version	5.6.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `servermonitor`
--

DROP TABLE IF EXISTS `servermonitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servermonitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sistema` varchar(45) DEFAULT NULL,
  `hostname` varchar(45) DEFAULT NULL,
  `percentual_memoria` varchar(45) DEFAULT NULL,
  `percentual_cpu` varchar(45) DEFAULT NULL,
  `percentual_disco` varchar(45) DEFAULT NULL,
  `carga` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servermonitor`
--
  
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
