SELECT title,rental_duration,ROUND(AVG(rental_rate),3) AS Average_rental_rate
FROM film
GROUP BY title, rental_duration
ORDER BY title