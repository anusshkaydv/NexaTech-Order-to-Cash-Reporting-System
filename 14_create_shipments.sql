/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 14_create_shipments.sql
Purpose : Create the Shipments table
Author  : Anushka Yadav
=========================================================
*/

USE NexaTechERP;
GO

-- ======================================================
-- Create Shipments Table
-- Stores shipment details for customer orders.
-- ======================================================

CREATE TABLE Shipments
(
    Shipment_ID INT IDENTITY(1,1) PRIMARY KEY,

    Shipment_Number VARCHAR(20) NOT NULL UNIQUE,

    Order_ID INT NOT NULL,

    Warehouse_ID INT NOT NULL,

    Shipment_Date DATE NOT NULL,

    Expected_Delivery_Date DATE NOT NULL,

    Actual_Delivery_Date DATE NULL,

    Shipment_Status VARCHAR(30) NOT NULL,

    Tracking_Number VARCHAR(50) NULL,

    Created_Date DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Shipments_Orders
        FOREIGN KEY (Order_ID)
        REFERENCES Orders(Order_ID),

    CONSTRAINT FK_Shipments_Warehouses
        FOREIGN KEY (Warehouse_ID)
        REFERENCES Warehouses(Warehouse_ID)
);
GO