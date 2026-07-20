/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 11_create_inventory.sql
Purpose : Create the Inventory table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Inventory Table
-- Stores product stock available in each warehouse.
-- ======================================================

CREATE TABLE Inventory
(
    -- Auto-generated unique identifier
    Inventory_ID INT IDENTITY(1,1) PRIMARY KEY,

    -- Warehouse reference
    Warehouse_ID INT NOT NULL,

    -- Product reference
    Product_ID INT NOT NULL,

    -- Current available quantity
    Quantity_On_Hand INT NOT NULL,

    -- Minimum quantity before reorder
    Reorder_Level INT NOT NULL,

    -- Last inventory update
    Last_Updated DATETIME NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Inventory_Warehouse
        FOREIGN KEY (Warehouse_ID)
        REFERENCES Warehouses(Warehouse_ID),

    CONSTRAINT FK_Inventory_Product
        FOREIGN KEY (Product_ID)
        REFERENCES Products(Product_ID),

    -- Prevent duplicate warehouse-product combinations
    CONSTRAINT UQ_Inventory_Warehouse_Product
        UNIQUE (Warehouse_ID, Product_ID)
);
GO
