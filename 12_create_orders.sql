/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 12_create_orders.sql
Purpose : Create the Orders table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Orders Table
-- Stores customer order headers.
-- Products are stored separately in Order_Items.
-- ======================================================

CREATE TABLE Orders
(
    -- Auto-generated unique identifier
    Order_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Business order number
    Order_Number VARCHAR(20) NOT NULL UNIQUE,

    -- Customer placing the order
    Customer_ID INT NOT NULL,

    -- Sales executive handling the order
    Employee_ID INT NOT NULL,

    -- Order date
    Order_Date DATE NOT NULL,

    -- Shipping method selected
    Shipping_Method_ID INT NOT NULL,

    -- Current order status
    Order_Status VARCHAR(20) NOT NULL,

    -- Total order amount
    Total_Amount DECIMAL(12,2) NOT NULL,

    -- Record creation date
    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Orders_Customers
        FOREIGN KEY (Customer_ID)
        REFERENCES Customers(Customer_ID),

    CONSTRAINT FK_Orders_Employees
        FOREIGN KEY (Employee_ID)
        REFERENCES Employees(Employee_ID),

    CONSTRAINT FK_Orders_ShippingMethods
        FOREIGN KEY (Shipping_Method_ID)
        REFERENCES Shipping_Methods(Shipping_Method_ID)
);
GO