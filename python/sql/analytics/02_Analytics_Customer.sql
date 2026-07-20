/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 02_Analytics_Customer.sql
Purpose : Analytics Customer Dimension View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Customer
AS

SELECT

    c.Customer_ID,
    c.Customer_Code,
    c.Company_Name,
    c.Contact_Person,
    c.Email,
    c.Phone,
    c.City,

    r.Region_Name,

    pt.Payment_Term_Name,

    c.Is_Active

FROM Customers c

LEFT JOIN Regions r
    ON c.Region_ID = r.Region_ID

LEFT JOIN Payment_Terms pt
    ON c.Payment_Term_ID = pt.Payment_Term_ID;
GO
