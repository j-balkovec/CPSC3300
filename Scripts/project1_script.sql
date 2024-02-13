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
    `PhoneNumber` VARCHAR(255) UNIQUE,       
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

/**
 * -----------------------------------------------------------------
 * @brief: Insert 10 mock entries into each table.
 * -----------------------------------------------------------------
 */

/**
* @table: User
* @brief: Data accquired with the help of the 'faker' and 'bcrypt' libraries in Python
*/
INSERT INTO `User` (`UserID`, `Username`, `Password`, `Email`, `PhoneNumber`, `DateOfBirth`)
VALUES 
(1, 'ncole', '$2b$12$xqRuTccHGaAbvqLX2yeuGeGXXTHUD96KNCaACzxq/x6l6N/bUI36a', 'ncole@example.net', '212-282-7306', '1990-01-01'),
(2, 'robertocurry', '$2b$12$U6nLlr2u2bq6ey285kKE/umMMW0dM4vwsKzVpHOhqdzWnetEMEVQy', 'robertocurry@example.org', '527-958-9099x74074', '1985-03-15'),
(3, 'johnsoneric', '$2b$12$1NtB1L7Cx0K/K6126byRzeysIgD7UgXIugkGThRd/eQqLE//m6Kjy', 'johnsoneric@example.com', '001-648-919-3759x25086', '1992-07-20'),
(4, 'kathleen22', '$2b$12$mwsL.oRD2Vorj7re.xQNFe9/nANnqrKVzRG6zgMGPdxzdg7EAWQnq', 'kathleen22@example.org', '+1-635-592-2912x588', '1988-09-10'),
(5, 'burchjustin', '$2b$12$rWY9uBKnn4e6DDAJ4L48GuRPc9eS0vC0C6/CJSaenQP/9W5wvHYcy', 'burchjustin@example.net', '(658)975-1782x757', '1987-11-25'),
(6, 'hebertjessica', '$2b$12$p0FisujbfFH8u22xep/7TeWGruwhFlXtzp/LdfQ5kTtz6jZFT4Eba', 'hebertjessica@example.com', '001-944-531-7390x91580', '1995-05-12'),
(7, 'billywong', '$2b$12$oxNW.tlZsiZ0hnrctJAovueOLc5UlyOasxlxXQTFlZkGzfhsru4HC', 'billywong@example.org', '001-844-752-2758x1216', '1993-02-28'),
(8, 'brittney21', '$2b$12$.ZdhLkofNx.bHhTFh.XNcO9q8CqJp7GSelP1YazFd1DOxS0XDiWQ6', 'brittney21@example.net', '(525)965-7667x5309', '1991-04-17'),
(9, 'wardoscar', '$2b$12$MirjAkSGJ6dVosmsrIvgNu5tTxIHXcuU41itr32TANzVS3i9cPFLi', 'wardoscar@example.com', '+1-233-911-8123x69395', '1994-08-03'),
(10, 'michael91', '$2b$12$6Dum5O3B9VdWTFQ/q89tZOfMb6ebnAS6ZINn92Cy1agEcNZOWbYc2', 'michael91@example.org', '001-584-702-0321x2347', '1989-12-07');

