SELECT e.name
FROM Employee e
JOIN Employee sub ON sub.managerId = e.id
GROUP BY e.id, e.name
HAVING COUNT(sub.id) >= 5;