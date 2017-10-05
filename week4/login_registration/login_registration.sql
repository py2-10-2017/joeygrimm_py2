-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema login_registration
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema login_registration
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_registration` DEFAULT CHARACTER SET utf8 ;
USE `login_registration` ;

-- -----------------------------------------------------
-- Table `login_registration`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_registration`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(60) NULL,
  `last_name` VARCHAR(60) NULL,
  `email` VARCHAR(75) NULL,
  `pw_hash` VARCHAR(225) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;