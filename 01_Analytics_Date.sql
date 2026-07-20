/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 01_Analytics_Date.sql
Purpose : Analytics Date Dimension View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Date
AS

SELECT DISTINCT

    CAST(Order_Date AS DATE) AS Date_Key,

    YEAR(Order_Date) AS Report_Year,

    MONTH(Order_Date) AS Month_Number,

    DATENAME(MONTH, Order_Date) AS Month_Name,

    DATEPART(QUARTER, Order_Date) AS Quarter_Number,

    DAY(Order_Date) AS Day_Number,

    DATENAME(WEEKDAY, Order_Date) AS Day_Name

FROM Orders;
GO