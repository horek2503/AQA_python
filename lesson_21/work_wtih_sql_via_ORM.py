import secrets_storage.db_secrets as s
import random
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey, select, or_, and_
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from faker import Faker

faker = Faker(locale='en_US')

# Base class from ORM
Base = declarative_base()


# CREATE OUR DATA MODEL

class Category(Base):
    __tablename__ = 'categories_orm'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    isavailable = Column(Boolean,default=True)
    isdeleted = Column(Boolean, default=False)
    # RELATIONSHIP
    products = relationship("Product", back_populates='category')

class Product(Base):
    __tablename__ = 'products_orm'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    categoryId = Column(Integer, ForeignKey('categories_orm.id'), nullable=False, default = 1)
    isAvailable = Column(Boolean, default=True)

    def __str__(self):
        return f"Product with id={self.id}, name={self.name}, price = {self.price}"

    # RELATIONSHIP
    category = relationship("Category", back_populates='products')

DB_URL = f'postgresql://{s.DB_USER}:{s.DB_PASSWORD}@{s.DB_HOST}:{s.DB_PORT}/{s.DB_NAME}'
# print(DB_URL)
engine = create_engine(DB_URL)

### START SESSION WITH DB
Session = sessionmaker(bind=engine)
session = Session()

### CREATE TABLES
Base.metadata.create_all(engine)

### INSERT RECORDS
### Category 1
new_category1 = Category(id=1,name='Base', description='Basic category')
check_if_category1_exists = session.query(Category).filter_by(name='Base').first()
if not check_if_category1_exists:
    session.add(new_category1)

### Category 2
new_category2 = Category(id=2,name='Advanced', description='Advanced category')
check_if_category2_exists = session.query(Category).filter_by(name='Advanced').first()
if not check_if_category2_exists:
    session.add(new_category2)

### One product
# new_product = Product(name=faker.word(), price=random.randint(100, 10000) / 100, description='Created via ORM', categoryId=2)
# session.add(new_product)

### One product with relationship
related_category = session.query(Category).filter_by(name="Advanced").first()
rel_product = Product(name='VIP', price = 100.11, category=related_category)
session.add(rel_product)

### Several products
# products = []
# for _ in range(5):
#     products.append(Product(name=faker.word(), price=random.randint(1,100), description='Created via ORM'))
# session.add_all(products)

### UPDATE RECORDS
# product_to_change = session.query(Product).filter_by(name='ORM_item_1',id=1).first()
# product_to_change.price = 111


# ### DELETE RECORDS
# product_to_delete = session.query(Product).filter_by(name='ORM_item_1', id=1).first()
# session.delete(product_to_delete)

### ADVANCED FILTER + SORTING
select_query = select(Product).where(
    and_(Product.id > 10, Product.id < 15)
).order_by(Product.price.desc())
result = session.execute(select_query)

### print(result.fetchall()) # --> list of tuples
products = [k[0] for k in result.fetchall()]

### print option1 - unpacking + __str__
print(*products, sep='\n')

### print option2 - object + access to fields
# for product in products:
#     print(f"Product with id {product.id} costs {product.price}")


### COMMITING CHANGES AND CLOSING SESSION
session.commit()
