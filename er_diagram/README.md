# ER Diagram Description

## Title: Q_Project Milestone 1

## Project Description:
The project revolves around achieving personal goals, fostering growth, and encouraging collaboration. Upon creating a profile, each user is assigned a plant for every goal they set. Progress towards these goals directly influences the growth of their respective plants. Additionally, the application facilitates collaborative efforts by enabling group goals, where all participants share a common plant. Contributions towards these collective objectives contribute to the plant's development as well. Furthermore, members can engage in group discussions through a built-in group chat feature. The collective progress of all plants is showcased on a virtual field, with tags identifying the associated goals for each plant.

## ERD Description
The ER diagram depicts the conceptual schema of the database system, illustrating the entities, attributes, and relationships that comprise the data model. Below is a comprehensive description of each component:

## Entities:
- **`Profile`**: Represents the user's profile information, including personal details, preferences, and settings. 
<br>

- **`User`**: Represents an individual user within the application, containing attributes such as username, email, password, and profile picture.
<br>

- **`Group`**: Represents a collective entity formed by multiple users collaborating towards common goals or interests.
<br>

- **`GroupUser`**: Serves as a link between users and groups, defining the membership relationship between individual users and specific groups.
<br>

- **`Plant`**: Represents a visual representation of a user's progress towards their goals, with attributes reflecting the plant's growth status and associated goals.
<br>

- **`Message`**: Represents a communication sent within the application, facilitating interaction between users or within groups.
<br>

- **`Goal`**: Defines the objectives or targets set by users, with attributes describing the goal's name, description, deadline, and status.
<br>

- **`Comment`**: Represents user-generated feedback or remarks associated with specific goals, messages, or media content.
<br>

- **`Like`**: Represents user interactions indicating approval or appreciation for specific content, such as messages, comments, or media.
<br>

- **`Media`**: Represents multimedia content uploaded or shared within the application, including images, videos, or documents, with attributes detailing the media type, file size, and associated user or group.

### Attributes:
Each entity in the diagram is associated with a set of attributes that describe its properties. Attributes are listed below for each entity:
</br>

### **Profile**
  - **`[PK] ProfileID (INT) NOT NULL`**: Primary Key, uniquely identifies each profile.
  - ***`[FK1] UserID (INT) NOT NULL`***: Foreign Key referencing the User entity, links the profile to its respective user.
  - `Bio (VARCHAR(n))`: Textual description of the user's biography or personal information.
  - `Education (VARCHAR(n))`: Information about the user's educational background or qualifications.
  - `Job (VARCHAR(n))`: Description of the user's current employment.
  - `Interests (VARCHAR(n))`: User's interests or hobbies, providing insights into their preferences.
  - `PrivacySettings (ENUM)`: Enumerated type indicating the user's chosen privacy settings for their profile. (Public, Private, Brand, Athlete, ...)
  - `ProfilePicture (BLOB)`: Binary Large Object (BLOB) storing the user's profile picture image.
  - `CoverPhoto (BLOB)`: BLOB storing the user's cover photo or banner image displayed on their profile.
  - `JoinDate (DATE)`: Date when the user joined the platform or created their profile.
  - `LastActive (DATETIME)`: Timestamp indicating the user's last activity on the platform, capturing both date and time.

### **User**
  - **`[PK] UserID (INT) NOT NULL`**: Primary Key, uniquely identifies each user.
  - `Username (VARCHAR(n))`: Unique username chosen by the user for their account.
  - `Password (VARCHAR(n) [HASHED])`: Hashed representation of the user's password for security.
  - `Email (VARCHAR(n))`: Email address associated with the user's account.
  - `PhoneNumber (VARCHAR(11))`: Phone number linked to the user's account, typically for verification for communication purposes/double authentication.
  - `DateOfBirth (DATE)`: Date representing the user's date of birth.
 
### **Group**
  - **`[PK] GroupID (INT) NOT NULL`**: Primary Key, uniquely identifies each group.
  - ***`[FK1] UserID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the User to the respective Group.
  - `GroupName (VARCHAR(n))`: Unique username chosen by the admin for their group.
  - `Description (VARCHAR(n))`: Describes the group, their mission, goals, interests, etc.
  - `MemberCount (BIGINT)`: Number of members.
  - `CreationDate (DATE)`: Date when the group was created.
 
### **GroupUser**
  - **`[PK] GroupUserID (INT) NOT NULL`**: Primary Key, uniquely identifies each group user.
  - ***`[FK1] UserID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the group user to its respective user.
  - ***`[FK2] GroupID (INT) NOT NULL`***: Foreign Key referencing the Group entity, linking the group user to its respective group.

### **Plant**
  - **`[PK] PlantID (INT) NOT NULL`**: Primary Key, uniquely identifies each plant.
  - ***`[FK1] GoalID (INT) NOT NULL`***: Foreign Key referencing the Goal entity, linking the Plant to its respective Goal.
  - ***`[FK2] ProfileID (INT) NOT NULL`***: Foreign Key referencing the Profile entity, linking the Plant to its respective Profile.
  - `StreakAlive (BOOLEAN)`: Indicates whether the streak associated with the plant is currently alive (true) or not (false).
  - `StreakDuration (BIGINT)`: The total duration of the streak associated with the plant, measured in days.
  - `DaysStreakDead (BIGINT)`: The number of days the streak associated with the plant has been inactive or dead.
  - `DaysStreakKeptAlive (BIGINT)`: The total number of days the streak associated with the plant has been maintained or kept alive.
 
