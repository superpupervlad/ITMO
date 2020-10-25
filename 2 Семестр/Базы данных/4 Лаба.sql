/* 1 */
/*SELECT p.Name 
FROM Production.Product p 
where p.ProductID = 
(SELECT top 1 sod.ProductID 
FROM Sales.SalesOrderDetail sod
GROUP BY sod.ProductID 
order by SUM(sod.OrderQty) DESC)*/
/* 2 */
/*SELECT soh.CustomerID, soh.SalesOrderID
FROM Sales.SalesOrderHeader soh
where soh.SalesOrderID = 
(SELECT top 1 sod.SalesOrderID
FROM Sales.SalesOrderDetail sod 
group by sod.SalesOrderID
ORDER BY SUM(sod.OrderQty * sod.UnitPrice) DESC )*/
/* 3 */
SELECT p.Name 
FROM Production.Product p
where p.ProductID in(
SELECT p.ProductID 
FROM Sales.SalesOrderDetail sod
where sod.SalesOrderDetailID = 
(SELECT soh.SalesOrderID 
FROM Sales.SalesOrderHeader soh))