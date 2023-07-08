-- MySQL dump 10.19  Distrib 10.3.29-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: Parqueadero1
-- ------------------------------------------------------
-- Server version	10.3.29-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuarios` (
  `Id_usuario` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(25) NOT NULL,
  `Contrasena` varchar(25) DEFAULT NULL,
  `Nom_usuario` varchar(255) DEFAULT NULL,
  `Fecha_alta` datetime DEFAULT NULL,
  `Telefono1` varchar(25) DEFAULT NULL,
  `Aviso_Emer` varchar(255) DEFAULT NULL,
  `TelefonoEmer` varchar(25) DEFAULT NULL,
  `Sucursal` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuarios`
--

LOCK TABLES `Usuarios` WRITE;
/*!40000 ALTER TABLE `Usuarios` DISABLE KEYS */;
INSERT INTO `Usuarios` VALUES (1,'AG','13579','Aurelio Guarneros Ruiz',NULL,NULL,NULL,NULL,NULL),(2,'FRANCISCO','FHM','Juan Francisco Hernandez Morales',NULL,NULL,NULL,NULL,NULL),(3,'ARMANDO','ASP','Armando Salazar Perdomo',NULL,NULL,NULL,NULL,NULL),(4,'LAURA','LCF','Laura Janet Cruz Flores',NULL,NULL,NULL,NULL,NULL),(5,'HERIBERTO','HSO','Heriberto Salazar Ocaña',NULL,NULL,NULL,NULL,NULL),(6,'BERNARDO','BG','Bernardo Garcia',NULL,NULL,NULL,NULL,NULL),(7,'HECTOR','HMM','Hector Agustin Martinez Miranda',NULL,NULL,NULL,NULL,NULL),(8,'TACHO','EB','Eustaquio Bautista',NULL,NULL,NULL,NULL,NULL),(9,'DANY','DS','Daniela Santiago',NULL,NULL,NULL,NULL,NULL),(10,'ARTEMIO','AR','Artemio Ramirez',NULL,NULL,NULL,NULL,NULL),(11,'MANUEL','JMM','José Manuel Marín',NULL,NULL,NULL,NULL,NULL),(12,'BELEN','BBB','Belen Becerril Berrozabal',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-15 22:31:22
