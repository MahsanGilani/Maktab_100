SELECT title, rental_duration, AVG (rental_rate)
FROM film
GROUP BY title
ORDER BY title
--همش ارور میده اینو :((