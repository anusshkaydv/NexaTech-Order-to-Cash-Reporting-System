/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 13_create_order_items.sql
Purpose : Create the Order_Items table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Order_Items Table
-- Stores individual products within each order.
-- ======================================================

CREATE TABLE Order_Items
(
    -- Auto-generated unique identifier
    Order_Item_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Parent order
    Order_ID INT NOT NULL,

    -- Product ordered
    Product_ID INT NOT NULL,

    -- Warehouse fulfilling the order
    Warehouse_ID INT NOT NULL,

    -- Quantity ordered
    Quantity INT NOT NULL,

    -- Selling price at the time of order
    Unit_Price DECIMAL(10,2) NOT NULL,

    -- Discount applied
    Discount_Amount DECIMAL(10,2) NOT NULL DEFAULT 0,

    -- Total amount for this line
    Line_Total DECIMAL(12,2) NOT NULL,

    CONSTRAINT FK_OrderItems_Orders
        FOREIGN KEY (Order_ID)
        REFERENCES Orders(Order_ID),

    CONSTRAINT FK_OrderItems_Products
        FOREIGN KEY (Product_ID)
        REFERENCES Products(Product_ID),

    CONSTRAINT FK_OrderItems_Warehouses
        FOREIGN KEY (Warehouse_ID)
        REFERENCES Warehouses(Warehouse_ID)
);
GO

