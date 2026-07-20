/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 10_create_products.sql
Purpose : Create the Products master table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Products Master Table
-- Stores all products sold by NexaTech.
-- ======================================================

CREATE TABLE Products
(
    -- Auto-generated unique identifier
    Product_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Business product code
    Product_Code VARCHAR(15) NOT NULL UNIQUE,

    -- Product name
    Product_Name VARCHAR(100) NOT NULL,

    -- Product category
    Category_ID INT NOT NULL,

    -- Selling price
    Unit_Price DECIMAL(10,2) NOT NULL,

    -- Cost price
    Cost_Price DECIMAL(10,2) NOT NULL,

    -- Brand name
    Brand VARCHAR(50) NOT NULL,

    -- Warranty period in months
    Warranty_Months INT NOT NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Products_ProductCategories
        FOREIGN KEY (Category_ID)
        REFERENCES Product_Categories(Category_ID)
);
GO
