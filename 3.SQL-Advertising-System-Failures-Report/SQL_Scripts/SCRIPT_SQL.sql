use mydb;

SELECT CONCAT(first_name, " ", last_name) AS "customer", COUNT(e.status) AS failures
FROM events e 
INNER JOIN campaigns camp 
ON e.campaign_id = camp.id
INNER JOIN customers cust
ON cust.id = camp.customers_id
WHERE e.status = "failure"
GROUP BY camp.customers_id
HAVING COUNT(e.status) > 3; # It consults the rows defined on the group by
