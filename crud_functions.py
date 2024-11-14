import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    cursor.execute("DELETE FROM Products")
    connection.commit()
    connection.close()

def add_product(title, description, price):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))

    connection.commit()
    connection.close()

def get_all_products(limit=4):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products LIMIT ?", (limit,))
    products = cursor.fetchall()
    connection.close()
    return products
