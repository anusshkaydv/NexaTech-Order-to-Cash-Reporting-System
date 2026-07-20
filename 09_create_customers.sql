/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 09_create_customers.sql
Purpose : Create the Customers master table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Customers Master Table
-- Stores customer companies that purchase products
-- from NexaTech.
-- ======================================================

CREATE TABLE Customers
(
    -- Auto-generated unique identifier
    Customer_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Business customer code
    Customer_Code VARCHAR(10) NOT NULL UNIQUE,

    -- Company name
    Company_Name VARCHAR(100) NOT NULL,

    -- Primary contact person
    Contact_Person VARCHAR(100) NOT NULL,

    -- Official email
    Email VARCHAR(100) NOT NULL UNIQUE,

    -- Contact number
    Phone VARCHAR(15) NOT NULL,

    -- Customer city
    City VARCHAR(50) NOT NULL,

    -- Region reference
    Region_ID INT NOT NULL,

    -- Customer payment terms
    Payment_Term_ID INT NOT NULL,

    -- Assigned account manager
    Account_Manager_ID INT NOT NULL,

    -- Active (1) / Inactive (0)
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Customers_Regions
        FOREIGN KEY (Region_ID)
        REFERENCES Regions(Region_ID),

    CONSTRAINT FK_Customers_PaymentTerms
        FOREIGN KEY (Payment_Term_ID)
        REFERENCES Payment_Terms(Payment_Term_ID),

    CONSTRAINT FK_Customers_Employees
        FOREIGN KEY (Account_Manager_ID)
        REFERENCES Employees(Employee_ID)
);
GO