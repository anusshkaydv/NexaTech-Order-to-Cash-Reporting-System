/*
=========================================================
Project : NexaTech Order-to-Cash Reporting System
File    : 04_Analytics_Employee.sql
Purpose : Analytics Employee Dimension View
Author  : Anushka Yadav
=========================================================
*/

CREATE OR ALTER VIEW Analytics_Employee
AS

SELECT

    e.Employee_ID,
    e.Employee_Code,

    CONCAT(e.First_Name, ' ', e.Last_Name) AS Employee_Name,

    e.Department,
    e.Designation,

    e.Email,
    e.Phone,

    e.Warehouse_ID,
    w.Warehouse_Name,

    e.Hire_Date,

    e.Is_Active

FROM Employees e

LEFT JOIN Warehouses w
    ON e.Warehouse_ID = w.Warehouse_ID;
GO