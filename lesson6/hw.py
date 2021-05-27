import sqlite3


class Product:

    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table products (id integer, name text, price text);')
        except sqlite3.OperationalError:
            print("Таблица уже существует!")
        self.connection.commit()

    def insert(self, id, name, price):
        cursor = self.connection.cursor()
        cursor.execute("insert into products values (?, ?, ?)", (id, name, price))
        self.connection.commit()
        print("Row inserted")

    def update(self, id, name=None, price=None):
        cursor = self.connection.cursor()
        cursor.execute(f"update products set name = 'Milk' where id = {id}")
        self.connection.commit()
        print("Row updated")

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"delete from products where id = {id}")
        self.connection.commit()
        print("Row deleted")


product = Product()
product.create_table()
product.insert(1, 'Banana', 100)
product.insert(2, 'Milk', 50)

product.delete(1)
