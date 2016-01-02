-- MySQL dump 10.13  Distrib 5.6.28, for Linux (x86_64)
--
-- Host: localhost    Database: ApiItemDb
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
-- Table structure for table `tblServers`
--

DROP TABLE IF EXISTS `tblServers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblServers` (
  `IdServidor` int(11) NOT NULL AUTO_INCREMENT,
  `Sistema` varchar(45) DEFAULT NULL,
  `Hostname` varchar(45) DEFAULT NULL,
  `PercentualMemoria` varchar(45) DEFAULT NULL,
  `PercentualCpu` varchar(45) DEFAULT NULL,
  `PercentualDisco` varchar(45) DEFAULT NULL,
  `Carga` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IdServidor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblServers`
--


--
-- Dumping routines for database 'ApiItemDb'
--
/*!50003 DROP PROCEDURE IF EXISTS `StoredProcedureCreateServer` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `StoredProcedureCreateServer`(

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

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-31  6:02:08