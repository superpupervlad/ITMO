 
/*
Найти для каждого чека его номер, количество категорий и подкатегорий 
 */
with z (orderid, subcat, c)
as (
	SELECT sod.SalesOrderID, 
	DENSE_RANK() OVER (PARTITION BY SalesOrderID ORDER BY sc.ProductSubcategoryID) as subcat,
	DENSE_RANK() OVER (PARTITION BY SalesOrderID ORDER BY cat.ProductCategoryID) as c
	FROM Sales.SalesOrderDetail sod 
	join Production.Product p
	on p.ProductID = sod.ProductID 
	join Production.ProductSubcategory sc
	on p.ProductSubcategoryID = sc.ProductSubcategoryID
	join Production.ProductCategory cat
	on sc.ProductCategoryID = cat.ProductCategoryID 
)

SELECT distinct orderid, MAX(subcat) OVER (PARTITION BY orderid) as 'SubCategory amount', MAX(c) OVER (PARTITION BY orderid) as 'Category amount'
FROM z



/* 1 */
/* Найти долю продаж каждого продукта (цена продукта * количество продукта),
на каждый чек, в денежном выражении. */
/*
SELECT SalesOrderID, ProductID, 
	OrderQty*UnitPrice 
/   ------------------ <- дробная черта
	sum(OrderQty*UnitPrice) OVER (PARTITION BY SalesOrderID) as 'Part in total cost'
FROM Sales.SalesOrderDetail sod */


/* 2 */
/*  Вывести на экран список продуктов, их стоимость, а также разницу между
стоимостью этого продукта и стоимостью самого дешевого продукта в той же
подкатегории, к которой относится продукт. */
/*
SELECT p.ProductID, p.ListPrice, p.ListPrice - MIN(p.ListPrice) 
	OVER (PARTITION BY p.ProductSubcategoryID)
FROM Production.Product p */