/**
* @table: Profile
* @brief: Data accquired with the help of the 'faker' and 'bcrypt' libraries in Python
* @attention: Types (BLOB) are left NULL purposefully until we figure something else out 
*/
INSERT INTO `Profile` (`ProfileID`, `UserID`, `Bio`, `Education`, `Job`, `Interests`, `PrivacySettings`, `ProfilePicture`, `CoverPhoto`, `JoinDate`, `LastActive`)
VALUES 
(1, 1, 'Lorem ipsum dolor sit amet.', 'Bachelor of Science in Computer Science', 'Software Engineer', 'Programming, Reading, Hiking', 'Public', NULL, NULL,'2023-01-15', '2024-02-12 08:30:00'),
(2, 2, 'Ut enim ad minim veniam.', 'Master of Business Administration', 'Marketing Manager', 'Traveling, Photography, Cooking', 'Private', NULL, NULL, '2023-02-20', '2024-02-12 10:45:00'),
(3, 3, 'Duis aute irure dolor in reprehenderit.', 'Bachelor of Arts in English Literature', 'Editor', 'Writing, Painting, Music', 'Brand', NULL, NULL, '2023-03-10', '2024-02-12 12:15:00'),
(4, 4, 'Excepteur sint occaecat cupidatat non proident.', 'Bachelor of Science in Biology', 'Research Scientist', 'Scuba Diving, Yoga, Gardening', 'Athlete',  NULL, NULL, '2023-04-05', '2024-02-12 14:20:00'),
(5, 5, 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Bachelor of Fine Arts in Graphic Design', 'Graphic Designer', 'Drawing, Calligraphy, Typography', 'Private', NULL, NULL, '2023-05-18', '2024-02-12 16:10:00'),
(6, 6, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Bachelor of Science in Psychology', 'Clinical Psychologist', 'Meditation, Mindfulness, Traveling', 'Public', NULL, NULL, '2023-06-30', '2024-02-12 18:55:00'),
(7, 7, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Phasellus volutpat enim et turpis.', 'Bachelor of Arts in History', 'Historian', 'Archaeology, Ancient Civilizations, Photography', 'Private', NULL, NULL, '2023-07-11', '2024-02-12 20:30:00'),
(8, 8, 'Morbi in sem quis dui placerat ornare.', 'Master of Science in Environmental Science', 'Environmental Consultant', 'Hiking, Birdwatching, Sustainability', 'Brand', NULL, NULL, '2023-08-25', '2024-02-12 22:45:00'),
(9, 9, 'Praesent blandit dolor sed nunc venenatis gravida.', 'Bachelor of Science in Mechanical Engineering', 'Mechanical Engineer', 'DIY Projects, Robotics, Automotive', 'Athlete', NULL, NULL, '2023-09-19', '2024-02-13 01:05:00'),
(10, 10, 'Cras mattis consectetur purus sit amet fermentum.', 'Bachelor of Arts in Sociology', 'Social Worker', 'Volunteering, Community Outreach, Social Justice', 'Private', NULL, NULL, '2023-10-07', '2024-02-13 03:20:00');

/**
* @table: Group
* @brief: Data accquired with the help of the 'faker' and 'bcrypt' libraries in Python
*/
INSERT INTO `Group` (`GroupID`, `UserID`, `GroupName`, `Description`, `MemberCount`, `CreationDate`)
VALUES 
(1, 1, 'Tech Enthusiasts', 'A group for technology enthusiasts to discuss latest trends and developments.', 20, '2023-01-15'),
(2, 2, 'Fitness Freaks', 'A group dedicated to fitness enthusiasts to share workout routines and motivate each other.', 15, '2023-02-20'),
(3, 3, 'Book Club', 'A book club where members discuss and review books they are reading.', 30, '2023-03-10'),
(4, 4, 'Photography Lovers', 'A group for photography enthusiasts to share their photos and techniques.', 25, '2023-04-05'),
(5, 5, 'Foodies Unite', 'A group for food lovers to share recipes, restaurant recommendations, and cooking tips.', 40, '2023-05-18'),
(6, 6, 'Travel Addicts', 'A group for travel enthusiasts to share travel experiences, tips, and destination recommendations.', 50, '2023-06-30'),
(7, 7, 'Artists Collective', 'A group for artists to showcase their artwork, discuss techniques, and collaborate on projects.', 20, '2023-07-11'),
(8, 8, 'Entrepreneurship Hub', 'A group for aspiring and established entrepreneurs to share insights, resources, and networking opportunities.', 35, '2023-08-25'),
(9, 9, 'Music Lovers', 'A group for music enthusiasts to discuss their favorite genres, artists, and concerts.', 45, '2023-09-19'),
(10, 10, 'Film Buffs', 'A group for film enthusiasts to discuss movies, directors, and upcoming releases.', 30, '2023-10-07');

/**
* @table: GroupUser
* @brief: Data accquired with the help of the 'faker' and 'bcrypt' libraries in Python
*/
INSERT INTO `GroupUser` (`GroupUserID`, `UserID`, `GroupID`)
VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

/**
* @table: Message
* @brief: Data accquired with the help of the 'faker' and 'bcrypt' libraries in Python
*/
INSERT INTO `Message` (`MessageID`, `UserIDSender`, `UserIDReceiver`, `Content`, `Timestamp`, `Status`)
VALUES 
(1, 1, 2, 'Hello there!', '2024-02-12 08:00:00', 'sent'),
(2, 2, 1, 'Hi, how are you?', '2024-02-12 08:05:00', 'delivered'),
(3, 3, 4, 'Meeting at 3 PM today.', '2024-02-12 09:00:00', 'sent'),
(4, 4, 3, 'Got it, thanks!', '2024-02-12 09:05:00', 'delivered'),
(5, 5, 6, 'Are you coming to the party?', '2024-02-12 10:00:00', 'sent'),
(6, 6, 5, 'Yes, I will be there.', '2024-02-12 10:05:00', 'delivered'),
(7, 7, 8, 'DO NOT forget about the deadline tomorrow.', '2024-02-12 11:00:00', 'sent'),
(8, 8, 7, 'I am on it, thanks for the reminder!', '2024-02-12 11:05:00', 'delivered'),
(9, 9, 10, 'Lunch at 3PM today?', '2024-02-12 12:00:00', 'sent'),
(10, 10, 9, 'Sure, where do you want to go?', '2024-02-12 12:05:00', 'delivered');

/**
* @table: Goal
* @brief: Data accquired with the help of the 'faker' and 'bcrypt' libraries in Python
*/
INSERT INTO `Goal` (`GoalID`, `UserID`, `ProfileID`, `Content`, `DatePosted`, `Frequency`, `Score`, `PrivacySettings`)
VALUES 
(1, 1, 1, 'Exercise for 30 minutes', '2024-02-12', 'daily', 10, 'Public'),
(2, 2, 2, 'Read a book', '2024-02-12', 'weekly', 20, 'Private'),
(3, 3, 3, 'Learn a new programming language', '2024-02-12', 'monthly', 30, 'Private'),
(4, 4, 4, 'Meditate for 15 minutes', '2024-02-12', 'daily', 15, 'Public'),
(5, 5, 5, 'Write a journal entry', '2024-02-12', 'weekly', 25, 'Brand'),
(6, 6, 6, 'Complete a coding project', '2024-02-12', 'monthly', 35, 'Athlete'),
(7, 7, 7, 'Practice playing the guitar', '2024-02-12', 'daily', 12, 'Private'),
(8, 8, 8, 'Learn a new recipe', '2024-02-12', 'weekly', 22, 'Private'),
(9, 9, 9, 'Run 5 kilometers', '2024-02-12', 'daily', 18, 'Public'),
(10, 10, 10, 'Study for exams', '2024-02-12', 'monthly', 28, 'Brand');

/**
* @table: Plant
* @brief: Data accquired with the help of the 'faker', 'bcrypt' and 'random' libraries in Python
*/
INSERT INTO `Plant` (`PlantID`, `GoalID`, `ProfileID`, `StreakAlive`, `StreakDuration`, `DaysStreakDead`, `DaysStreakKeptAlive`)
VALUES 
(1, 1, 1, TRUE, 30, 0, 30),
(2, 2, 2, TRUE, 15, 0, 15),
(3, 3, 3, FALSE, 0, 10, 0),
(4, 4, 4, TRUE, 45, 0, 45),
(5, 5, 5, FALSE, 0, 20, 0),
(6, 6, 6, TRUE, 60, 0, 60),
(7, 7, 7, TRUE, 75, 0, 75),
(8, 8, 8, FALSE, 0, 5, 0),
(9, 9, 9, TRUE, 90, 0, 90),
(10, 10, 10, TRUE, 30, 0, 30);

/**
* @table: Comment
* @brief: Data accquired with the help of the 'faker', 'bcrypt' and libraries in Python
*/
INSERT INTO `Comment` (`CommentID`, `UserID`, `GoalID`, `Content`, `Timestamp`)
VALUES 
(1, 1, 1, 'Great progress!', '2024-02-12 09:30:00'),
(2, 2, 1, 'Keep it up!', '2024-02-12 10:15:00'),
(3, 3, 2, 'Impressive work!', '2024-02-12 11:00:00'),
(4, 4, 3, 'You can do it!', '2024-02-12 12:00:00'),
(5, 5, 4, 'Almost there!', '2024-02-12 13:00:00'),
(6, 6, 5, 'Stay motivated!', '2024-02-12 14:00:00'),
(7, 7, 6, 'Keep pushing!', '2024-02-12 15:00:00'),
(8, 8, 7, 'You got this!', '2024-02-12 16:00:00'),
(9, 9, 8, 'Amazing effort!', '2024-02-12 17:00:00'),
(10, 10, 9, 'Inspiring!', '2024-02-12 18:00:00');

/**
* @table: Like
* @brief: Data accquired with the help of the 'faker', 'bcrypt' and libraries in Python
*/
-- Mock data for likes on goals
INSERT INTO `Like` (`LikeID`, `GoalID`, `UserID`, `Timestamp`)
VALUES 
(1, 1, 1, '2024-02-12 09:30:00'),
(2, 2, 2, '2024-02-12 10:15:00'),
(3, 3, 3, '2024-02-12 11:00:00'),
(4, 4, 4, '2024-02-12 12:00:00'),
(5, 5, 5, '2024-02-12 13:00:00'),
(6, 6, 6, '2024-02-12 14:00:00'),
(7, 7, 7, '2024-02-12 15:00:00'),
(8, 8, 8, '2024-02-12 16:00:00'),
(9, 9, 9, '2024-02-12 17:00:00'),
(10, 10, 10, '2024-02-12 18:00:00');

/**
* @table: Media
* @brief: Data accquired with the help of the 'faker', 'bcrypt' and libraries in Python
* @attention: Types (BLOB) are left NULL purposefully until we figure something else out 
*/
INSERT INTO `Media` (`MediaID`, `GoalID`, `UserID`, `Content`, `DateUploaded`, `PrivacySettings`)
VALUES 
(1, 1, 1, NULL, '2024-02-12', 'Public'),
(2, 2, 2, NULL, '2024-02-12', 'Private'),
(3, 3, 3, NULL, '2024-02-12', 'Brand'),
(4, 4, 4, NULL, '2024-02-12', 'Athlete'),
(5, 5, 5, NULL, '2024-02-12', 'Private'),
(6, 6, 6, NULL, '2024-02-12', 'Public'),
(7, 7, 7, NULL, '2024-02-12', 'Private'),
(8, 8, 8, NULL, '2024-02-12', 'Brand'),
(9, 9, 9, NULL, '2024-02-12', 'Athlete'),
(10, 10, 10, NULL, '2024-02-12', 'Private');

/**
 * -----------------------------------------------------------------
 * @brief: Verify changes.
 * -----------------------------------------------------------------
 */
SELECT * FROM `User`;
SELECT * FROM `Profile`;
SELECT * FROM `Group`;
SELECT * FROM `GroupUser`;
SELECT * FROM `Message`;
SELECT * FROM `Goal`;
SELECT * FROM `Plant`;
SELECT * FROM `Comment`;
SELECT * FROM `Like`;
SELECT * FROM `Media`;