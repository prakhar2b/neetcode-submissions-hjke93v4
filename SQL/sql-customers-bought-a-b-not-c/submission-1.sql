-- Write your query below
select * from customers
where customer_id in (
    select distinct customer_id 
    from orders
    where product_name in ('A')
) and customer_id in (
    select distinct customer_id 
    from orders
    where product_name in ('B')
) and customer_id not in (
    select distinct customer_id 
    from orders
    where product_name in ('C')
)
order by customer_name