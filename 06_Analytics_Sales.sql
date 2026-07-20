/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 06_Analytics_Sales.sql
Purpose : Sales Fact View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Sales
AS

SELECT

    o.Order_ID,
    o.Order_Number,
    o.Order_Date,

    oi.Order_Item_ID,

    c.Customer_ID,
    c.Company_Name,

    p.Product_ID,
    p.Product_Name,
    p.Brand,
    pc.Category_Name,

    e.Employee_ID,
    CONCAT(e.First_Name,' ',e.Last_Name) AS Employee_Name,

    w.Warehouse_ID,
    w.Warehouse_Name,

    oi.Quantity,
    oi.Unit_Price,
    oi.Discount_Amount,
    oi.Line_Total,

    o.Total_Amount,
    o.Order_Status

FROM Orders o

INNER JOIN Order_Items oi
ON o.Order_ID = oi.Order_ID

LEFT JOIN Customers c
ON o.Customer_ID = c.Customer_ID

LEFT JOIN Products p
ON oi.Product_ID = p.Product_ID

LEFT JOIN Product_Categories pc
ON p.Category_ID = pc.Category_ID

LEFT JOIN Employees e
ON o.Employee_ID = e.Employee_ID

LEFT JOIN Warehouses w
ON oi.Warehouse_ID = w.Warehouse_ID;
GO