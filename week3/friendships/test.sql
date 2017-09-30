-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friendship
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friendship
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendship` DEFAULT CHARACTER SET utf8 ;
USE `friendship` ;

-- -----------------------------------------------------
-- Table `friendship`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendship`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

LOCK TABLES `users` WRITE;
INSERT INTO `users` (id, first_name, last_name)
VALUES (1,'Joe','Larkin'),(2,'Dave','Wheeler'),(3,'Ryan','Smith'),(4,'Coleman','Shepard'),(5,'Nacy','Fields');
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `friendship`.`friendships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendship`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friendships_users_idx` (`user_id` ASC),
  INDEX `fk_friendships_users1_idx` (`friend_id` ASC),
  CONSTRAINT `fk_friendships_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendship`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_friendships_users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `friendship`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

LOCK TABLES `friendships` WRITE;
INSERT INTO `friendships` ( id, user_id, friend_id)
VALUES (1,1,2),(2,1,3),(3,1,4),(4,2,1),(5,2,3),(6,3,1),(7,3,2),(8,3,4),(9,4,1),(10,4,3);
UNLOCK TABLES;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
