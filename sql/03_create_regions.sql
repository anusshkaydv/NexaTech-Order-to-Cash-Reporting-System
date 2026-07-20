/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 03_create_regions.sql
Purpose : Create the Regions master table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- Create Regions master table
CREATE TABLE Regions
(
    -- Auto-generated unique region identifier
    Region_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Short code (NR, SR, WR, etc.)
    Region_Code VARCHAR(5) NOT NULL UNIQUE,

    -- Region name
    -- Stores the business region used for sales, logistics,
    -- and financial reporting.
    Region_Name VARCHAR(30) NOT NULL UNIQUE,

    -- Regional headquarters city
    Headquarters_City VARCHAR(50) NOT NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE()
);
GO

USE NexaTechERP;
GO

SELECT *
FROM INFORMATION_SCHEMA.TABLES;
GO
