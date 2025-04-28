--
-- File generated with SQLiteStudio v3.4.4 on Wed Apr 16 18:32:47 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Administrator
DROP TABLE IF EXISTS Administrator;

CREATE TABLE IF NOT EXISTS Administrator (
    Admin_Id TEXT PRIMARY KEY,
    Email    TEXT UNIQUE,
    Password TEXT
);

INSERT INTO Administrator (
                              Admin_Id,
                              Email,
                              Password
                          )
                          VALUES (
                              '001',
                              'charlotte.kim@sky.com',
                              'ChKim543!%'
                          );


-- Table: Badge
DROP TABLE IF EXISTS Badge;

CREATE TABLE IF NOT EXISTS Badge (
    Badge_Id   TEXT PRIMARY KEY,
    Tier_Level TEXT
);

INSERT INTO Badge (
                      Badge_Id,
                      Tier_Level
                  )
                  VALUES (
                      NULL,
                      'Diamond'
                  );

INSERT INTO Badge (
                      Badge_Id,
                      Tier_Level
                  )
                  VALUES (
                      NULL,
                      'Gold'
                  );

INSERT INTO Badge (
                      Badge_Id,
                      Tier_Level
                  )
                  VALUES (
                      NULL,
                      'Bronze'
                  );


-- Table: Department
DROP TABLE IF EXISTS Department;

CREATE TABLE IF NOT EXISTS Department (
    Department_Id   TEXT PRIMARY KEY,
    Department_Name      NOT NULL,
    User_Id         TEXT REFERENCES User (User_Id),
    Team_Id         TEXT REFERENCES Team (Team_Id) 
);


-- Table: Health_Card
DROP TABLE IF EXISTS Health_Card;

CREATE TABLE IF NOT EXISTS Health_Card (
    Health_Card_Id          TEXT PRIMARY KEY,
    Health_Card_Name        TEXT NOT NULL,
    Health_Card_Description TEXT
);

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Teamwork',
                            'Are you effectively working and collaborating together as a team?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Support',
                            'Are you receiving a great lebel of support and guidance?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Suitable Process',
                            'Is you way of working motivational and harmonic?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Speed',
                            'Do you get things done on time and efficiently?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Pawns or Players',
                            'Are you in control of deciding an dknowing how and what to build?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Mission',
                            'Do you know your purpose and have a clear picure/focus of what you are building?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Learning',
                            'Are you consistently learning interessting stuff?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Health of Code',
                            'Is quality of the code clean, easy to read and has great test coverage?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Fun',
                            'Do you love going to work and hav efun working with your team?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Easy to Release',
                            'Is releasing simple, painless and mostly automated?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Delivering Value',
                            'Are you delivering great value of work to the comany and its stakeholders?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Testing',
                            'Is most of your testing automated, no shortfalls, and you quickly adapt to discovered things through testing?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Right Tools for the Job',
                            'Do you have the right and high quality equipment to do your job well?'
                        );

INSERT INTO Health_Card (
                            Health_Card_Id,
                            Health_Card_Name,
                            Health_Card_Description
                        )
                        VALUES (
                            NULL,
                            'Work-Life',
                            'Do you have a balanced approached between work and other life roles and do you achieve set expectaions within office hours?'
                        );


-- Table: Health_Record
DROP TABLE IF EXISTS Health_Record;

CREATE TABLE IF NOT EXISTS Health_Record (
    Record_Id        INTEGER PRIMARY KEY,
    Record_Time      TEXT,
    Record_Date      TEXT,
    Team_Sum_Id      INTEGER REFERENCES Team_Summary (Team_Sum_Id),
    Session_Id       INTEGER UNIQUE
                             NOT NULL,
    Session_Duration NUMERIC,
    Session_Date     TEXT,
    Health_Card_Id   INTEGER REFERENCES Health_Card (Health_Card_Id),
    Depart_Id        TEXT    REFERENCES Department (Department_Id) 
);


-- Table: SKYE-AI
DROP TABLE IF EXISTS [SKYE-AI];

CREATE TABLE IF NOT EXISTS [SKYE-AI] (
    Chat_Id  TEXT PRIMARY KEY,
    Prompt   TEXT,
    Response TEXT,
    User_Id  TEXT REFERENCES User (User_Id) 
);


-- Table: Team
DROP TABLE IF EXISTS Team;

CREATE TABLE IF NOT EXISTS Team (
    Team_Id     TEXT PRIMARY KEY,
    Team_Name   TEXT NOT NULL,
    Depart_Id   TEXT REFERENCES Department (Department_Id),
    Team_Sum_Id TEXT REFERENCES Team_Summary (Team_Sum_Id) 
);


-- Table: Team_Summary
DROP TABLE IF EXISTS Team_Summary;

CREATE TABLE IF NOT EXISTS Team_Summary (
    Team_Sum_Id    TEXT    PRIMARY KEY,
    Vote_Average   REAL,
    Progress_Trend TEXT,
    Team_Id        TEXT    REFERENCES Team (Team_Id),
    Record_Id      INTEGER REFERENCES Health_Record (Record_Id) 
);


