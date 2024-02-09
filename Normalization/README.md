# Normalization

## Title: Q_Project Milestone 2
---
### Note on Data Population
At this stage, the table remains devoid of any data entries. Therefore, when we refer to *"<u>all data in the table is atomic</u>"* we emphasize the absence of comma-separated values within the table

---
<!--
Normalization:

First Normal Form (1NF): 
    - Ensures that each table has a unique identifier and that all attributes contain atomic values, 
      meaning they cannot be further divided.

Second Normal Form (2NF): 
    - Requires that each non-key attribute is fully functionally dependent on the entire primary key, 
      eliminating partial dependencies.

Third Normal Form (3NF): 
    - Ensures that there are no transitive dependencies, meaning that non-key attributes are not 
      dependent on other non-key attributes within the same table.

-->
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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`ProfileID`) and all attributes contain atomic values.

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`ProfileID`), and there are no transitive dependencies present.


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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`UserID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`UserID`), and there are no transitive dependencies present.
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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`GroupID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`GroupID`), and there are no transitive dependencies present.

---
<!-- 4 -->
### GroupUser Table

- **Attributes**: 
  - `GroupUserID (PK)` 
  - `UserID (FK)`
  - `GroupID (FK)` 
  <br>
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`GroupUserID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key. Additionally, the use of a composite primary key (`UserID` and `GroupID`) ensures uniqueness and further eliminates potential partial dependencies.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`GroupUserID`), and there are no transitive dependencies present.

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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`PlantID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`PlantID`), and there are no transitive dependencies present.

---
<!-- 6 -->
### Message Table

- **Attributes**: 
  - `MessageID (PK)`
  - `UserID (FK)`
  - `UserID (FK)`
  - `Content`
  - `Timestamp`
  - `Status`
  <br>
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`MessageID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`MessageID`), and there are no transitive dependencies present.


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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`GoalID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key. Additionally, composite keys or multiple candidate keys, if present, have been appropriately identified and accounted for in the design.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`GoalID`), and there are no transitive dependencies present.

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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`CommentID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`CommentID`), and there are no transitive dependencies present.


---
<!-- 9 -->
### Like Table

- **Attributes**: 
  - `LikeID (PK)`
  - `GoalID (FK)`
  - `UserID (FK)`
  - `Timestamp`
  <br>
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`LikeID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`LikeID`), and there are no transitive dependencies present.

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
- **Normalization Level**: `1NF`
  - **Justification**: The table is in the first normal form (`1NF`) as it includes a unique identifier (`MediaID`) and all attributes contain atomic values.
<br>

- **Normalization Level**: `2NF`
  - **Justification**: The table satisfies the second normal form (`2NF`) by eliminating partial dependencies, ensuring that every attribute is fully functionally dependent on the entire primary key.
<br>

- **Normalization Level**: `3NF`
  - **Justification**: The table meets the requirements of the third normal form (`3NF`) as all attributes are fully functionally dependent on the primary key (`MediaID`), and there are no transitive dependencies present.