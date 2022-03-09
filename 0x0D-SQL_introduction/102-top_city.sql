--  displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT TOP 3 * FROM temperature 
GROUP BY city 
ORDER BY temperature DESC;
