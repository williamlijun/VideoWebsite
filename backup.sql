/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50735
 Source Host           : localhost:3306
 Source Schema         : video_website

 Target Server Type    : MySQL
 Target Server Version : 50735
 File Encoding         : 65001

 Date: 08/05/2024 21:51:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for channel
-- ----------------------------
DROP TABLE IF EXISTS `channel`;
CREATE TABLE `channel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `subscribe_number` int(10) UNSIGNED ZEROFILL NULL DEFAULT NULL,
  `channel_image_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `channel_description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CreatorID` tinyint(4) NULL DEFAULT NULL,
  `CreationTime` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `UpdateTime` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ViewCount` int(11) NULL DEFAULT NULL,
  `VideoCount` int(11) NULL DEFAULT NULL,
  `ChannelStatus` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `channel_describe` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of channel
-- ----------------------------
INSERT INTO `channel` VALUES (1, '阿斯顿撒', 0000000020, 'img/s2.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (2, 'test2', 0000000010, 'img/channel_img1.png', NULL, 2, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (3, 'test2', 0000000005, 'img/channel_img2.png', NULL, 3, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (4, 'test3', 0000000006, 'img/channel_img3.png', NULL, 4, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (6, 'test5', 0000000003, 'img/channel_img5.png', NULL, 5, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (7, 'test6', 0000000000, 'img/channel_img6.png', NULL, 6, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (8, 'test7', 0000000000, 'img/channel_img7.png', NULL, 7, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (9, 'test8', 0000000000, 'img/channel_img8.png', NULL, 8, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (10, 'test9', 0000000000, 'img/channel_img9.png', NULL, 9, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (11, 'test10', 0000000000, 'img/channel_img10.png', NULL, 10, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (12, 'test11', 0000000000, 'img/channel_img11.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (13, 'test12', 0000000000, 'img/channel_img12.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (14, 'test13', 0000000000, 'img/channel_img13.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (15, 'test14', 0000000000, 'img/channel_img14.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (16, 'test15', 0000000000, 'img/channel_img15.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `channel` VALUES (17, 'test16', 0000000050, 'img/channel_img16.png', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `comments` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES (4, 1, 1, '阿斯顿撒旦的撒旦');
INSERT INTO `comment` VALUES (5, 1, 1, '哈哈哈哈哈');
INSERT INTO `comment` VALUES (6, 1, 7, 'asadasdasdsad');
INSERT INTO `comment` VALUES (7, 1, 7, '你说的对');
INSERT INTO `comment` VALUES (8, 1, 7, '你好啊');
INSERT INTO `comment` VALUES (9, 1, 7, '你好');
INSERT INTO `comment` VALUES (10, 1, 7, '你好啊');
INSERT INTO `comment` VALUES (11, 1, 7, '这个非常的好看');
INSERT INTO `comment` VALUES (12, 1, 1, 'sdfsdfsd');
INSERT INTO `comment` VALUES (13, 3, 2, '你好');
INSERT INTO `comment` VALUES (14, 1, 2, '你哈');
INSERT INTO `comment` VALUES (15, 2, 2, '你好啊');
INSERT INTO `comment` VALUES (16, 1, NULL, '啊实打实');
INSERT INTO `comment` VALUES (17, 7, 1, '好看');
INSERT INTO `comment` VALUES (18, 9, 1, 'nihao1');
INSERT INTO `comment` VALUES (19, 8, 1, 'bsgsdgsd');
INSERT INTO `comment` VALUES (20, 33, 1, '你好');

-- ----------------------------
-- Table structure for favorite_video
-- ----------------------------
DROP TABLE IF EXISTS `favorite_video`;
CREATE TABLE `favorite_video`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `video_id` int(11) NULL DEFAULT NULL,
  `is_favorite` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of favorite_video
-- ----------------------------
INSERT INTO `favorite_video` VALUES (8, 1, 4, '1');
INSERT INTO `favorite_video` VALUES (9, 1, 10, '1');
INSERT INTO `favorite_video` VALUES (10, 1, 8, '1');
INSERT INTO `favorite_video` VALUES (11, 1, 7, '1');
INSERT INTO `favorite_video` VALUES (15, 1, 1, '1');

-- ----------------------------
-- Table structure for like_table
-- ----------------------------
DROP TABLE IF EXISTS `like_table`;
CREATE TABLE `like_table`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `is_like` tinyint(2) NULL DEFAULT NULL COMMENT '为0表示不喜欢，为1表示喜欢',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of like_table
-- ----------------------------
INSERT INTO `like_table` VALUES (2, 2, 1, 1);
INSERT INTO `like_table` VALUES (20, 4, 1, 1);
INSERT INTO `like_table` VALUES (23, 10, 1, 1);
INSERT INTO `like_table` VALUES (24, 8, 1, 1);
INSERT INTO `like_table` VALUES (25, 7, 1, 1);
INSERT INTO `like_table` VALUES (26, 3, 1, 0);
INSERT INTO `like_table` VALUES (30, 1, 1, 1);
INSERT INTO `like_table` VALUES (31, 14, 1, 1);

-- ----------------------------
-- Table structure for search_img
-- ----------------------------
DROP TABLE IF EXISTS `search_img`;
CREATE TABLE `search_img`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `img_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of search_img
-- ----------------------------

