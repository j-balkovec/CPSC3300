CREATE DATABASE IF NOT EXISTS Project1;

USE Project1;

/**
 * @name: User
 * @brief: User table represents registered users of the system.
 */
CREATE TABLE IF NOT EXISTS `User` ( 
    `UserID` INT PRIMARY KEY NOT NULL, 	    -- PK
    `Username` VARCHAR(255) UNIQUE,
    `Password` VARCHAR(255),
    `Email` VARCHAR(255) UNIQUE,
    `PhoneNumber` VARCHAR(11) UNIQUE,
    `DateOfBirth` DATE
);

/**
 * @name: Profile
 * @brief: Profile table represents user profiles.
 */
CREATE TABLE IF NOT EXISTS `Profile` (
    `ProfileID` INT PRIMARY KEY NOT NULL, 	-- PK
    `UserID` INT NOT NULL, 					-- FK
    `Bio` VARCHAR(255),
    `Education` VARCHAR(255),
    `Job` VARCHAR(255),
    `Interests` VARCHAR(255),
    `PrivacySettings` ENUM('Public', 'Private', 'Brand', 'Athlete', 'FriendsOnly'),
    `ProfilePicture` BLOB,
    `CoverPhoto` BLOB,
    `JoinDate` DATE,
    `LastActive` DATETIME,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE
);

/**
 * @name: Group
 * @brief: Group table represents groups created by users.
 */
CREATE TABLE IF NOT EXISTS `Group` (
    `GroupID` INT PRIMARY KEY NOT NULL, 	-- PK
    `UserID` INT NOT NULL,					-- FK
    `GroupName` VARCHAR(255),
    `Description` VARCHAR(255),
    `MemberCount` BIGINT,
    `CreationDate` DATE,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE
);

/**
 * @name: GroupUser
 * @brief: GroupUser table represents the association between users and groups.
 */
CREATE TABLE IF NOT EXISTS `GroupUser` (
    `GroupUserID` INT PRIMARY KEY NOT NULL, -- PK
    `UserID` INT NOT NULL, 					-- FK
    `GroupID` INT NOT NULL, 				-- FK
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE,
    FOREIGN KEY (`GroupID`) REFERENCES `Group` (`GroupID`) ON UPDATE CASCADE
);

/**
 * @name: Message
 * @brief: Message table represents messages sent between users.
 */
CREATE TABLE IF NOT EXISTS `Message` (
    `MessageID` INT PRIMARY KEY NOT NULL, 	-- PK
    `UserIDSender` INT NOT NULL, 			-- FK
    `UserIDReciever` INT NOT NULL, 			-- FK
    `Content` VARCHAR(255),
    `Timestamp` DATETIME,
    `Status` ENUM('sent', 'delivered', 'read'),
    FOREIGN KEY (`UserIDSender`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE,
    FOREIGN KEY (`UserIDReceiver`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE
);

/**
 * @name: Goal
 * @brief: Goal table represents user goals.
 */
CREATE TABLE IF NOT EXISTS `Goal` (
    `GoalID` INT PRIMARY KEY NOT NULL, 		-- PK
    `UserID` INT NOT NULL,  				-- FK
    `ProfileID` INT NOT NULL, 				-- FK
    `Content` VARCHAR(255),
    `DatePosted` DATE,
    `Frequency` ENUM('daily', 'weekly', 'monthly', 'annually'),
    `Score` BIGINT,
    `PrivacySettings` ENUM('Public', 'Private', 'Brand', 'Athlete', 'FriendsOnly'),
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE,
    FOREIGN KEY (`ProfileID`) REFERENCES `Profile` (`ProfileID`) ON UPDATE CASCADE
);

/**
 * @name: Plant
 * @brief: Plant table represents user's progress on goals.
 */
CREATE TABLE IF NOT EXISTS `Plant` (
    `PlantID` INT PRIMARY KEY NOT NULL, 	-- PK
    `GoalID` INT NOT NULL, 					-- FK
    `ProfileID` INT NOT NULL,				-- FK
    `StreakAlive` BOOLEAN,
    `StreakDuration` BIGINT,
    `DaysStreakDead` BIGINT,
    `DaysStreakKeptAlive` BIGINT,
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`) ON UPDATE CASCADE,
    FOREIGN KEY (`ProfileID`) REFERENCES `Profile` (`ProfileID`) ON UPDATE CASCADE
);

/**
 * @name: Comment
 * @brief: Comment table represents comments made on goals.
 */
CREATE TABLE IF NOT EXISTS `Comment` (
    `CommentID` INT PRIMARY KEY NOT NULL,	-- PK
    `UserID` INT NOT NULL,					-- FK
    `GoalID` INT NOT NULL,					-- FK
    `Content` VARCHAR(255),
    `Timestamp` TIMESTAMP,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE,
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`) ON UPDATE CASCADE
);

/**
 * @name: Like
 * @brief: Like table represents likes on goals.
 */
CREATE TABLE IF NOT EXISTS `Like` (
    `LikeID` INT PRIMARY KEY NOT NULL,		-- PK
    `GoalID` INT NOT NULL,					-- FK
    `UserID` INT NOT NULL,					-- FK
    `Timestamp` TIMESTAMP,
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`) ON UPDATE CASCADE,
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE
);

/**
 * @name: Media
 * @brief Media table represents media content associated with goals.
 */
CREATE TABLE IF NOT EXISTS `Media` (
    `MediaID` INT PRIMARY KEY NOT NULL,		-- PK
    `GoalID` INT NOT NULL,					-- FK
    `UserID` INT NOT NULL,					-- FK
    `Content` BLOB,
    `DateUploaded` DATE,
    `PrivacySettings` ENUM('Public', 'Private', 'Brand', 'Athlete', 'FriendsOnly'),
    FOREIGN KEY (`GoalID`) REFERENCES `Goal` (`GoalID`) ON UPDATE CASCADE,
    FOREIGN KEY (`UderID`) REFERENCES `User` (`UserID`) ON UPDATE CASCADE
);


