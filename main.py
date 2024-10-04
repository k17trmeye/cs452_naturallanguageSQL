import argparse
import openai
from openai import OpenAI
import os
from sqlalchemy import create_engine, text, Table, MetaData
from db import createNewTables, populateTables


def main(conn, conn_string, question):
    # Create tables, uncomment as needed
    createNewTables(conn)

    # Populate tables, uncomment as needed
    populateTables(conn, conn_string)

    # Load your API key from an environment variable
    openai.api_key = os.getenv('GPT_API_KEY')

    # Make a request to the OpenAI API
    print("\n\nQuestion = " + question + "\n")
    client = OpenAI()

    # Create API request with content
    request = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Given this SQL table data: restaurants(restaurantid, name, city, state, phone), " +
                    "customers(customerid, name, city, state, phone), " +
                    "and orders(orderid, customerid, restaurantid); " +
                    "Convert this text to mySQL code, only provide the code, no explanation: " + 
                    question
            }
        ]
    )

    # Extract the SQL query
    query = request.choices[0].message.content
    cleaned_sql = query.strip('```sql').strip('```').strip()
    print("GPT SQL code:")
    print(cleaned_sql)
    print("\n")
    
    # Execute the query GPT produced
    result = conn.execute(text(cleaned_sql))

    # Fetch all rows from the result
    rows = result.fetchall()

    # Convert the result rows to a string
    result_string = '\n'.join([str(row) for row in rows])
    print("SQL Query Response: ")
    print(result_string)
    print("\n")
    
    # Send a request to GPT to return a response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Provide an answer to this question (" +
                    question + ") " +
                    "given this return from a SQL query: " +
                    result_string + ". " +
                    "Don't explain the SQL return, give the answer in a sentence restating the question."
            }
        ]
    )

    # Extract the content of the API response and print
    responseGPT = response.choices[0].message.content
    print("GPT Response:")
    print(responseGPT)
    print("\n\n")


if __name__ == "__main__":
    # Parse the input to grab the query
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="natural language query")
    args = parser.parse_args()

    # Creating connection to timescale for db
    conn_string = os.getenv('TIMESCALE_LINK')
    engine = create_engine(conn_string)
    conn = engine.connect() 

    # Use the query with the connection
    main(conn, conn_string, question=args.query)