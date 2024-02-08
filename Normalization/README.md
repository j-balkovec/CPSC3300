# Normalization

## Title: Q_Project Milestone 2
---
<!-- 1 -->
### Profile Table

- **Attributes**: 
  - `ProfileID (PK)` 
  - `UserID (FK)` 
  - `Bio`
  - `Education`
  - `Job`
  - `Interests` 
  - `PrivacySettings`
  - `ProfilePicture` 
  - `CoverPhoto`
  - `JoinDate`
  - `LastActive`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Profile table was designed in `3NF` from the outset. All attributes are fully functionally dependent on the primary key (`ProfileID`), and there are no transitive dependencies present. Each column contains atomic values, and there are no repeating groups.

---
<!-- 2 -->
### User Table

- **Attributes**: 
  - `UserID (PK)`
  - `Username`
  - `Password`
  - `Email`
  - `PhoneNumber`
  - `DateOfBirth`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: Similar to the Profile table, the User table follows `3NF` principles. All non-prime attributes are fully functionally dependent on the primary key (`UserID`), and there are no transitive dependencies present. Each column contains atomic values without any repeating groups.

---
<!-- 3 -->
### Group Table

- **Attributes**: 
  - `GroupID (PK)`
  - `UserID (FK)`
  - `GroupName`
  - `Description`
  - `MemberCount`
  - `CreationDate`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Group table is in `3NF`. All attributes are fully functionally dependent on the primary key (`GroupID`), and there are no transitive dependencies present. Each column contains atomic values, and there are no repeating groups.

---
<!-- 4 -->
### GroupUser Table

- **Attributes**: 
  - `GroupUserID (PK)` 
  - `UserID (FK)`
  - `GroupID (FK)` 
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The GroupUser table adheres to `3NF` principles. The primary key (GroupUserID) uniquely identifies each record, and the foreign keys (`UserID`, `GroupID`) establish relationships between users and groups. There are no transitive dependencies present.

---
<!-- 5 -->
### Plant Table

- **Attributes**: 
  - `PlantID (PK)`
  - `GoalID (FK)`
  - `ProfileID (FK)`
  - `StreakAlive`
  - `StreakDuration`
  - `DaysStreakDead`
  - `DaysStreakKeptAlive`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Plant table is in `3NF`. The primary key (`PlantID`) uniquely identifies each record, and the foreign keys (`GoalID`, `ProfileID`) establish relationships with the Goal and Profile tables, respectively. All attributes are fully functionally dependent on the primary key.

---
<!-- 6 -->
### Message Table

- **Attributes**: 
  - `MessageID (PK)`
  - `UserIDSender (FK)`
  - `UserIDReceiver (FK)`
  - `Content`
  - `Timestamp`
  - `Status`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Message table is in `3NF`. The primary key (MessageID) uniquely identifies each message, and the foreign keys (`UserIDSender`, `UserIDReceiver`) establish relationships with the User table. All attributes are fully functionally dependent on the primary key, and there are no transitive dependencies present.

---
<!-- 7 -->
### Goal Table

- **Attributes**: 
  - `GoalID (PK)`
  - `UserID (FK)`
  - `ProfileID (FK)`
  - `Content`
  - `DatePosted`
  - `Frequency`
  - `Score`
  - `PrivacySettings`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Goal table follows `3NF` principles. The primary key (`GoalID`) uniquely identifies each goal, and the foreign keys (`UserID`, `ProfileID`) establish relationships with the User and Profile tables. All attributes are fully functionally dependent on the primary key without any transitive dependencies.

---
<!-- 8 -->
### Comment Table

- **Attributes**: 
  - `CommentID (PK)`
  - `UserID (FK)`
  - `GoalID (FK)`
  - `Content`
  - `Timestamp`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Comment table adheres to `3NF` principles. The primary key (`CommentID`) uniquely identifies each comment, and the foreign keys (`UserID`, `GoalID`) establish relationships with the User and Goal tables. All attributes are fully functionally dependent on the primary key without any transitive dependencies.

---
<!-- 9 -->
### Like Table

- **Attributes**: 
  - `LikeID (PK)`
  - `GoalID (FK)`
  - `UserID (FK)`
  - `Timestamp`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Like table is in `3NF`. The primary key (`LikeID`) uniquely identifies each like, and the foreign keys (`GoalID`, `UserID`) establish relationships with the Goal and User tables. All attributes are fully functionally dependent on the primary key, and there are no transitive dependencies present.

---
<!-- 10 -->
### Media Table

- **Attributes**: 
  - `MediaID (PK)`
  - `GoalID (FK)`
  - `UserID (FK)`
  - `Content`
  - `DateUploaded`
  - `PrivacySettings`
  <br>
- **Normalization Level**: `3NF`
- **Justification**: The Media table follows `3NF` principles. The primary key (`MediaID`) uniquely identifies each media entry, and the foreign key (`GoalID`) establishes a relationship with the Goal table. All attributes are fully functionally dependent on the primary key without any transitive dependencies