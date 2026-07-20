/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 10_Analytics_Inventory.sql
Purpose : Inventory Reporting View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Inventory
AS

SELECT

    i.Inventory_ID,

    p.Product_ID,
    p.Product_Name,
    p.Brand,

    pc.Category_Name,

    w.Warehouse_Name,

    i.Quantity_On_Hand,
    i.Reorder_Level,

    i.Last_Updated

FROM Inventory i

LEFT JOIN Products p
ON i.Product_ID = p.Product_ID

LEFT JOIN Product_Categories pc
ON p.Category_ID = pc.Category_ID

LEFT JOIN Warehouses w
ON i.Warehouse_ID = w.Warehouse_ID;
GO