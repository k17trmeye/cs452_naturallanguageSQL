from sqlalchemy import create_engine, text, Table, MetaData
from tables import restaurants_table, customers_table, orders_table
from data import restaurants, customers, orders


def createNewTables(conn):
    drop_table = "DROP TABLE IF EXISTS restaurants CASCADE"
    conn.execute(text(drop_table))
    conn.commit()

    drop_table = "DROP TABLE IF EXISTS customers CASCADE"
    conn.execute(text(drop_table))
    conn.commit()

    drop_table = "DROP TABLE IF EXISTS orders CASCADE"
    conn.execute(text(drop_table))
    conn.commit()

    conn.execute(text(restaurants_table))
    conn.commit()

    conn.execute(text(customers_table))
    conn.commit()

    conn.execute(text(orders_table))
    conn.commit()


def populateTables(conn, conn_string):
    metadata = MetaData()
    engine = create_engine(conn_string)
    restaurants_table = Table("restaurants", metadata, autoload_with=engine)
    conn.execute(restaurants_table.insert(), restaurants)


    metadata = MetaData()
    engine = create_engine(conn_string)
    customers_table = Table("customers", metadata, autoload_with=engine)
    conn.execute(customers_table.insert(), customers)


    metadata = MetaData()
    engine = create_engine(conn_string)
    orders_table = Table("orders", metadata, autoload_with=engine)
    conn.execute(orders_table.insert(), orders)

