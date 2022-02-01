SELECT date, SUM(prod_price * prod_qty * 1000) AS ventes
FROM TRANSACTION
WHERE YEAR(date) = 2019
GROUP BY date
ORDER BY date ASC
