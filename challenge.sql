-- Query 1
SELECT
    name
FROM
    employee as e
        INNER JOIN employee as m ON e.managerId = m.id
WHERE
    e.salary > m.salary;

-- Query 2
WITH aux (
    SELECT
        s.product_id
        s.year,
        s.quantity,
        s.price,
        ROW_NUMBER() OVER (PARTITION BY s.product_id ORDER BY s.year ASC) as rank
    FROM
        Sales as s
);

SELECT
    aux.product_id,
    aux.year as first_year,
    aux.quantity,
    aux.price
FROM
    aux
where
    rank = 1;
