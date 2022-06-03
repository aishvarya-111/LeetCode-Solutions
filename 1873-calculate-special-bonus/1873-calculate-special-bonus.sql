# Write your MySQL query statement below
select employee_id , salary * (employee_id%2) * (name NOT LIKE "M%") as bonus
from Employees