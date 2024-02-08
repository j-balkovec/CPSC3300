CREATE DATABASE IF NOT EXISTS Project1;

USE Project1;

-- Create User table
CREATE TABLE IF NOT EXISTS `User` (
    `UserID` INT PRIMARY KEY NOT NULL,
    `Username` VARCHAR(255) UNIQUE,
    `Password` VARCHAR(255),
    `Email` VARCHAR(255),
    `PhoneNumber` VARCHAR(11),
    `DateOfBirth` DATE
);

-- Create Profile table
CREATE TABLE IF NOT EXISTS `Profile` (
    `ProfileID` INT PRIMARY KEY NOT NULL,
    `UserID` INT NOT NULL,
    `Bio` VARCHAR(255),
    `Education` VARCHAR(255),
    `Job` VARCHAR(255),
    `Interests` VARCHAR(255),
    `PrivacySettings` ENUM('Public', 'Private', 'Brand', 'Athlete'),
    `ProfilePicture` BLOB,
    `CoverPhoto` BLOB,
    `JoinDate` DATE,
    `LastActive` DATETIME,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`)
);

-- Create Group table
CREATE TABLE IF NOT EXISTS `Group` (
    `GroupID` INT PRIMARY KEY NOT NULL,
    `UserID` INT NOT NULL,
    `GroupName` VARCHAR(255),
    `Description` VARCHAR(255),
    `MemberCount` BIGINT,
    `CreationDate` DATE,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`)
);

-- Create GroupUser table
CREATE TABLE IF NOT EXISTS `GroupUser` (
    `GroupUserID` INT PRIMARY KEY NOT NULL,
    `UserID` INT NOT NULL,
    `GroupID` INT NOT NULL,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`),
    FOREIGN KEY (`GroupID`) REFERENCES `Group` (`GroupID`)
);

-- Create Message table
CREATE TABLE IF NOT EXISTS `Message` (
    `MessageID` INT PRIMARY KEY NOT NULL,
    `UserIDSender` INT NOT NULL,
    `UserIDReceiver` INT NOT NULL,
    `Content` VARCHAR(255),
    `Timestamp` DATETIME,
    `Status` ENUM('sent', 'delivered', 'read'),
    FOREIGN KEY (`UserIDSender`) REFERENCES `User` (`UserID`),
    FOREIGN KEY (`UserIDReceiver`) REFERENCES `User` (`UserID`)
);

-- Create Goal table
CREATE TABLE IF NOT EXISTS `Goal` (
    `GoalID` INT PRIMARY KEY NOT NULL,
    `UserID` INT NOT NULL,
    `ProfileID` INT NOT NULL,
    `Content` VARCHAR(255),
    `DatePosted` DATE,
    `Frequency` ENUM('daily', 'weekly', 'monthly'),
    `Score` BIGINT,
    `PrivacySettings` ENUM('Public', 'Private', 'Brand', 'Athlete'),
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`),
    FOREIGN KEY (`ProfileID`) REFERENCES `Profile` (`ProfileID`)
);

-- Create Plant table
CREATE TABLE IF NOT EXISTS `Plant` (
    `PlantID` INT PRIMARY KEY NOT NULL,
    `GoalID` INT NOT NULL,
    `ProfileID` INT NOT NULL,
    `StreakAlive` BOOLEAN,
    `StreakDuration` BIGINT,
    `DaysStreakDead` BIGINT,
    `DaysStreakKeptAlive` BIGINT,
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`),
    FOREIGN KEY (`ProfileID`) REFERENCES `Profile` (`ProfileID`)
);

-- Create Comment table
CREATE TABLE IF NOT EXISTS `Comment` (
    `CommentID` INT PRIMARY KEY NOT NULL,
    `UserID` INT NOT NULL,
    `GoalID` INT NOT NULL,
    `Content` VARCHAR(255),
    `Timestamp` TIMESTAMP,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`),
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`)
);

-- Create Like table
CREATE TABLE IF NOT EXISTS `Like` (
    `LikeID` INT PRIMARY KEY NOT NULL,
    `GoalID` INT NOT NULL,
    `UserID` INT NOT NULL,
    `Timestamp` TIMESTAMP,
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`),
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`)
);

-- Create Media table
CREATE TABLE IF NOT EXISTS `Media` (
    `MediaID` INT PRIMARY KEY NOT NULL,
    `GoalID` INT NOT NULL,
    `Content` BLOB,
    `DateUploaded` DATE,
    `PrivacySettings` ENUM('Public', 'Private', 'Brand', 'Athlete'),
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`)
);

SELECT * FROM `USER`
