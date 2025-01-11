import psycopg2

if __name__ == '__main__':
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sup1nf0", 
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You connected to PostgreSQL", record)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("PostgreSQL connection is closed")