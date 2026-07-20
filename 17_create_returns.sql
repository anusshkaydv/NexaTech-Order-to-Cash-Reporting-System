/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 17_create_returns.sql
Purpose : Create the Returns table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Returns Table
-- Stores products returned by customers.
-- ======================================================

CREATE TABLE Returns
(
    Return_ID INT IDENTITY(1,1) PRIMARY KEY,

    Return_Number VARCHAR(20) NOT NULL UNIQUE,

    Order_ID INT NOT NULL,

    Return_Date DATE NOT NULL,

    Return_Reason VARCHAR(200) NOT NULL,

    Return_Status VARCHAR(20) NOT NULL,

    Refund_Amount DECIMAL(12,2) NOT NULL DEFAULT 0,

    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Returns_Orders
        FOREIGN KEY (Order_ID)
        REFERENCES Orders(Order_ID)
);
GO