### **Message**
  - **`[PK] MessageID (INT) NOT NULL`**: Primary Key, uniquely identifies each message.
  - ***`[FK1] UserID (INT) NOT NULL UNIQUE {SENDER}`***: Foreign Key referencing the User entity, linking the Message to its respective User.
  - ***`[FK2] UserID (INT) NOT NULL UNIQUE {RECIEVER}`***: Foreign Key referencing the User entity, linking the Message to its respective User. 
  - `Content (VARCHAR(n))`: Textual content of the message.
  - `Timestamp (DATETIME)`: Date and time when the message was sent.
  - `Status (ENUM)`: Indicates the status of the message, such as "sent," "delivered," or "read."

### **Goal**
  - **`[PK] GoalID (INT) NOT NULL`**: Primary Key, uniquely identifies each goal.
  - ***`[FK1] UserID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the Goal to its respective User.
  - ***`[FK2] ProfileID (INT) NOT NULL`***: Foreign Key referencing the Profile entity, linking the Goal to its respective Profile.
  - `Content (VARCHAR(n))`: Description or content of the goal.
  - `DatePosted (DATE)`: Date when the goal was posted or created.
  - `Frequency (ENUM)`: Enumerated type indicating the frequency or recurrence of the goal (e.g., daily, weekly, monthly).
  - `Score (BIGINT)`: Numerical score or rating associated with the goal's achievement or progress.
  - `PrivacySettings (ENUM)`: Enumerated type representing the privacy settings of the goal, determining who can view or interact with it.

### **Comment**
  - **`[PK] CommentID (INT) NOT NULL`**: Primary Key, uniquely identifies each comment.
  - ***`[FK1] UserID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the Comment to its respective User.
  - ***`[FK2] GoalID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the Comment to its respective Goal.
  - `Content (VARCHAR(n))`: Content of the comment.
  - `Timestamp (TIMESTAMP)`: Date and time when the comment was made.

### **Like**
  - **`[PK] LikeID (INT) NOT NULL`**: Primary Key, uniquely identifies each like.
  - ***`[FK1] GoalID (INT) NOT NULL`***: Foreign Key referencing the Goal entity, linking the Like to its respective Goal.
  - ***`[FK2] UserID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the Like to its respective User.
  - `Timestamp (TIMESTAMP)`: Date and time when the like was registered or recorded. This timestamp indicates when the like was given or generated.

### **Media**
  - **`[PK] MediaID (INT) NOT NULL`**: Primary Key, uniquely identifies each media.
  - ***`[FK1] GoalID (INT) NOT NULL`***: Foreign Key referencing the User entity, linking the Message to its respective User.
  -- ***`[FK2] UserID (INT) NOT NULL`***
  - `Content (BLOB)`: Binary Large Object (BLOB) field to store the media content.
  - `DateUploaded (DATE)`: Date when the media was uploaded or created.
  - `PrivacySettings (ENUM)`: Enumerated type representing the privacy settings of the media, determining who can view or access it.

``

### Relationships:
- **`User-Comment`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each user can add multiple comments, but a comment is authored by only one user.
  - **Cardinality**: 
    - One user can leave multiple comments, while each comment is associated with only one user.
  - **Participation**: 
    - Optional participation on the comment side (a comment may or may not be written by a user), and mandatory participation on the user side (each comment must be associated with a user).

- **`User-Like`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each user can give out multiple life, but a like belongs to only one user.
  - **Cardinality**: 
    - One user can leave multiple like, while each like is associated with only one user.
  - **Participation**: 
    - Optional participation on the like side (a like may or may not be given out by a user), and mandatory participation on the user side (each like must be associated with a user).

- **`Goal-Media`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each goal can have multiple pictures/videos/GIFs, but a picture belongs to only one goal.
  - **Cardinality**: 
    - One goal can contain multiple pictures/videos/GIFs, while each pictures/videos/GIFs is associated with only one goal.
  - **Participation**: 
    - Optional participation on the media side (media may or may not be added to the goal), and mandatory participation on the goal side (media must be associated with a goal (post)).

- **`Goal-Like`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each goal can have multiple likes, but a like belongs to only one goal.
  - **Cardinality**: 
    - One goal can contain multiple likes, while each like is associated with only one goal.
  - **Participation**: 
    - Optional participation on the like side (a goal may or may not be liked by some user), and mandatory participation on the goal side (each like must be associated with a goal (post)).

- **`Goal-Comment`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each goal can have multiple comments, but a comment belongs to only one goal.
  - **Cardinality**: 
    - One goal can have multiple comments, while each comment is associated with only one goal.
  - **Participation**: 
    - Optional participation on the comment side (a comment may or may not be added to a goal), and mandatory participation on the goal side (each comment must be associated with a goal).