-- ----------------------------
-- Table structure for subscription
-- ----------------------------
DROP TABLE IF EXISTS `subscription`;
CREATE TABLE `subscription`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `channel_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `channel_id` int(11) NOT NULL,
  `subscription_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 82 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of subscription
-- ----------------------------
INSERT INTO `subscription` VALUES (5, 'lee', 1, NULL, 5, NULL);
INSERT INTO `subscription` VALUES (75, NULL, 2, NULL, 3, NULL);
INSERT INTO `subscription` VALUES (76, 'lee', 1, NULL, 9, NULL);
INSERT INTO `subscription` VALUES (77, 'lee', 1, NULL, 12, NULL);
INSERT INTO `subscription` VALUES (78, 'lee', 1, NULL, 13, NULL);
INSERT INTO `subscription` VALUES (81, 'lee', 1, NULL, 16, NULL);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone_number` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `RegistrationTime` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `LastLoginTime` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `UserType` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `UserStatus` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Gender` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `DateOfBirth` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Bio` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'lee', '20101130116', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s1.png');
INSERT INTO `user` VALUES (2, NULL, '15686547', '123456', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s2.png');
INSERT INTO `user` VALUES (3, NULL, '1568654788', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s3.png');
INSERT INTO `user` VALUES (4, NULL, '1865974', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s4.png');
INSERT INTO `user` VALUES (5, NULL, '1458697', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s5.png');
INSERT INTO `user` VALUES (6, NULL, '12568', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s6.png');
INSERT INTO `user` VALUES (7, NULL, '123456', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/s7.png');
INSERT INTO `user` VALUES (8, NULL, '555555', '123', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `user` VALUES (9, 'Zhao Zitao', '52-876-3301', 'SUUU5OM34m', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `user` VALUES (10, 'visitor', '80-9097-9967', 'XbyyErsioS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'img/logo.png');

-- ----------------------------
-- Table structure for user_tag
-- ----------------------------
DROP TABLE IF EXISTS `user_tag`;
CREATE TABLE `user_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 51 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_tag
-- ----------------------------
INSERT INTO `user_tag` VALUES (1, 1, '动漫');
INSERT INTO `user_tag` VALUES (2, 1, '战争');
INSERT INTO `user_tag` VALUES (3, 1, '广告');
INSERT INTO `user_tag` VALUES (4, 1, '搞笑');
INSERT INTO `user_tag` VALUES (5, 1, '广告');
INSERT INTO `user_tag` VALUES (6, 1, '快递');
INSERT INTO `user_tag` VALUES (7, 1, '真人');
INSERT INTO `user_tag` VALUES (8, 1, '广告');
INSERT INTO `user_tag` VALUES (9, 1, '化妆品');
INSERT INTO `user_tag` VALUES (10, 1, '真人');
INSERT INTO `user_tag` VALUES (11, 1, '粉色');
INSERT INTO `user_tag` VALUES (12, 1, '广告');
INSERT INTO `user_tag` VALUES (13, 1, '食品');
INSERT INTO `user_tag` VALUES (14, 1, '汉堡');
INSERT INTO `user_tag` VALUES (15, 1, '动漫');
INSERT INTO `user_tag` VALUES (16, 1, '战争');
INSERT INTO `user_tag` VALUES (17, 1, '广告');
INSERT INTO `user_tag` VALUES (18, 1, '搞笑');
INSERT INTO `user_tag` VALUES (19, 1, '广告');
INSERT INTO `user_tag` VALUES (20, 1, '快递');
INSERT INTO `user_tag` VALUES (21, 1, '真人');
INSERT INTO `user_tag` VALUES (22, 1, '广告');
INSERT INTO `user_tag` VALUES (23, 1, '化妆品');
INSERT INTO `user_tag` VALUES (24, 1, '真人');
INSERT INTO `user_tag` VALUES (25, 1, '粉色');
INSERT INTO `user_tag` VALUES (26, 1, '广告');
INSERT INTO `user_tag` VALUES (27, 1, '食品');
INSERT INTO `user_tag` VALUES (28, 1, '汉堡');
INSERT INTO `user_tag` VALUES (29, 2, '动漫');
INSERT INTO `user_tag` VALUES (30, 2, '战争');
INSERT INTO `user_tag` VALUES (31, 2, '广告');
INSERT INTO `user_tag` VALUES (32, 2, '搞笑');
INSERT INTO `user_tag` VALUES (33, 2, '广告');
INSERT INTO `user_tag` VALUES (34, 2, '快递');
INSERT INTO `user_tag` VALUES (35, 2, '真人');
INSERT INTO `user_tag` VALUES (36, 2, '广告');
INSERT INTO `user_tag` VALUES (37, 2, '化妆品');
INSERT INTO `user_tag` VALUES (38, 2, '真人');
INSERT INTO `user_tag` VALUES (39, 2, '粉色');
INSERT INTO `user_tag` VALUES (40, 2, '广告');
INSERT INTO `user_tag` VALUES (41, 2, '食品');
INSERT INTO `user_tag` VALUES (42, 2, '汉堡');
INSERT INTO `user_tag` VALUES (43, 3, '动漫');
INSERT INTO `user_tag` VALUES (44, 3, '战争');
INSERT INTO `user_tag` VALUES (45, 3, '广告');
INSERT INTO `user_tag` VALUES (46, 3, '搞笑');
INSERT INTO `user_tag` VALUES (47, 3, '广告');
INSERT INTO `user_tag` VALUES (48, 3, '快递');
INSERT INTO `user_tag` VALUES (49, 3, '真人');
INSERT INTO `user_tag` VALUES (50, 4, '动漫');

