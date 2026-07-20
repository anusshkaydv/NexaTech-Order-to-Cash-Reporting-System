/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 08_Analytics_Payments.sql
Purpose : Payments Reporting View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Payments
AS

SELECT

    p.Payment_ID,
    p.Payment_Number,
    p.Payment_Date,

    p.Payment_Method,
    p.Payment_Status,
    p.Payment_Amount,

    i.Invoice_Number,
    i.Invoice_Date,

    o.Order_Number,

    c.Company_Name

FROM Payments p

LEFT JOIN Invoices i
ON p.Invoice_ID = i.Invoice_ID

LEFT JOIN Orders o
ON i.Order_ID = o.Order_ID

LEFT JOIN Customers c
ON o.Customer_ID = c.Customer_ID;
GO