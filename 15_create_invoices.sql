/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 15_create_invoices.sql
Purpose : Create the Invoices table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Invoices Table
-- Stores invoices generated for customer orders.
-- ======================================================

CREATE TABLE Invoices
(
    Invoice_ID INT IDENTITY(1,1) PRIMARY KEY,

    Invoice_Number VARCHAR(20) NOT NULL UNIQUE,

    Order_ID INT NOT NULL,

    Invoice_Date DATE NOT NULL,

    Due_Date DATE NOT NULL,

    Invoice_Amount DECIMAL(12,2) NOT NULL,

    Invoice_Status VARCHAR(20) NOT NULL,

    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Invoices_Orders
        FOREIGN KEY (Order_ID)
        REFERENCES Orders(Order_ID)
);
GO