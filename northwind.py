import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

expensive_items = """
select * from Product
order by  UnitPrice desc
limit 10
"""


avg_hire_age = """
select AVG(floor((JULIANDAY(HireDate) - JULIANDAY(BirthDate))/365)) from Employee
"""

avg_age_by_city = """
select City, AVG(floor((JULIANDAY(HireDate) - JULIANDAY(BirthDate))/365)) from Employee
group by City
"""

ten_most_expensive = """
select ProductName, CompanyName from (select * from Product
                order by  UnitPrice desc
                limit 10) as top_ten
left join Supplier
on Supplier.Id = top_ten.SupplierId
"""

largest_category = """
select CategoryName, total_prod from (select CategoryId,
                       count(distinct ProductName) as total_prod
                from Product
                group by CategoryId
                order by total_prod desc
                limit 1) as largest_cat
left join Category
on Category.Id = largest_cat.CategoryId
"""

most_territories = """
select * from (select EmployeeId,
                       count(distinct TerritoryId) as total_territories
                from EmployeeTerritory
                group by EmployeeId
                order by total_territories desc
                limit 1) as emp_total_terr
left join Employee
on Employee.Id = emp_total_terr.EmployeeId
"""

conn.close()