- **`User-Goal`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each user can create multiple goals, but a goal is authored by only one user.
  - **Cardinality**: 
    - One user can create/set multiple goals, while each goal is associated with only one user.
  - **Participation**: 
    - Optional participation on the goal side (a goal may or may not be set by a user), and mandatory participation on the user side (each goal must be associated with a user).

- **`GroupUser-User`**
  - **Type**: One-to-Many Optional
  - **Description**: 
    - Each group user belongs to one user, while one user can belong to multiple group users.
  - **Cardinality**: 
    - One user can be associated with multiple group users, but each group user is linked to only one user.
  - **Participation**: 
    - Mandatory participation on the GroupUser side (each group user must be associated with a user), and optional participation on the User side (a user may or may not be associated with a group user).

- **`GroupUser-Group`**
  - **Type**: One-to-Many Optional
  - **Description**: 
    - Each group user can belong to one group, while one group can have multiple group users. Participation is optional on the group side, meaning a group may or may not have associated group users.
  - **Cardinality**: 
    - One group can be associated with multiple group users, but each group user is linked to only one group.
  - **Participation**: 
    - Mandatory participation on the group user side (each group user must be associated with a group), and optional participation on the group side (a group may or may not have associated group users).

- **`Profile-User`**
  - **Type**: One-to-One Mandatory 
  - **Description**: 
    - Each profile is associated with exactly one user, and each user is associated with exactly one profile.
  - **Cardinality**: 
    - Each profile is linked to one user, and each user is linked to one profile.
  - **Participation**: 
    - Mandatory participation on both sides (each profile must be associated with a user, and each user must be associated with a profile).

- **`User-Message`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each user can send/receive multiple messages, while each message is sent by only one user. Participation is optional on the message side, meaning a message may or may not be associated with a user.
  - **Cardinality**: 
    - One user can send/receive multiple messages, but each message is sent by only one user.
  - **Participation**: 
    - Mandatory participation on the user side (each message must be associated with a user), and optional participation on the message side (a user may or may not send a message).

- **`Profile-Goal`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each profile shows multiple goals, while each goal belongs to only one profile. This relationship represents the goals associated with a particular profile.
  - **Cardinality**: 
    - One profile show multiple goals, but each goal is associated with only one profile.
  - **Participation**: 
    - Mandatory participation on the profile side (each goal must be associated with a profile), and optional participation on the goal side (a profile may or may not have associated goals).

- **`Group-Message`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each group can have multiple messages, while each message belongs to only one group. This relationship represents the messages associated with a particular group.
  - **Cardinality**: 
    - One group can have multiple messages, but each message is associated with only one group.
  - **Participation**: 
    - Mandatory participation on the group side (each message must be associated with a group), and optional participation on the message side (a group may or may not have associated messages).

- **`Group-Goal`**
  - **Type**: One-to-Many Optional
  - **Description**: 
    - Each group or group member can share multiple goals, while each goal belongs to only one group or group member. This relationship represents the goals shared by a group or its members.
  - **Cardinality**: 
    - One group or group member can share multiple goals, but each goal is associated with only one group or group member.
  - **Participation**: 
    - Mandatory participation on the group or group member side (each goal must be associated with a group or group member), and optional participation on the goal side (a group or group member may or may not have associated goals).
 
- **`Goal-Plant`**
  - **Type**: Mandatory One-to-One
  - **Description**: 
    - Each goal is associated with exactly one plant, and each plant is associated with exactly one goal. This relationship represents the goal's contribution to the growth of a specific plant.
  - **Cardinality**: 
    - Each goal is linked to one plant, and each plant is linked to one goal.
  - **Participation**: 
    - Mandatory participation on both sides (each goal must be associated with a plant, and each plant must be associated with a goal).

- **`GroupUser-Message`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each group user can send multiple messages, while each message is sent by only one group user. This relationship represents the messages sent by a particular group user.
  - **Cardinality**: 
    - One group user can send multiple messages, but each message is sent by only one group user.
  - **Participation**: 
    - Mandatory participation on the group user side (each message must be associated with a group user), and optional participation on the message side (a group user may or may not send a message).

- **`Profile-Plant`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each profile can have multiple plants, while each plant belongs to only one profile. This relationship represents the plants associated with a particular profile.
  - **Cardinality**: 
    - One profile can have multiple plants, but each plant is associated with only one profile.
  - **Participation**: 
    - Mandatory participation on the profile side (each plant must be associated with a profile), and optional participation on the plant side (a profile may or may not have associated plants).

- **`User-Media`**
  - **Type**: Mandatory One-to-Many Optional
  - **Description**: 
    - Each User can add multiple pictures/videos/GIFs, while each pictures/videos/GIFs belongs to only one User.
  - **Cardinality**: 
    - One User can add multiple pictures/videos/GIFs, but each picture/video/GIF is associated with only one User.
  - **Participation**: 
    - Mandatory participation on the User side (each picture/video/GIF must be associated with a profile), and optional participation on the Media side (a User may or may not add media).

### Additional Notes:

- Things are subject to change.