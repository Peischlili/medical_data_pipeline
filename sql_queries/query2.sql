WITH ventes_type (client_id, product_type, ventes)
AS (
	SELECT CP.client_id, PN.product_type, SUM(CP.ventes) 
	FROM (
		SELECT client_id, prod_id, SUM(prod_price * prod_qty) AS ventes 
		FROM TRANSCATION
		WHERE year(date) = 2020
		GROUP BY client_id, prod_id	
		) AS CP,
	JOIN PRODUIT_NOMENCLATURE AS PN
	ON CP.prod_id = PN.product_id
	GROUP BY PN.product_type
)
SELECT V1.client_id, V1.ventes AS ventes_meuble, V2.ventes AS ventes_deco
FROM ventes_type AS V1, ventes_type AS V2
WHERE V1.client_id = V2.client_id
	AND V1.product_type in ('MEUBLE')
	AND V2.product_type in ('DECO')

