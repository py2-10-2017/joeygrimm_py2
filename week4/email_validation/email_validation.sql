-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema email_validation_ERD
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema email_validation_ERD
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `email_validation_ERD` DEFAULT CHARACTER SET utf8 ;
USE `email_validation_ERD` ;

-- -----------------------------------------------------
-- Table `email_validation_ERD`.`Emails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `email_validation_ERD`.`Emails` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(70) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
