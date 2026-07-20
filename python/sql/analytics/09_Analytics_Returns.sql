/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 09_Analytics_Returns.sql
Purpose : Returns Reporting View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Returns
AS

SELECT

    r.Return_ID,
    r.Return_Number,
    r.Return_Date,

    r.Return_Status,
    r.Return_Reason,
    r.Refund_Amount,

    o.Order_Number,

    c.Company_Name

FROM Returns r

LEFT JOIN Orders o
ON r.Order_ID = o.Order_ID

LEFT JOIN Customers c
ON o.Customer_ID = c.Customer_ID;
GO
