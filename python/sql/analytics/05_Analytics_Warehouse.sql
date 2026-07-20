/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 05_Analytics_Warehouse.sql
Purpose : Analytics Warehouse Dimension View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Warehouse
AS

SELECT

    w.Warehouse_ID,
    w.Warehouse_Code,
    w.Warehouse_Name,

    w.City,

    w.Region_ID,
    r.Region_Name,

    w.Is_Active,

    w.Created_Date

FROM Warehouses w

LEFT JOIN Regions r
    ON w.Region_ID = r.Region_ID;
GO
