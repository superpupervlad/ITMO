/* 1 
select Color, count(*)
from Production.Product
where ListPrice >= 30
group by Color
*/

/* 2
select Color, min(ListPrice)
from Production.Product
group by Color
having min(ListPrice) > 100
*/

/* 3
select ProductSubcategoryID, count(*)
from Production.Product
where ProductSubcategoryID is not NULL
group by ProductSubcategoryID
*/

/* 4
select ProductID, sum(OrderQty)
from Sales.SalesOrderDetail
group by ProductID
*/

/* 5
select ProductID, sum(OrderQty)
from Sales.SalesOrderDetail
group by ProductID
having sum(OrderQty) > 5
*/

/* 6
select CustomerID, convert(date, OrderDate) /*Берем только дату, без времени*/
from Sales.SalesOrderHeader
group by convert(date, OrderDate), CustomerID
having count(*) > 1
*/



/* 7 
select SalesOrderID
from Sales.SalesOrderDetail
group by SalesOrderID
having count(*) > 3
*/

/* 8 
select ProductID
from Sales.SalesOrderDetail
group by ProductID
having count(*) > 3
*/

/* 9
select ProductID
from Sales.SalesOrderDetail
group by ProductID
having count(*) IN (3, 5)
*/

/* 10 
select ProductSubcategoryID
from Production.Product
group by ProductSubcategoryID
having count(*) > 10
*/

/* 11 
SELECT ProductID
from Sales.SalesOrderDetail
where OrderQty = 1
group by ProductID
*/

/* 12 
select top 1 SalesOrderID
from Sales.SalesOrderDetail
group by SalesOrderID
order by count(*) desc
*/

/* 13 
select top 1 SalesOrderId, sum(OrderQty*UnitPrice) as s
from Sales.SalesOrderDetail
group by SalesOrderId
order by s desc
*/

/* 14
select ProductSubcategoryID, count(*)
from Production.Product
where ProductSubcategoryID is not NULL and Color is not NULL
group by ProductSubcategoryID
*/

/* 15
select Color
from Production.Product
group by Color
order by count(*) desc
*/

/* 16
select ProductID, count(*)
from Sales.SalesOrderDetail
group by ProductID
having min(OrderQty) > 1 and count(*) > 2
*/