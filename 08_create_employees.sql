/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 08_create_employees.sql
Purpose : Create the Employees master table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Employees Master Table
-- Stores employee information across all departments.
-- Some employees may be assigned to a warehouse.
-- ======================================================

CREATE TABLE Employees
(
    -- Auto-generated unique identifier
    Employee_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Business employee code
    Employee_Code VARCHAR(10) NOT NULL UNIQUE,

    -- Employee first name
    First_Name VARCHAR(50) NOT NULL,

    -- Employee last name
    Last_Name VARCHAR(50) NOT NULL,

    -- Official email address
    Email VARCHAR(100) NOT NULL UNIQUE,

    -- Contact number
    Phone VARCHAR(15) NOT NULL,

    -- Department name
    Department VARCHAR(50) NOT NULL,

    -- Employee designation
    Designation VARCHAR(50) NOT NULL,

    -- Assigned warehouse (if applicable)
    Warehouse_ID INT NULL,

    -- Date of joining
    Hire_Date DATE NOT NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Employees_Warehouses
        FOREIGN KEY (Warehouse_ID)
        REFERENCES Warehouses(Warehouse_ID)
);
GO

