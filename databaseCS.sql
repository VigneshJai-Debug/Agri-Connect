-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: agriconnect
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `uid` char(8) NOT NULL,
  `oid` int DEFAULT NULL,
  `qty` int NOT NULL,
  KEY `oid` (`oid`),
  KEY `uid` (`uid`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`oid`) REFERENCES `inventory` (`oid`),
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `register` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES ('ath@2023',101,5);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `oid` int NOT NULL,
  `product` varchar(60) DEFAULT NULL,
  `unit_price` int DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `image_url` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (101,'Basmati Rice',70,95,'https://5.imimg.com/data5/IOS/Default/2023/6/317693859/AP/JO/NR/155543594/product-jpeg-1000x1000.png'),(102,'Wheat Flour',45,100,'https://5.imimg.com/data5/RG/YW/MY-21924532/wheat-flour-500x500.jpg'),(103,'Soybean',60,80,'https://tempehchennai.in/cdn/shop/products/5c7d316714fc001b8d66e53ed799b545.jpg'),(104,'Onion',60,70,'https://familyneeds.co.in/cdn/shop/products/2_445fc9bd-1bab-4bfb-8d5d-70b692745567_600x600_crop_center.jpg'),(105,'Potato',50,45,'https://m.media-amazon.com/images/I/61yXL70-RaL._SL1500_.jpg');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `register` (
  `id` int NOT NULL,
  `name` varchar(40) NOT NULL,
  `email_id` varchar(30) NOT NULL,
  `phone_no` bigint NOT NULL,
  `State` varchar(40) NOT NULL,
  `District` varchar(40) NOT NULL,
  `town_vill` varchar(50) NOT NULL,
  `status` char(8) NOT NULL,
  `uid` char(8) NOT NULL,
  `pass` char(8) NOT NULL,
  `address` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid` (`uid`),
  UNIQUE KEY `pass` (`pass`),
  UNIQUE KEY `email_id_2` (`email_id`),
  UNIQUE KEY `phone_no` (`phone_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (0,'Vignesh Jaisankar','xyz@gmail.com',1234567899,'Kerala','Ernakulam','Perumbavoor','Admin','viki2006','viki2006','...'),(4501,'Athul Krishna BS','leo@gmail.com',2067676767,'West Bengal','u know','ha','Customer','ath@2023','ath@2023','...'),(4502,'Karthik S Prakash','kaka@gmail.com',1290909090,'Andhra Pradesh','hello','world','Customer','kaka2023','kaka2023','...'),(9002,'Joyal Thomas','abc@gmail.com',2090909090,'Goa','abc','idk','Producer','jo@@2023','jo@@2023','...'),(9003,'R Devanarayanan','dev@gmail.com',1234567890,'Andhra Pradesh','blah','blah','Producer','deva2023','deva2023','...');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `sale` (
  `uid` char(8) NOT NULL,
  `oid` int DEFAULT NULL,
  `qty` int DEFAULT NULL,
  KEY `oid` (`oid`),
  CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`oid`) REFERENCES `inventory` (`oid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES ('kaka2023',101,5),('kaka2023',102,5),('jo@@2023',101,1);
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-07 10:39:53
