/* 1 */
select product.Name as 'Product name', cat.Name as 'Category name'
from Production.Product as product
join Production.ProductSubcategory as subcat
on product.ProductSubcategoryID = subcat.ProductSubcategoryID
join Production.ProductCategory as cat
on cat.ProductCategoryID = subcat.ProductCategoryID
where product.Color = 'Red' and product.ListPrice >= 100
/* 2 */
select one.Name
from Production.ProductSubcategory as one,
Production.ProductSubcategory as two
where one.Name = two.Name and one.ProductCategoryID != two.ProductCategoryID
/* 3 */
select cat.ProductCategoryID, count(*) as 'Qty'
from Production.Product as product
join Production.ProductSubcategory as subcat
on product.ProductSubcategoryID = subcat.ProductSubcategoryID
join Production.ProductCategory as cat
on subcat.ProductCategoryID = cat.ProductCategoryID
group by cat.ProductCategoryID
/* 4 */
select subcat.Name, count(*)
from Production.ProductSubcategory as subcat,
Production.Product as product
where product.ProductSubcategoryID = subcat.ProductSubcategoryID
group by subcat.ProductSubcategoryID, subcat.Name
/* 5 */
select top 3 subcat.Name, count(*)
from Production.ProductSubcategory as subcat,
Production.Product as product
where product.ProductSubcategoryID = subcat.ProductSubcategoryID
group by subcat.ProductSubcategoryID, subcat.Name
order by count(*) desc
/* 6 */
select subcat.Name, max(product.ListPrice)
from Production.ProductSubcategory as subcat,
Production.Product as product
where product.ProductSubcategoryID = subcat.ProductSubcategoryID
and product.Color = 'Red'
group by subcat.ProductSubcategoryID, subcat.Name
/* 7 */
select vendor.Name, count(*)
from Purchasing.Vendor as vendor
join Purchasing.ProductVendor as pvendor
on vendor.BusinessEntityID = pvendor.BusinessEntityID
join Production.Product as product
on product.ProductID = pvendor.ProductID
group by vendor.Name
/* 8 */
select product.Name
from Purchasing.Vendor as vendor
join Purchasing.ProductVendor as pvendor
on vendor.BusinessEntityID = pvendor.BusinessEntityID
join Production.Product as product
on product.ProductID = pvendor.ProductID
group by product.Name
having count(product.ProductID) > 1
/* 9 */
select top 1 product.Name
from Production.Product as product
join Sales.SalesOrderDetail as sales
on product.ProductID = sales.ProductID
group by product.Name
order by sum(sales.OrderQty) desc
/* 10 */
select top 3 cat.Name /* 3 самые "продаваемые категории" */
from Production.Product as product
join Production.ProductSubcategory as subcat
on product.ProductSubcategoryID = subcat.ProductSubcategoryID
join Production.ProductCategory as cat
on subcat.ProductCategoryID = cat.ProductCategoryID
join Sales.SalesOrderDetail as sales
on sales.ProductID = product.ProductID
group by cat.Name
order by sum(sales.OrderQty) desc
/* 11 */
select cat.name, count(distinct subcat.name) as 'Amount of Subcategories', count(distinct product.ProductNumber) as 'Amount of products'
from Production.Product as product 
join Production.ProductSubcategory as subcat
on product .ProductSubcategoryID = subcat.ProductSubcategoryID
join Production.ProductCategory as cat
on subcat.ProductCategoryID = cat.ProductCategoryID
group by cat.ProductCategoryID, subcat.ProductSubcategoryID
/* 12 */
select vendor.CreditRating, count(product.ProductID)
from Purchasing.Vendor as vendor
join Purchasing.ProductVendor as pvendor
on vendor.BusinessEntityID = pvendor.BusinessEntityID
join Production.Product as product
on product.ProductID = pvendor.ProductID
group by vendor.CreditRating