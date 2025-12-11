import mysql.connector


def create_database():
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host= 'localhost',
            user='username',
            password='your_password'
        )
        cursor = connection.cursor()


        # Create a new database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully")


    except mysql.connector.Error as err:
        print(f"Error connecting to DB: {err}")


    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
