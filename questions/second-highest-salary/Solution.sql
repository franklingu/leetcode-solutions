# Write a SQL query to get the second highest salary from the Employee table.
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+

# For example, given the above Employee table, the second highest salary is 200.
# If there is no second highest salary, then the query should return null.

# Write your MySQL query statement below
SELECT (SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1,1) AS SecondHighestSalary;