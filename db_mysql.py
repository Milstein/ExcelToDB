
from peewee import MySQLDatabase, Model, CharField, FloatField, IntegerField

from test_multiple_files import parse_products

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('my_app', user='root', password='')

class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = mysql_db

class Product(BaseModel):
    name = CharField()
    price = FloatField()
    quantity_sold = IntegerField()

Product.create_table()

product_rows = parse_products()

for product_row in product_rows:
    product = Product(name=product_row[0], price=product_row[1], quantity_sold=product_row[2]) #Product(product.name, product.price, product.quantity_sold)
    product.save()


#product.save()

for product in Product.filter(name="Laptop"):
    print(product.name)

