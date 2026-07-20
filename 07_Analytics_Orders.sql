/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 07_Analytics_Orders.sql
Purpose : Orders Reporting View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Orders
AS

SELECT

    o.Order_ID,
    o.Order_Number,
    o.Order_Date,
    o.Order_Status,
    o.Total_Amount,

    c.Company_Name,

    CONCAT(e.First_Name,' ',e.Last_Name) AS Sales_Representative,

    sm.Shipping_Method_Name

FROM Orders o

LEFT JOIN Customers c
ON o.Customer_ID = c.Customer_ID

LEFT JOIN Employees e
ON o.Employee_ID = e.Employee_ID

LEFT JOIN Shipping_Methods sm
ON o.Shipping_Method_ID = sm.Shipping_Method_ID;
GO