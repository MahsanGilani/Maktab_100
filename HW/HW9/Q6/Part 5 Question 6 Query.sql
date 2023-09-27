SELECT CONCAT(customer.first_name,'-',customer.last_name) AS fullname, customer.customer_id, count(rental.rental_id)
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
GROUP BY fullname, customer.customer_id
ORDER BY count(rental.rental_id) DESC
LIMIT 10
