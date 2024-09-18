CREATE DATABASE IF NOT EXISTS orlando_crimes;
USE orlando_crimes;

CREATE TABLE crimes(
	Case_Number varchar(50) primary key,
    Case_Date_Time datetime,
    Case_Location varchar(200),
    Case_Offense_Location_Type varchar(100),
    Case_Offense_Category varchar(100),
    Case_Offense_Type varchar(50),
    Case_Offense_Charge_Type varchar(100),
    Case_Disposition varchar(50),
    Status varchar(50),
    Location varchar(100),
    Orlando_Main_Street_Program_Area varchar(100),
    Orlando_Commissioner_Districts varchar(100),
    Orlando_Neighborhoods varchar(100)
);

