SELECT 
	CATEGORY,
    PRICE AS MAX_PRICE,
    PRODUCT_NAME
FROM 
	FOOD_PRODUCT T1
WHERE 
	PRICE = (
        SELECT 
            MAX(PRICE) 
        FROM
            FOOD_PRODUCT
        WHERE 
            T1.CATEGORY = CATEGORY
	)
AND 
	category IN ('과자', '국', '김치', '식용유')
ORDER BY 
	MAX_PRICE DESC