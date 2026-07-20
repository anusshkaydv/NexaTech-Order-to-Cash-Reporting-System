/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 03_Analytics_Product.sql
Purpose : Analytics Product Dimension View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Product
AS

SELECT

    p.Product_ID,
    p.Product_Code,
    p.Product_Name,

    p.Category_ID,
    pc.Category_Name,

    p.Brand,

    p.Cost_Price,
    p.Unit_Price,

    p.Is_Active

FROM Products p

LEFT JOIN Product_Categories pc
    ON p.Category_ID = pc.Category_ID;
GO