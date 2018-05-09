from peewee import SqliteDatabase, Model, CharField, FloatField, IntegerField

from test_multiple_files import parse_products

db = SqliteDatabase('revenue.db')

class Product(Model):
    name = CharField()
    price = FloatField()
    quantity_sold = IntegerField()

    class Meta:
        database = db

db.connect()

#db.create_tables([Product])
product_rows = parse_products()

for product_row in product_rows:
    product_row = Product(name=product_row[0], price=product_row[1], quantity_sold=product_row[2]) #Product(product.name, product.price, product.quantity_sold)
    product_row.save()

db.close()
