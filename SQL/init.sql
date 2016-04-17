CREATE DATABASE `factorio`;
USE `factorio`;

CREATE TABLE `user` (
	`user_id` INT NOT NULL AUTO_INCREMENT,
	`peer_id` INT NOT NULL,
	`username` VARCHAR(50) NOT NULL,
	`ip_address` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`user_id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB;

CREATE TABLE `messages` (
	`message_id` INT NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(50) NOT NULL,
	`message` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`message_id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB;