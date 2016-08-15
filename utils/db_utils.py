import json
import psycopg2
import datetime
from urllib.parse import urlparse

"""
Utility functions to perform a variety of actions on the postgreSQL database.

To use, replace the code in main() with the desired actions.

"""

with open('../keys.json') as key_data:
    key_dict = json.load(key_data)
    
    database_url = key_dict['app']['database_url']
    parsed_url = urlparse(database_url)
    
    
def main():
    """
    EXAMPLE CODE:
    
    create_table('example_queue', 'filepath text', 'timestamp timestamp')
    create_table('example_recent_queue', 'filepath text', 'timestamp timestamp')
    create_table('example_request_sent', 'id text', 'screen_name text', 'timestamp timestamp')
    drop_table('example_queue')
    clear_table('example_queue')
    insert_row('example_queue', 'filepath', 'example_string')
    delete_row('example_queue', 'filepath', 'example_string')
    """
    
    pass
    
    
# Helper function for creating a connection to the database
def create_connection():
    return psycopg2.connect(database=parsed_url.path[1:],
                            user=parsed_url.username,
                            password=parsed_url.password,
                            host=parsed_url.hostname,
                            port=parsed_url.port)
                            

def create_table(table_name, *columns):
    """
    Create a table with the specified name and columns

    *columns is a variable length argument list which should contain at least one string
    with column information. At minimum, each string should have the name of the column
    followed by the data type of the column.

    For example:

    create_table("user", "id bigint", "name text")

    will create a table named "user" with two fields called id and name, with the
    data types bigint and text respectively.

    The user can specify constraints within the column string. Examples:

    "id bigint UNIQUE"
    "name text PRIMARY KEY"
    "lastname text NOT NULL"

    Refer to PostgreSQL documentation for a list of accepted data types and constraints.

    It is the caller's responsibility to ensure that the column strings are formatted correctly!
    """
    conn = create_connection()
    cur = conn.cursor()

    if len(columns) == 0:
        print("At least one column string required. Table not created.")
        return

    column_string = ""
    for column in columns:
        column_string += column
        column_string += ","

    column_string = column_string[:-1]

    cur.execute("CREATE TABLE {} ({});".format(table_name, column_string))

    conn.commit()
    cur.close()
    conn.close()
    
    
# Drops the specified table from the database
def drop_table(table_name):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("DROP TABLE {}".format(table_name))

    conn.commit()
    cur.close()
    conn.close()
    
    
# Delete all rows in the table, resulting in a valid, but empty table
def clear_table(table_name):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM {}".format(table_name))

    conn.commit()
    cur.close()
    conn.close()

    
# Insert a single row in the table
# ONLY CALL THIS IF THE TABLE HAS A timestamp FIELD
def insert_row(table_name, field, id):
    conn = create_connection()
    cur = conn.cursor()
    
    timestamp = str(datetime.datetime.now())
    
    cur.execute("INSERT INTO {0} ({1}, timestamp) VALUES ('{2}', '{3}')".format(table_name, field, id, timestamp))
    
    conn.commit()
    cur.close()
    conn.close()
    
    
# Delete a single row in the table
def delete_row(table_name, field, id):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM {0} WHERE {1} = ('{2}')".format(table_name, field, id))

    conn.commit()
    cur.close()
    conn.close()
    
    
# Get all rows and columns of a table
def get_table_contents(table_name):
    conn = create_connection()
    cur = conn.cursor()

    entries = []

    cur.execute("SELECT * FROM {}".format(table_name))

    for row in cur.fetchall():
        entries.append(row)

    conn.commit()
    cur.close()
    conn.close()

    return entries
        
        
if __name__ == "__main__":
    main()