-- ----------------------------
-- Table structure for video
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_classification` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_blong_to` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_img_url` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `video_title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `upload_date` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `views` int(11) NULL DEFAULT NULL,
  `likes` int(11) NULL DEFAULT NULL,
  `Privacy` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `channel_id` int(11) NULL DEFAULT NULL,
  `dislike` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `video_blong_to`(`video_blong_to`) USING BTREE,
  CONSTRAINT `video_ibfk_1` FOREIGN KEY (`video_blong_to`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 55 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of video
-- ----------------------------
INSERT INTO `video` VALUES (1, 'test1', NULL, NULL, 'lee', 'video/1.mp4', 'video/1.jpg', NULL, '瑞克与莫蒂', NULL, NULL, 1, NULL, 1, 0);
INSERT INTO `video` VALUES (2, 'test2', NULL, NULL, 'lee', 'video/2.mp4', 'video/2.jpg', NULL, '电影片段', NULL, NULL, 1, NULL, 1, 0);
INSERT INTO `video` VALUES (3, 'test3', NULL, NULL, 'lee', 'video/3.mp4', 'video/3.jpg', NULL, '动漫', NULL, NULL, 0, NULL, 1, 1);
INSERT INTO `video` VALUES (4, 'test4', NULL, NULL, 'lee', 'video/4.mp4', 'video/4.jpg', NULL, '心灵捕手', NULL, NULL, 1, NULL, 1, 0);
INSERT INTO `video` VALUES (5, 'test5', NULL, NULL, NULL, 'video/5.mp4', 'video/5.jpg', NULL, '加勒比海盗', NULL, NULL, 0, NULL, 2, 0);
INSERT INTO `video` VALUES (6, 'test6', NULL, NULL, NULL, 'video/6.mp4', 'video/6.jpg', NULL, NULL, NULL, NULL, 0, NULL, 3, 0);
INSERT INTO `video` VALUES (7, 'test7', NULL, NULL, NULL, 'video/7.mp4', 'video/7.jpg', NULL, NULL, NULL, NULL, 1, NULL, 2, 0);
INSERT INTO `video` VALUES (8, 'test8', NULL, NULL, NULL, 'video/8.mp4', 'video/8.jpg', NULL, NULL, NULL, NULL, 1, NULL, 2, 0);
INSERT INTO `video` VALUES (9, 'test9', NULL, NULL, NULL, 'video/9.mp4', 'video/9.jpg', NULL, NULL, NULL, NULL, 0, NULL, 3, 0);
INSERT INTO `video` VALUES (10, 'test10', NULL, NULL, NULL, 'video/10.mp4', 'video/10.jpg', NULL, NULL, NULL, NULL, 1, NULL, 3, 0);
INSERT INTO `video` VALUES (11, 'test11', NULL, NULL, NULL, 'video/11.mp4', 'video/11.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL);
INSERT INTO `video` VALUES (12, 'test12', NULL, NULL, NULL, 'video/12.mp4', 'video/12.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL);
INSERT INTO `video` VALUES (13, 'test13', NULL, NULL, NULL, 'video/13.mp4', 'video/13.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL);
INSERT INTO `video` VALUES (14, 'test14', NULL, NULL, NULL, 'video/14.mp4', 'video/14.jpg', NULL, NULL, NULL, NULL, 1, NULL, 5, 0);
INSERT INTO `video` VALUES (15, 'test15', NULL, NULL, NULL, 'video/15.mp4', 'video/15.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL);
INSERT INTO `video` VALUES (16, 'test16', NULL, NULL, NULL, 'video/16.mp4', 'video/16.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL);
INSERT INTO `video` VALUES (17, 'test17', NULL, NULL, NULL, 'video/17.mp4', 'video/17.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL);
INSERT INTO `video` VALUES (18, 'test18', NULL, NULL, NULL, 'video/18.mp4', 'video/18.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL);
INSERT INTO `video` VALUES (19, 'test19', NULL, NULL, NULL, 'video/19.mp4', 'video/19.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL);
INSERT INTO `video` VALUES (20, 'test20', NULL, NULL, NULL, 'video/20.mp4', 'video/20.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL);
INSERT INTO `video` VALUES (21, 'test21', NULL, NULL, NULL, 'video/21.mp4', 'video/21.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL);
INSERT INTO `video` VALUES (22, 'test22', NULL, NULL, NULL, 'video/22.mp4', 'video/22.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL);
INSERT INTO `video` VALUES (23, 'test23', NULL, NULL, NULL, 'video/23.mp4', 'video/23.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL);
INSERT INTO `video` VALUES (24, 'test24', NULL, NULL, NULL, 'video/24.mp4', 'video/24.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL);
INSERT INTO `video` VALUES (25, 'test25', NULL, NULL, 'lee', 'video/25.mp4', 'video/25.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 3, NULL);
INSERT INTO `video` VALUES (26, 'test26', NULL, NULL, NULL, 'video/26.mp4', 'video/26.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL);
INSERT INTO `video` VALUES (27, 'test27', NULL, NULL, NULL, 'video/27.mp4', 'video/27.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL);
INSERT INTO `video` VALUES (28, 'test28', NULL, NULL, NULL, 'video/28.mp4', 'video/28.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL);
INSERT INTO `video` VALUES (29, 'test29', NULL, NULL, NULL, 'video/29.mp4', 'video/29.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL);
INSERT INTO `video` VALUES (30, 'test30', NULL, NULL, NULL, 'video/30.mp4', 'video/30.jpg', NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL);
INSERT INTO `video` VALUES (31, NULL, NULL, NULL, NULL, 'video/31.mp4', 'video/31.jpg', '和哥哥可以给vu一股vu一个vu股份有车有房', 'When \"Asian\" Is a Difficulty Mode', NULL, NULL, NULL, 'public', 9, NULL);
INSERT INTO `video` VALUES (32, NULL, NULL, NULL, NULL, 'video/32.mp4', 'video/32.jpg', '和哥哥可以给vu一股vu一个vu股份有车有房', 'When \"Asian\" Is a Difficulty Mode', NULL, NULL, NULL, 'public', 10, NULL);
INSERT INTO `video` VALUES (33, NULL, NULL, NULL, NULL, 'video/33.mp4', 'video/33.jpg', '和哥哥可以给vu一股vu一个vu股份有车有房', 'When \"Asian\" Is a Difficulty Mode', NULL, NULL, NULL, 'public', 11, NULL);

-- ----------------------------
-- Table structure for video_tag
-- ----------------------------
DROP TABLE IF EXISTS `video_tag`;
CREATE TABLE `video_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` int(11) NULL DEFAULT NULL,
  `tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 83 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of video_tag
-- ----------------------------
INSERT INTO `video_tag` VALUES (15, 1, '动漫');
INSERT INTO `video_tag` VALUES (16, 2, '电影片段');
INSERT INTO `video_tag` VALUES (17, 3, '动漫');
INSERT INTO `video_tag` VALUES (18, 4, '动漫');
INSERT INTO `video_tag` VALUES (19, 5, '海盗');
INSERT INTO `video_tag` VALUES (20, 6, '励志');
INSERT INTO `video_tag` VALUES (21, 7, '唯美');
INSERT INTO `video_tag` VALUES (22, 8, '战争');
INSERT INTO `video_tag` VALUES (23, 9, '战争');
INSERT INTO `video_tag` VALUES (24, 10, '战争');
INSERT INTO `video_tag` VALUES (25, 11, '科幻');
INSERT INTO `video_tag` VALUES (26, 12, '唯美');
INSERT INTO `video_tag` VALUES (27, 13, '动漫');
INSERT INTO `video_tag` VALUES (28, 14, '动漫');
INSERT INTO `video_tag` VALUES (29, 15, '动漫');
INSERT INTO `video_tag` VALUES (30, 16, '动漫');
INSERT INTO `video_tag` VALUES (31, 17, '动漫');
INSERT INTO `video_tag` VALUES (32, 18, '动漫');
INSERT INTO `video_tag` VALUES (33, 19, '搞笑');
INSERT INTO `video_tag` VALUES (34, 20, '搞笑');
INSERT INTO `video_tag` VALUES (35, 21, '动漫');
INSERT INTO `video_tag` VALUES (36, 22, '动漫');
INSERT INTO `video_tag` VALUES (37, 23, '奥特曼');
INSERT INTO `video_tag` VALUES (38, 24, '剪辑');
INSERT INTO `video_tag` VALUES (39, 25, '剪辑');
INSERT INTO `video_tag` VALUES (40, 26, '励志');
INSERT INTO `video_tag` VALUES (41, 27, '励志');
INSERT INTO `video_tag` VALUES (42, 28, '励志');
INSERT INTO `video_tag` VALUES (43, 29, '剪辑');
INSERT INTO `video_tag` VALUES (44, 30, '治愈');
INSERT INTO `video_tag` VALUES (45, 31, '唯美');
INSERT INTO `video_tag` VALUES (46, 32, '剪辑');
INSERT INTO `video_tag` VALUES (47, 33, '电影解说');
INSERT INTO `video_tag` VALUES (48, 2, '剪辑');
INSERT INTO `video_tag` VALUES (49, 2, '悲伤');
INSERT INTO `video_tag` VALUES (50, 3, '唯美');
INSERT INTO `video_tag` VALUES (51, 4, '唯美');
INSERT INTO `video_tag` VALUES (52, 5, '海盗');
INSERT INTO `video_tag` VALUES (53, 6, '剪辑');
INSERT INTO `video_tag` VALUES (54, 7, '剪辑');
INSERT INTO `video_tag` VALUES (56, 9, '感动');
INSERT INTO `video_tag` VALUES (57, 10, '感动');
INSERT INTO `video_tag` VALUES (58, 11, '搞笑');
INSERT INTO `video_tag` VALUES (59, 12, '剪辑');
INSERT INTO `video_tag` VALUES (60, 13, '音乐');
INSERT INTO `video_tag` VALUES (61, 14, '感动');
INSERT INTO `video_tag` VALUES (62, 15, '动作');
INSERT INTO `video_tag` VALUES (63, 16, '动作');
INSERT INTO `video_tag` VALUES (64, 17, '唯美');
INSERT INTO `video_tag` VALUES (65, 18, '动作');
INSERT INTO `video_tag` VALUES (66, 19, '剪辑');
INSERT INTO `video_tag` VALUES (67, 20, '动漫');
INSERT INTO `video_tag` VALUES (68, 21, '动作');
INSERT INTO `video_tag` VALUES (69, 22, '动作');
INSERT INTO `video_tag` VALUES (70, 23, '阴暗');
INSERT INTO `video_tag` VALUES (71, 24, '搞笑');
INSERT INTO `video_tag` VALUES (72, 25, '搞笑');
INSERT INTO `video_tag` VALUES (73, 26, '剪辑');
INSERT INTO `video_tag` VALUES (74, 27, '剪辑');
INSERT INTO `video_tag` VALUES (75, 28, '电影片段');
INSERT INTO `video_tag` VALUES (76, 29, '黑社会');
INSERT INTO `video_tag` VALUES (77, 30, '唯美');
INSERT INTO `video_tag` VALUES (78, 31, '美丽');
INSERT INTO `video_tag` VALUES (79, 32, '电影片段');
INSERT INTO `video_tag` VALUES (80, 33, '科幻');

-- ----------------------------
-- Table structure for view_history
-- ----------------------------
DROP TABLE IF EXISTS `view_history`;
CREATE TABLE `view_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `video_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 113 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of view_history
-- ----------------------------
INSERT INTO `view_history` VALUES (81, 1, 2);
INSERT INTO `view_history` VALUES (82, 1, 4);
INSERT INTO `view_history` VALUES (83, 1, 6);
INSERT INTO `view_history` VALUES (84, 1, 8);
INSERT INTO `view_history` VALUES (85, 1, 18);
INSERT INTO `view_history` VALUES (86, 1, 27);
INSERT INTO `view_history` VALUES (87, 1, 29);
INSERT INTO `view_history` VALUES (88, 1, 14);
INSERT INTO `view_history` VALUES (89, 1, 1);
INSERT INTO `view_history` VALUES (90, 1, 7);
INSERT INTO `view_history` VALUES (91, 1, 3);
INSERT INTO `view_history` VALUES (92, 1, 9);
INSERT INTO `view_history` VALUES (107, 2, 1);
INSERT INTO `view_history` VALUES (108, 2, 7);
INSERT INTO `view_history` VALUES (109, 2, 8);
INSERT INTO `view_history` VALUES (110, 2, 10);
INSERT INTO `view_history` VALUES (111, 1, 24);
INSERT INTO `view_history` VALUES (112, 1, 33);

SET FOREIGN_KEY_CHECKS = 1;
