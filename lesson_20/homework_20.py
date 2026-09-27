import psycopg2
import secrets.db_secrets as s


def execute_db_query(query: str, do_commit: bool = False, return_data: bool = False):
    connection = False
    try:
        connection = psycopg2.connect(
            dbname=s.DB_NAME,
            user=s.DB_USER,
            password=s.DB_PASSWORD,
            host=s.DB_HOST,
            port=s.DB_PORT
        )
        cursor = connection.cursor()

    except Exception as e:
        print(f"Cannot connect to DB. Exception: {e}")

    else:
        cursor.execute(query)
        if return_data:
            return cursor.fetchall()

    finally:
        if connection:
            if do_commit:
                connection.commit()
            cursor.close()
            connection.close()


def create_retail_tables_if_not_exist():
    create_query = '''
    create table if not exists public.categories (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) not NULL,
	description VARCHAR(100),
	isAvailable BOOLEAN NOT NULL DEFAULT true,
	isDeleted BOOLEAN NOT NULL DEFAULT false
	);
	
    create table if not exists public.products (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) UNIQUE not NULL,
	description VARCHAR(100),
	price float,
	categoryId integer references categories (id),
	isAvailable BOOLEAN NOT NULL DEFAULT true,
	isDeleted BOOLEAN NOT NULL DEFAULT false
	);

    '''
    execute_db_query(create_query, do_commit=True)


def populate_retail_data_if_not_exists():
    insert_query = '''
    insert into categories
    (id, name, description, isAvailable)
    values
    (1, 'Food', 'General category for food', true),
    (2, 'Drinks', 'All drinks', true),
    (3, 'Personal care products', '', true)
    on conflict do nothing;
    
    insert into products
    (name, description, price, categoryId, isAvailable)
    values
    ('Pizza 4 cheeses', 'TOP product', 249.99, 1, true),
    ('Chicken roll XXL', 'Discount: -50% on Fridays', 190, 1, true),
    ('Farmer tomatoes', 'Delivery each SU', 78.90, 1, false),
    ('Pepsi 2L no sugar', 'Pepsi cola', 57.90, 2, true),
    ('Captain Morgan 0.7L', '18+ only', 399.99, 2, true),
    ('Morshynska 1.5L', '', 37.20, 2, true)
    on conflict do nothing;
    '''
    execute_db_query(insert_query, do_commit=True)


def get_available_food_and_drinks_from_db():
    select_query = '''
    select p.name "Product", p.price, p.description, c.name " Category"
    from products p
    join categories c 
    on p.categoryid = c.id 
    where c.name in ('Food', 'Drinks')
    and p.isavailable = true
    '''

    return execute_db_query(select_query, return_data=True)


create_retail_tables_if_not_exist()
populate_retail_data_if_not_exists()
products = get_available_food_and_drinks_from_db()

for product in products:
    print(product)
