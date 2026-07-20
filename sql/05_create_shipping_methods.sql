/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 05_create_shipping_methods.sql
Purpose : Create the Shipping Methods master table
Author  : Anushka Yadav
Created : 10-Jul-2026
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Shipping_Methods Master Table
-- Stores the available delivery methods offered by
-- NexaTech for customer orders.
-- ======================================================

CREATE TABLE Shipping_Methods
(
    -- Auto-generated unique identifier
    Shipping_Method_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Shipping method name
    Shipping_Method_Name VARCHAR(50) NOT NULL UNIQUE,

    -- Estimated delivery duration in days
    Estimated_Delivery_Days INT NOT NULL,

    -- Additional description
    Description VARCHAR(150) NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE()
);
GO
/*
USE NexaTechERP;
GO

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'Shipping_Methods';
GO

SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Shipping_Methods';
*/
