-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: xinjiang
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `documents`
--

DROP TABLE IF EXISTS `documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documents` (
  `id` int NOT NULL AUTO_INCREMENT,
  `parallel_title` varchar(45) DEFAULT NULL,
  `alternate_title` varchar(45) DEFAULT NULL,
  `other_title_info` varchar(45) DEFAULT NULL,
  `individual_name` varchar(45) DEFAULT NULL,
  `group_name` varchar(45) DEFAULT NULL,
  `conference_name` varchar(45) DEFAULT NULL,
  `joint_author_name` varchar(45) DEFAULT NULL,
  `other_info` varchar(45) DEFAULT NULL,
  `bearing_method` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `pro_loca` varchar(45) DEFAULT NULL,
  `producer` varchar(45) DEFAULT NULL,
  `public_date` varchar(45) DEFAULT NULL,
  `release_date` varchar(45) DEFAULT NULL,
  `create_date` varchar(45) DEFAULT NULL,
  `abstract` varchar(300) DEFAULT NULL,
  `catalog` varchar(45) DEFAULT NULL,
  `award` varchar(45) DEFAULT NULL,
  `notes` varchar(45) DEFAULT NULL,
  `search_method` varchar(45) DEFAULT NULL,
  `key_word` varchar(45) DEFAULT NULL,
  `sum` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `audience` varchar(45) DEFAULT NULL,
  `resource` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `inclusion` varchar(45) DEFAULT NULL,
  `included` varchar(45) DEFAULT NULL,
  `copyright_holder` varchar(45) DEFAULT NULL,
  `copyright_notice` varchar(45) DEFAULT NULL,
  `authorize_person` varchar(45) DEFAULT NULL,
  `authorize_form` varchar(45) DEFAULT NULL,
  `authorize_date` varchar(45) DEFAULT NULL,
  `authorize_due` varchar(45) DEFAULT NULL,
  `authorize_area` varchar(45) DEFAULT NULL,
  `authorize_file` varchar(45) DEFAULT NULL,
  `authorize_info` varchar(45) DEFAULT NULL,
  `time_length` varchar(45) DEFAULT NULL,
  `space_length` varchar(45) DEFAULT NULL,
  `source_carrier` varchar(45) DEFAULT NULL,
  `collect_area` varchar(45) DEFAULT NULL,
  `collect_unit` varchar(45) DEFAULT NULL,
  `call_number` varchar(45) DEFAULT NULL,
  `collect_person` varchar(45) DEFAULT NULL,
  `process_unit` varchar(45) DEFAULT NULL,
  `serve_form` varchar(45) DEFAULT NULL,
  `serve_column` varchar(45) DEFAULT NULL,
  `serve_time` varchar(45) DEFAULT NULL,
  `serve_addr` varchar(45) DEFAULT NULL,
  `serve_obj` varchar(45) DEFAULT NULL,
  `acce_time` varchar(45) DEFAULT NULL,
  `acce_form` varchar(45) DEFAULT NULL,
  `acce_person` varchar(45) DEFAULT NULL,
  `acce_opi` varchar(45) DEFAULT NULL,
  `acce_repo` varchar(45) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `URL` varchar(100) DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents`
--

LOCK TABLES `documents` WRITE;
/*!40000 ALTER TABLE `documents` DISABLE KEYS */;
INSERT INTO `documents` VALUES (1,NULL,NULL,NULL,'张绍雯','山西师范大学音乐学院',NULL,NULL,NULL,NULL,NULL,'新疆',NULL,'2020-5','2020-5','2021-12-10','赛乃姆舞蹈是维吾尔族舞蹈的重要代表之一，自由灵活的表演形式使其深受维吾尔族人民的喜爱。在地域广阔的新疆维吾尔自治区，由于不同地区的人们生活方式与地理环境存在差异，使得各地区赛乃姆的舞蹈风格各具特色。',NULL,NULL,NULL,NULL,'维吾尔族，赛乃姆，风格特征',NULL,'pdf',NULL,'参花（上）','吉林省群众艺术馆',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'试论维吾尔族赛乃姆舞蹈的风格特征','resource/documents/试论维吾尔族赛乃姆舞蹈的风格特征_张绍雯.pdf','1494kb'),(2,NULL,NULL,NULL,'迪力牙尔·尼加提','喀什大学艺术学院',NULL,NULL,NULL,NULL,NULL,'新疆',NULL,'2016-2','2016-2','2021-12-10','本文首先简要介绍舞蹈艺术,其次主要叙述萨玛舞蹈具体的表演形式、传播范围、音乐特点、历史背景,展现萨玛舞蹈在当代舞台以及文艺活动中的表演形式,并提出了相关意见。',NULL,NULL,NULL,NULL,'萨玛舞蹈，表演形式，美学意义',NULL,'pdf',NULL,'音乐时空(理论版)','贵州省文学艺术界联合会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'维吾尔族萨玛舞蹈的特征与现状','resource/documents/维吾尔族萨玛舞蹈的特征与现状_迪力牙尔·尼加提.pdf','861kb'),(3,NULL,NULL,NULL,'张古力加马丽·吐尔荪','巴楚县文工团',NULL,NULL,NULL,NULL,NULL,'新疆',NULL,'2019-11','2019-11','2021-12-10','刀郎舞又称刀郎赛乃姆,是一种古老的民族舞,本文通过对刀郎舞的风格、特点和刀郎舞的形成进行详细的描述,全面了解刀郎舞。刀郎舞从很久之前流传下来,拥有大方、粗犷豪放的舞姿,充满了内蒙的劳动人民的气息,抒发自己的内心的情感,刀郎舞注重脚和手部的动作,身体的舞姿随着音乐的变化而变化。刀郎舞充分展示出了刀郎族人民的劳动智慧和打猎时的豪放。',NULL,NULL,NULL,NULL,'刀郎舞，形成，风格，特点',NULL,'pdf',NULL,'明日风尚(生活态度)','南京市文学艺术界联合会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'浅论刀郎舞的风格特点','resource/documents/浅论刀郎舞的风格特点_张古力加马丽·吐尔荪.pdf','131kb'),(4,NULL,NULL,NULL,'买买提·马木提','新疆艺术学院舞蹈系',NULL,NULL,NULL,NULL,NULL,'新疆',NULL,'2017','2017','2021-12-10','纳孜尔库姆舞蹈源于新疆吐鲁番麦西来普,孕育在\"吐鲁番十二木卡姆\"之中,是一种具有典型风格特征的民间歌舞娱乐形式,纳孜尔库姆将歌舞、器乐、竞技表演、各种民间娱乐和民俗风习结合在一起的综合艺术。',NULL,NULL,NULL,NULL,'	吐鲁番，纳孜尔库姆，舞蹈',NULL,'pdf',NULL,'戏剧之家(上半月)','湖北今古传奇传媒集团有限公司',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'维吾尔族舞蹈的璀璨明珠——谈纳孜尔库姆的艺术魅力','resource/documents/维吾尔族舞蹈的璀璨明珠——谈纳孜尔库姆的艺术魅力_买买提·马木提.pdf','2876kb');
/*!40000 ALTER TABLE `documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pictures`
--

DROP TABLE IF EXISTS `pictures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pictures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `URL` varchar(45) DEFAULT NULL,
  `individual_name` varchar(45) DEFAULT NULL,
  `group_name` varchar(45) DEFAULT NULL,
  `pro_loca` varchar(45) DEFAULT NULL,
  `pic_date` varchar(45) DEFAULT NULL,
  `create_date` varchar(45) NOT NULL,
  `release_date` varchar(45) DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  `resolution` varchar(45) DEFAULT NULL,
  `parallel_title` varchar(45) DEFAULT NULL,
  `alternate_title` varchar(45) DEFAULT NULL,
  `other_title_info` varchar(45) DEFAULT NULL,
  `conference_name` varchar(45) DEFAULT NULL,
  `joint_author_name` varchar(45) DEFAULT NULL,
  `other_info` varchar(45) DEFAULT NULL,
  `bearing_method` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `producer` varchar(45) DEFAULT NULL,
  `public_date` varchar(45) DEFAULT NULL,
  `award` varchar(45) DEFAULT NULL,
  `notes` varchar(45) DEFAULT NULL,
  `search_method` varchar(45) DEFAULT NULL,
  `key_word` varchar(45) DEFAULT NULL,
  `sum` varchar(45) DEFAULT NULL,
  `colors` varchar(45) DEFAULT NULL,
  `audience` varchar(45) DEFAULT NULL,
  `resource` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `inclusion` varchar(45) DEFAULT NULL,
  `included` varchar(45) DEFAULT NULL,
  `copyright_holder` varchar(45) DEFAULT NULL,
  `copyright_notice` varchar(45) DEFAULT NULL,
  `authorize_person` varchar(45) DEFAULT NULL,
  `authorize_form` varchar(45) DEFAULT NULL,
  `authorize_date` varchar(45) DEFAULT NULL,
  `authorize_due` varchar(45) DEFAULT NULL,
  `authorize_area` varchar(45) DEFAULT NULL,
  `authorize_file` varchar(45) DEFAULT NULL,
  `authorize_info` varchar(45) DEFAULT NULL,
  `time_length` varchar(45) DEFAULT NULL,
  `space_length` varchar(45) DEFAULT NULL,
  `source_carrier` varchar(45) DEFAULT NULL,
  `collect_person` varchar(45) DEFAULT NULL,
  `process_unit` varchar(45) DEFAULT NULL,
  `serve_form` varchar(45) DEFAULT NULL,
  `serve_column` varchar(45) DEFAULT NULL,
  `serve_time` varchar(45) DEFAULT NULL,
  `serve_addr` varchar(45) DEFAULT NULL,
  `serve_obj` varchar(45) DEFAULT NULL,
  `acce_time` varchar(45) DEFAULT NULL,
  `acce_form` varchar(45) DEFAULT NULL,
  `acce_person` varchar(45) DEFAULT NULL,
  `acce_opi` varchar(45) DEFAULT NULL,
  `acce_repo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pictures`
--

LOCK TABLES `pictures` WRITE;
/*!40000 ALTER TABLE `pictures` DISABLE KEYS */;
INSERT INTO `pictures` VALUES (1,'飞扬歌舞赞新疆','resource/Pictures/1.jpg','迪丽娜尔','新疆艺术剧院歌舞团','新疆','2020-6-10','2021-12-5','2020-6-10','128kb','831*541',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'我们新疆好地方','resource/Pictures/2.jpg',NULL,'新疆艺术剧院歌舞团','新疆','2011-04-19','2021-12-5','2011-04-19','116kb','818*546',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'心应弦而手应鼓','resource/Pictures/3.jpg',NULL,'新疆艺术剧院歌舞团','新疆','2014','2021-12-5','2014','118kb','822*548',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'新疆歌舞表演吸睛','resource/Pictures/4.jpg',NULL,'新疆艺术剧院歌舞团','新疆','2016-3-14','2021-12-5','2016-3-14','130kb','733*494',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'舞出边塞西域风','resource/Pictures/5.jpg',NULL,NULL,'新疆','2016-3-14','2021-12-5','2016-3-14','158kb','828*621',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,'阳光下的舞步','resource/Pictures/6.jpg','黄雨欣，彭仙仙等','新疆艺术剧院歌舞团','新疆','2017-7-21','2021-12-5','2017-7-21','134kb','900*574',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `pictures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `records` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `URL` varchar(45) DEFAULT NULL,
  `pro_loca` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `record_date` varchar(45) DEFAULT NULL,
  `create_date` varchar(45) NOT NULL,
  `release_date` varchar(45) DEFAULT NULL,
  `singing_form` varchar(45) DEFAULT NULL,
  `sound_track` varchar(45) DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  `length` varchar(45) DEFAULT NULL,
  `bit_rate` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `mode` varchar(45) DEFAULT NULL,
  `parallel_title` varchar(45) DEFAULT NULL,
  `alternate_title` varchar(45) DEFAULT NULL,
  `other_title_info` varchar(45) DEFAULT NULL,
  `series_title` varchar(45) DEFAULT NULL,
  `parallel_series_title` varchar(45) DEFAULT NULL,
  `total_episodes` varchar(45) DEFAULT NULL,
  `episode` varchar(45) DEFAULT NULL,
  `individual_name` varchar(45) DEFAULT NULL,
  `group_name` varchar(45) DEFAULT NULL,
  `conference_name` varchar(45) DEFAULT NULL,
  `joint_author_name` varchar(45) DEFAULT NULL,
  `other_info` varchar(45) DEFAULT NULL,
  `bearing_method` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `producer` varchar(45) DEFAULT NULL,
  `public_date` varchar(45) DEFAULT NULL,
  `award` varchar(45) DEFAULT NULL,
  `singing_style` varchar(45) DEFAULT NULL,
  `parts` varchar(45) DEFAULT NULL,
  `perform_form` varchar(45) DEFAULT NULL,
  `notes` varchar(45) DEFAULT NULL,
  `search_method` varchar(45) DEFAULT NULL,
  `key_word` varchar(45) DEFAULT NULL,
  `perf_type` varchar(45) DEFAULT NULL,
  `perf_form` varchar(45) DEFAULT NULL,
  `sum` varchar(45) DEFAULT NULL,
  `mesh_point` varchar(45) DEFAULT NULL,
  `audio_sampling_frequency` varchar(45) DEFAULT NULL,
  `depth` varchar(45) DEFAULT NULL,
  `language_id` varchar(45) DEFAULT NULL,
  `language_type` varchar(45) DEFAULT NULL,
  `audience` varchar(45) DEFAULT NULL,
  `resource` varchar(45) DEFAULT NULL,
  `ori_form` varchar(45) DEFAULT NULL,
  `other_form` varchar(45) DEFAULT NULL,
  `inclusion` varchar(45) DEFAULT NULL,
  `included` varchar(45) DEFAULT NULL,
  `referring` varchar(45) DEFAULT NULL,
  `reference` varchar(45) DEFAULT NULL,
  `copyright_holder` varchar(45) DEFAULT NULL,
  `copyright_notice` varchar(45) DEFAULT NULL,
  `authorize_person` varchar(45) DEFAULT NULL,
  `authorize_form` varchar(45) DEFAULT NULL,
  `authorize_date` varchar(45) DEFAULT NULL,
  `authorize_due` varchar(45) DEFAULT NULL,
  `authorize_area` varchar(45) DEFAULT NULL,
  `authorize_file` varchar(45) DEFAULT NULL,
  `authorize_info` varchar(45) DEFAULT NULL,
  `time_length` varchar(45) DEFAULT NULL,
  `space_length` varchar(45) DEFAULT NULL,
  `source_carrier` varchar(45) DEFAULT NULL,
  `collect_person` varchar(45) DEFAULT NULL,
  `process_unit` varchar(45) DEFAULT NULL,
  `serve_form` varchar(45) DEFAULT NULL,
  `serve_column` varchar(45) DEFAULT NULL,
  `serve_time` varchar(45) DEFAULT NULL,
  `serve_addr` varchar(45) DEFAULT NULL,
  `serve_obj` varchar(45) DEFAULT NULL,
  `acce_time` varchar(45) DEFAULT NULL,
  `acce_form` varchar(45) DEFAULT NULL,
  `acce_person` varchar(45) DEFAULT NULL,
  `acce_opi` varchar(45) DEFAULT NULL,
  `acce_repo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES (1,'伴奏1','resource/musics/Track01.mp3','新疆','中国原创音乐基地','2011-05-11 ','2021-12-5','2011-05-11 ','伴奏','多声道','594kb','0:37','128kbps','mp3','Exact Audio Copy   (暴发模式)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'伴奏2','resource/musics/Track04.mp3','新疆','中国原创音乐基地','2011-05-11 ','2021-12-5','2011-05-11 ','伴奏','多声道','227kb','0:14','128kbps','mp3','Exact Audio Copy   (暴发模式)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'伴奏3','resource/musics/Track05.mp3','新疆','中国原创音乐基地','2011-05-11 ','2021-12-5','2011-05-11 ','伴奏','多声道','233kb','0:14','128kbps','mp3','Exact Audio Copy   (暴发模式)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'伴奏4','resource/musics/Track07.mp3','新疆','中国原创音乐基地','2011-05-11 ','2021-12-5','2011-05-11 ','伴奏','多声道','228kb','0:14','128kbps','mp3','Exact Audio Copy   (暴发模式)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `name` char(20) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'q','test','pbkdf2:sha256:150000$HIHCyXFN$c0e0afb1e760bb86f0dee300099555e3601fa7757ce454e427ee8c84b45c0a16');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `URL` varchar(45) DEFAULT NULL,
  `parallel_title` varchar(45) DEFAULT NULL,
  `alternate_title` varchar(45) DEFAULT NULL,
  `other_title_info` varchar(45) DEFAULT NULL,
  `series_title` varchar(45) DEFAULT NULL,
  `parallel_series_title` varchar(45) DEFAULT NULL,
  `individual_name` varchar(45) DEFAULT NULL,
  `group_name` varchar(45) DEFAULT NULL,
  `conference_name` varchar(45) DEFAULT NULL,
  `joint_author_name` varchar(45) DEFAULT NULL,
  `other_info` varchar(45) DEFAULT NULL,
  `bearing_method` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `public_date` varchar(45) DEFAULT NULL,
  `addi_block_type` varchar(45) DEFAULT NULL,
  `addi_block_desc` varchar(45) DEFAULT NULL,
  `sound_id` varchar(45) DEFAULT NULL,
  `sound_content` varchar(45) DEFAULT NULL,
  `notes` varchar(45) DEFAULT NULL,
  `search_method` varchar(45) DEFAULT NULL,
  `key_word` varchar(45) DEFAULT NULL,
  `sum` varchar(45) DEFAULT NULL,
  `system` varchar(45) DEFAULT NULL,
  `sound_chara` varchar(45) DEFAULT NULL,
  `colors` varchar(45) DEFAULT NULL,
  `resolution` varchar(45) DEFAULT NULL,
  `sound_qua` varchar(45) DEFAULT NULL,
  `frame_qua` varchar(45) DEFAULT NULL,
  `mode` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `depth` varchar(45) DEFAULT NULL,
  `video_sampling_frequency` varchar(45) DEFAULT NULL,
  `language_id` varchar(45) DEFAULT NULL,
  `language_type` varchar(45) DEFAULT NULL,
  `subtitle_id` varchar(45) DEFAULT NULL,
  `subtitle_type` varchar(45) DEFAULT NULL,
  `audience` varchar(45) DEFAULT NULL,
  `ori_form` varchar(45) DEFAULT NULL,
  `other_form` varchar(45) DEFAULT NULL,
  `inclusion` varchar(45) DEFAULT NULL,
  `included` varchar(45) DEFAULT NULL,
  `refering` varchar(45) DEFAULT NULL,
  `reference` varchar(45) DEFAULT NULL,
  `copyright_holder` varchar(45) DEFAULT NULL,
  `copyright_notice` varchar(45) DEFAULT NULL,
  `authorize_person` varchar(45) DEFAULT NULL,
  `authorize_form` varchar(45) DEFAULT NULL,
  `authorize_date` varchar(45) DEFAULT NULL,
  `authorize_due` varchar(45) DEFAULT NULL,
  `authorize_area` varchar(45) DEFAULT NULL,
  `authorize_file` varchar(45) DEFAULT NULL,
  `authorize_info` varchar(45) DEFAULT NULL,
  `time_length` varchar(45) DEFAULT NULL,
  `space_length` varchar(45) DEFAULT NULL,
  `source_carrier` varchar(45) DEFAULT NULL,
  `collect_area` varchar(45) DEFAULT NULL,
  `collect_unit` varchar(45) DEFAULT NULL,
  `call_number` varchar(45) DEFAULT NULL,
  `collect_person` varchar(45) DEFAULT NULL,
  `process_unit` varchar(45) DEFAULT NULL,
  `serve_form` varchar(45) DEFAULT NULL,
  `serve_column` varchar(45) DEFAULT NULL,
  `serve_time` varchar(45) DEFAULT NULL,
  `serve_addr` varchar(45) DEFAULT NULL,
  `serve_obj` varchar(45) DEFAULT NULL,
  `acce_time` varchar(45) DEFAULT NULL,
  `acce_form` varchar(45) DEFAULT NULL,
  `acce_person` varchar(45) DEFAULT NULL,
  `acce_opi` varchar(45) DEFAULT NULL,
  `acce_repo` varchar(45) DEFAULT NULL,
  `series` varchar(45) NOT NULL,
  `episode` varchar(45) DEFAULT NULL,
  `total_episodes` varchar(45) DEFAULT NULL,
  `producer` varchar(45) DEFAULT NULL,
  `pro_loca` varchar(45) DEFAULT NULL,
  `resource` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `video_date` varchar(45) DEFAULT NULL,
  `create_date` varchar(45) NOT NULL,
  `release_date` varchar(45) DEFAULT NULL,
  `award` varchar(45) DEFAULT NULL,
  `performance_form` varchar(45) DEFAULT NULL,
  `program_type` varchar(45) DEFAULT NULL,
  `subtitle` varchar(45) DEFAULT NULL,
  `length` varchar(45) DEFAULT NULL,
  `aspect_ratio` varchar(45) DEFAULT NULL,
  `bit_rate` varchar(45) DEFAULT NULL,
  `sound_track` varchar(45) DEFAULT NULL,
  `data_rate` varchar(45) DEFAULT NULL,
  `total_bitrate` varchar(45) DEFAULT NULL,
  `audio_sampling_frequency` varchar(45) DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos`
--

LOCK TABLES `videos` WRITE;
/*!40000 ALTER TABLE `videos` DISABLE KEYS */;
INSERT INTO `videos` VALUES (1,'阿拉木汗','resource/dramas/8.舞蹈-阿拉木汗.mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'剧目','1','5','东映文化','新疆',NULL,NULL,'2010-5-6','2010-6-1',NULL,NULL,'舞蹈表演',NULL,'中文','8:59','640*512','64kbps','2','975kbps','1039kpbs','48khz','67.1mb'),(2,'天山姑娘','resource/dramas/9.舞蹈-天山姑娘.mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'剧目','2','5','东映文化','新疆',NULL,NULL,'2010-5-6','2010-6-1',NULL,NULL,'舞蹈表演',NULL,'中文','8:04','720*576','126kbps','2','1837kbps','1964kbps','48khz','113mb'),(3,'顶碗舞','resource/dramas/维族女班09-1剧目欣赏 顶碗舞.mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'剧目','3','5',NULL,'新疆','75pop.com','起舞网','2010-5-6','2010-6-1',NULL,NULL,'舞蹈表演',NULL,'中文','6:12','640*480','96kbps','2','1273kbps','1369kbps','48khz','61mb'),(4,'哈密姑娘1','resource/dramas/维族女班09-2剧目欣赏 哈密姑娘1.mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'剧目','4','5',NULL,'新疆','75pop.com','起舞网','2010-5-6','2010-6-1',NULL,NULL,'舞蹈表演',NULL,'中文','5:15','640*480','96kbps','2','1281kbps','1377kbps','48khz','51.9mb'),(5,'哈密姑娘2','resource/dramas/维族女班09-3剧目欣赏 哈密姑娘2.mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'剧目','5','5',NULL,'新疆','75pop.com','起舞网','2010-5-6','2010-6-1',NULL,'2017中国舞蹈“荷花奖”民族民间舞','舞蹈表演',NULL,'中文','7:15','640*480','96kbps','2','1287kbps','1384kbps','48khz','72mb'),(6,'第一节','resource/instructions/Movie_02_(Part_3_1).mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'教程','1','5','新疆艺术学院','新疆',NULL,NULL,'2017-9-20','2017-9-20',NULL,NULL,'','分解动作','中文','7:40','720*576','155kbps','2','2076kbps','2232kbps','48khz','122mb'),(7,'第二节','resource/instructions/Movie_03_(Part_4_1).mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'教程','2','5','新疆艺术学院','新疆',NULL,NULL,'2017-9-20','2017-9-20',NULL,NULL,'','分解动作','中文','5:09','720*576','153kbps','2','2074kbps','2227kbps','48khz','82.1mb'),(8,'第三节','resource/instructions/Movie_04_(Part_5_1).mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'教程','3','5','新疆艺术学院','新疆',NULL,NULL,'2017-9-20','2017-9-20',NULL,NULL,'','分解动作','中文','6:48','720*576','157kbps','2','2074kbps','2232kbps','48khz','108mb'),(9,'第四节','resource/instructions/Movie_05_(Part_6_1).mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'教程','4','5','新疆艺术学院','新疆',NULL,NULL,'2017-9-20','2017-9-20',NULL,NULL,'','分解动作','中文','2:25','720*576','154kbps','2','2068kbps','2222kbps','48khz','38.7mb'),(10,'第五节','resource/instructions/Movie_06_(Part_7_1).mp4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'教程','5','5','新疆艺术学院','新疆',NULL,NULL,'2017-9-20','2017-9-20',NULL,NULL,'','分解动作','中文','3:15','720*576','156kbps','2','2077kbps','2233kbps','48khz','51.9mb');
/*!40000 ALTER TABLE `videos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-14 22:41:22
