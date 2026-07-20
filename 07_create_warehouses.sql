/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 07_create_warehouses.sql
Purpose : Create the Warehouses master table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Warehouses Master Table
-- Stores warehouse information used for inventory
-- management and order fulfillment.
-- ======================================================

CREATE TABLE Warehouses
(
    -- Auto-generated unique identifier
    Warehouse_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Warehouse code
    Warehouse_Code VARCHAR(10) NOT NULL UNIQUE,

    -- Warehouse name
    Warehouse_Name VARCHAR(100) NOT NULL,

    -- Warehouse city
    City VARCHAR(50) NOT NULL,

    -- Foreign Key to Regions table
    Region_ID INT NOT NULL,

    -- Warehouse address
    Address VARCHAR(200) NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Warehouses_Regions
        FOREIGN KEY (Region_ID)
        REFERENCES Regions(Region_ID)
);
GO