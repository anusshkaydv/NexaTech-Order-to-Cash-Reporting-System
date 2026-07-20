/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 18_create_discounts.sql
Purpose : Create the Discounts table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Discounts Table
-- Stores discounts applied to customer orders.
-- ======================================================

CREATE TABLE Discounts
(
    Discount_ID INT IDENTITY(1,1) PRIMARY KEY,

    Order_ID INT NOT NULL,

    Discount_Type VARCHAR(20) NOT NULL,

    Discount_Value DECIMAL(10,2) NOT NULL,

    Discount_Reason VARCHAR(200) NULL,

    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Discounts_Orders
        FOREIGN KEY (Order_ID)
        REFERENCES Orders(Order_ID)
);
GO