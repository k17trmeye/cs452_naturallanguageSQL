restaurants_table = """
        CREATE TABLE restaurants (
            restaurantid INT NOT NULL UNIQUE PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            city VARCHAR(20) NOT NULL,
            state VARCHAR(20) NOT NULL,
            phone VARCHAR(15)
        )
    """

customers_table = """
        CREATE TABLE customers (
            customerid INT NOT NULL UNIQUE PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            city VARCHAR(20) NOT NULL,
            state VARCHAR(20) NOT NULL,
            phone VARCHAR(15)
        )
    """

orders_table = """
        CREATE TABLE orders (
            orderid INT NOT NULL UNIQUE PRIMARY KEY,
            customerid INT NOT NULL,
            restaurantid  INT NOT NULL,
            FOREIGN KEY (customerid) REFERENCES customers(customerid),
            FOREIGN KEY (restaurantid) REFERENCES restaurants(restaurantid)
        )
    """