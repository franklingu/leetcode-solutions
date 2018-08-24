/**
 * The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
 *
 * +----+-------+--------+-----------+
 * | Id | Name  | Salary | ManagerId |
 * +----+-------+--------+-----------+
 * | 1  | Joe   | 70000  | 3         |
 * | 2  | Henry | 80000  | 4         |
 * | 3  | Sam   | 60000  | NULL      |
 * | 4  | Max   | 90000  | NULL      |
 * +----+-------+--------+-----------+
 * Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
 *
 * +----------+
 * | Employee |
 * +----------+
 * | Joe      |
 * +----------+
 */
select e.name as Employee from Employee as e join Employee as e2 on e.ManagerId = e2.Id where e.Salary > e2.Salary;
