-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: internet_service_information_management_system
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `Bill_id` int NOT NULL,
  `Customer_id` int DEFAULT NULL,
  `DataPlan_id` int DEFAULT NULL,
  `Registration_date` date DEFAULT NULL,
  `Duration` int DEFAULT NULL,
  `total_amount` int DEFAULT NULL,
  PRIMARY KEY (`Bill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,1,1,'2021-01-01',10,1890),(2,1,2,'2021-01-01',7,1533),(3,2,1,'2021-01-01',10,1890),(4,3,2,'2021-01-01',5,1095),(10,1,3,'2021-01-01',36,9324);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Customer_id` int NOT NULL,
  `Customer_name` varchar(50) DEFAULT NULL,
  `Customer_phoneNumber` int DEFAULT NULL,
  `Customer_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Đỗ Thanh Hiếu',387797116,'Hà Nội'),(2,'Trần Trung Hiếu',123456789,'335 Cầu Giấy, Hà Nội'),(3,'Đỗ Đình Phúc',999911111,'135 Cầu Giấy, Hà Nội'),(4,'Nguyễn Viết Nhân',999911111,'18 Hoàng Quốc Việt, Cầu Giấy, Hà Nội'),(5,'Phí Nguyễn Hải Minh',555566666,'Tầng 2 tòa nhà Ellipse Tower, 110 Trần Phú'),(6,'Đinh Quang',2314232,'Hà Nội');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataplan`
--

DROP TABLE IF EXISTS `dataplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataplan` (
  `dataPlan_id` int NOT NULL,
  `dataPlan_name` varchar(50) DEFAULT NULL,
  `dataPlan_speed` varchar(50) DEFAULT NULL,
  `dataPlan_price_per_month` int DEFAULT NULL,
  PRIMARY KEY (`dataPlan_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataplan`
--

LOCK TABLES `dataplan` WRITE;
/*!40000 ALTER TABLE `dataplan` DISABLE KEYS */;
INSERT INTO `dataplan` VALUES (1,'Gói Home 1','30 Mbps',189),(2,'Gói Home 2','50 Mbps',219),(3,'Gói Home 3','70 Mbps',259);
/*!40000 ALTER TABLE `dataplan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-25 17:53:40
