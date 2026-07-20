/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 04_create_payment_terms.sql
Purpose : Create the Payment Terms master table
Author  : Anushka Yadav
Created : 10-Jul-2026
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Payment_Terms Master Table
-- Stores standard payment terms offered to customers.
-- Referenced by Customers and Invoices.
-- ======================================================

CREATE TABLE Payment_Terms
(
    -- Auto-generated unique identifier
    Payment_Term_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Payment term name (Net 30, Net 45, etc.)
    Payment_Term_Name VARCHAR(30) NOT NULL UNIQUE,

    -- Number of credit days
    Credit_Days INT NOT NULL,

    -- Additional business description
    Description VARCHAR(100) NULL,

    -- 1 = Active, 0 = Inactive
    Is_Active BIT NOT NULL DEFAULT 1,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE()
);
GO
/*
USE NexaTechERP;
GO

SELECT *
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'Payment_Terms';
GO
*/