/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 16_create_payments.sql
Purpose : Create the Payments table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Payments Table
-- Stores payments received against customer invoices.
-- ======================================================

CREATE TABLE Payments
(
    Payment_ID INT IDENTITY(1,1) PRIMARY KEY,

    Payment_Number VARCHAR(20) NOT NULL UNIQUE,

    Invoice_ID INT NOT NULL,

    Payment_Date DATE NOT NULL,

    Payment_Method VARCHAR(30) NOT NULL,

    Payment_Amount DECIMAL(12,2) NOT NULL,

    Payment_Status VARCHAR(20) NOT NULL,

    Transaction_Reference VARCHAR(100) NULL,

    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Payments_Invoices
        FOREIGN KEY (Invoice_ID)
        REFERENCES Invoices(Invoice_ID)
);
GO
