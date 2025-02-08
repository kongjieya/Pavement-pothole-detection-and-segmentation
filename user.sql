/*
 Navicat Premium Data Transfer

 Source Server         : python
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : yolo

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 15/01/2025 14:12:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `nick_name` varchar(12) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `avatar` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `register_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 46 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (13, '1', '1', '挂科边缘毕业版', '20250115124611_kk.jpg', '2025-01-06 04:18:19.000000');
INSERT INTO `user` VALUES (23, '15578546732', '12345@z', '1', '20250106013416_挂科.jpg', '2025-01-06 04:18:26.000000');
INSERT INTO `user` VALUES (30, '11111', '1', '1', '20250106015930_挂科.jpg', '2025-01-06 04:18:29.000000');
INSERT INTO `user` VALUES (43, '888', '888', '888', '20250106054949_kk.jpg', '2025-01-06 05:49:49.000000');
INSERT INTO `user` VALUES (44, '3', '3', '3', '20250107231455_kk.jpg', '2025-01-07 23:14:55.000000');
INSERT INTO `user` VALUES (45, '15578906543', '12345@z', '123', '20250108031156_kk.jpg', '2025-01-08 03:11:56.000000');

SET FOREIGN_KEY_CHECKS = 1;