-- Table: User
DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User (
    User_Id           TEXT    PRIMARY KEY,
    Name              TEXT    NOT NULL,
    Email             TEXT    NOT NULL,
    Username          TEXT,
    Password          TEXT,
    Role              TEXT    NOT NULL,
    Admin_Id          TEXT    REFERENCES Administrator (Admin_Id),
    Session_Id        INTEGER UNIQUE,
    Session_Duration  NUMERIC,
    Session_Date      TEXT,
    Badge_Id          TEXT    REFERENCES Badge (Badge_Id),
    View_Profile      TEXT,
    Profile_Picture   BLOB,
    Login_Error_Times INTEGER
);

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '003',
                     'Liam Chen',
                     'liam.chen@sky.com',
                     'liam.chen@sky.com',
                     'ChenLi0003',
                     'Department Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '002',
                     'Emma Johnson',
                     'emma.johnson@sky.com',
                     'emma.johnson@sky.com',
                     'Emma002?',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '001',
                     'John Doe',
                     'john.doe@sky.com',
                     'john.doe@sky.com',
                     'John1234@!',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '004',
                     'Olivia Brown',
                     'olivia.brown@sky.com',
                     'olivia.brown@sky.com',
                     'Olivia2025@?',
                     'Senior Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '005',
                     'Noah Kim',
                     'noah.kim@sky.com',
                     'noah.kim@sky.com',
                     'Noah12345@!',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '006',
                     'Ava Martinez',
                     'ava.martinez@sky.com',
                     'ava.martinez@sky.com',
                     'Ava21109?',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '009',
                     'Taylor Brooks',
                     'taylor.brooks@sky.com',
                     'taylor.brooks@sky.com',
                     'TayBrooks007',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '008',
                     'Riley Morgan',
                     'riley.morgan@sky.com',
                     'riley.morgan@sky.com',
                     'Riley112@',
                     'Department Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '007',
                     'Sam Carter',
                     'sam.carter@sky.com',
                     'sam.carter@sky.com',
                     'SammyC122!',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '018',
                     'James Patel',
                     'james.patel@sky.com',
                     'james.patel@sky.com',
                     'JaPat876!$',
                     'Senior Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '017',
                     'Mason Brooks',
                     'mason.brooks@sky.com',
                     'mason.brooks@sky.com',
                     'MaBro654!@',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '016',
                     'Sophia Rivera',
                     'sophia.rivera@sky.com',
                     'sophia.rivera@sky.com',
                     'SoRiv987!*',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '015',
                     'Ava Parker',
                     'ava.parker@sky.com',
                     'ava.parker@sky.com',
                     'AvPar654!&',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '014',
                     'Noah Bennett',
                     'noah.bennett@sky.com',
                     'noah.bennett@sky.com',
                     'NoBen321!%',
                     'Senior Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '013',
                     'Olivia Hayes',
                     'olivia.hayes@sky.com',
                     'olivia.hayes@sky.com',
                     'OHay45',
                     'Department Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '012',
                     'Liam Carter',
                     'liam.carter@sky.com',
                     'liam.carter@sky.com',
                     'LiCar789!@',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '011',
                     'Emma Sullivan',
                     'emma.sullivan@sky.com',
                     'emma.sullivan@sky.com',
                     'EmSul123!#',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '010',
                     'Izzy Foster',
                     'izzy.foster@sky.com',
                     'izzy.foster@sky.com',
                     'Fizzy12095?',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '019',
                     'Harper Adams',
                     'harper.adams@sky.com',
                     'harper.adams@sky.com',
                     'HaAda198!#',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '024',
                     'Oliver King',
                     'oliver.king@sky.com',
                     'oliver.king@sky.com',
                     'OlKin723!@',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '023',
                     'Evelyn Lopez',
                     'evelyn.lopez@sky.com',
                     'evelyn.lopez@sky.com',
                     'EvLop456!*',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '022',
                     'Benjamin Wright',
                     'benjamin.wright@sky.com',
                     'benjamin.wright@sky.com',
                     'BeWri891!&',
                     'Senior Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '021',
                     'Mia Turner',
                     'mia.turner@sky.com',
                     'mia.turner@sky.com',
                     'MiTur624!%',
                     'Department Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '020',
                     'Elijah Scott',
                     'elijah.scott@sky.com',
                     'elijah.scott@sky.com',
                     'ElSco357!$',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '025',
                     'Lily Evans',
                     'lily.evans@sky.com',
                     'lily.evans@sky.com',
                     'LiEva258!%',
                     'Engineer',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '028',
                     'Zoe Mitchell',
                     'zoe.mitchell@sky.com',
                     'zoe.mitchell@sky.com',
                     'ZoMit474!*',
                     'Senior Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '027',
                     'Amelia Garcia',
                     'amelia.garcia@sky.com',
                     'amelia.garcia@sky.com',
                     'AmGar765!*',
                     'Department Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );

INSERT INTO User (
                     User_Id,
                     Name,
                     Email,
                     Username,
                     Password,
                     Role,
                     Admin_Id,
                     Session_Id,
                     Session_Duration,
                     Session_Date,
                     Badge_Id,
                     View_Profile,
                     Profile_Picture,
                     Login_Error_Times
                 )
                 VALUES (
                     '026',
                     'Henry Nguyen',
                     'henry.nguyen@sky.com',
                     'henry.nguyen@sky.com',
                     'HeNgu210!&',
                     'Team Leader',
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL,
                     NULL
                 );


-- Table: Vote
DROP TABLE IF EXISTS Vote;

CREATE TABLE IF NOT EXISTS Vote (
    Vote_Id         INTEGER PRIMARY KEY,
    Vote_Value      REAL,
    Progress_Status TEXT,
    Vote_Comment    TEXT,
    User_Id         TEXT    REFERENCES User (User_Id),
    Health_Card_Id  TEXT    REFERENCES Health_Card (Health_Card_Id) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
