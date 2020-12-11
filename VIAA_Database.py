import sqlite3
from sqlite3 import Error


def create_connection(VIAA_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(VIAA_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    



#Create URL and Keyword tables
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"dbVIAA.db"

    sql_create_url_table = """ CREATE TABLE IF NOT EXISTS url (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        url text NOT NULL,
                                        website_name text NOT NULL,
                                        keyword text NOT NULL
                                    ); """

    sql_create_keyword_table = """CREATE TABLE IF NOT EXISTS keyword (
                                    id integer PRIMARY KEY,
                                    user_id text NOT NULL,
                                    keyword text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create url table
        create_table(conn, sql_create_url_table)

        # create keyword table
        create_table(conn, sql_create_keyword_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
