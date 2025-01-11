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
        print("Connexion établie à PostgreSQL")

        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        cursor.execute(create_table_query)
        print("Table 'users' créée ou déjà existante.")

        insert_data_query = """
        INSERT INTO users (name, age, email) 
        VALUES (%s, %s, %s);
        """
        users = [
            ("Alice", 25, "alice@supinfo.com"),
            ("Bob", 30, "bob@supinfo.com"),
            ("Charlie", 35, "charlie@supinfo.com"),
        ]
        for user in users:
            cursor.execute(insert_data_query, user)
        print("Données insérées dans la table 'users' avec succès.")

        connection.commit()

        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        print("Contenu de la table 'users' :")
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'accès à PostgreSQL", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("Connexion avec PostgreSQL fermée.")