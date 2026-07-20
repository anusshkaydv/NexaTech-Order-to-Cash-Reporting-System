/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 06_create_product_categories.sql
Purpose : Create the Product Categories master table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Product_Categories Master Table
-- Stores all product categories sold by NexaTech.
-- Referenced by the Products table.
-- ======================================================

CREATE TABLE Product_Categories
(
    -- Auto-generated unique identifier
    Category_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Product category name
    Category_Name VARCHAR(50) NOT NULL UNIQUE,

    -- Description of the category
    Description VARCHAR(150) NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE()
);
GO

