# cs452_natural_languageSQL
Restaurant Database

The database that I decided to implement was a fairly simple database with restaurants, customers, and orders. The main use for a database like this would be to basically inquire about the various orders going through to understand how busy select restaurants were.

<img src="schema.png">

## Successful SQL Query
**Question**: Which restaurant is the least busiest?

**GPT SQL Response**:
```sql
SELECT r.name
FROM restaurants r
LEFT JOIN orders o ON r.restaurantid = o.restaurantid
GROUP BY r.restaurantid
ORDER BY COUNT(o.orderid) ASC
LIMIT 1;
```

**Friendly Response**: The least busy restaurant is Canes.

## Unsuccesful SQL Query
**Question**: Give me a list of cities that have more orders than McDonalds

**GPT SQL Response**:
```python
SELECT o.city
FROM orders o
JOIN restaurants r ON o.restaurantid = r.restaurantid
GROUP BY o.city
HAVING COUNT(o.orderid) > (
    SELECT COUNT(o2.orderid)
    FROM orders o2
    JOIN restaurants r2 ON o2.restaurantid = r2.restaurantid
    WHERE r2.name = 'McDonalds'
);
```

This query didn't even give me a response as there was an error in the request. Despite being given the layout of the tables and all the attributes within, the query requests the city name from the orders table even though that is not an included attribute.

The response that I received was an error response giving a suggestion as far as correcting the query:
```sql
  LINE 1: SELECT o.city
               ^
  HINT:  Perhaps you meant to reference the column "r.city".
```

## Multi-Shot
Originally I was feeding GPT just the basic information as far as the tables and attributes. I think due to the simplicity of the database that I created, this caused the multi and single shot tests to have about the same affect. I saw no signs of improvement and no signs of decline in the quality of the responses I received. From that I would assume the more complex I made my database, the more difference I would see in results

## Conclusion
I think the coolest part was testing the capabilities of GPT converting requests to SQL code. It was very effective in taking in the data and generating a query that matches the questions that I fed it. I utilized gpt 4 mini and it served it's purpose effectively and efficiently for my database.
