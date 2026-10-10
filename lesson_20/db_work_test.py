import psycopg2
import secrets_storage.db_secrets as s
from faker import Faker

### CONNECTION
connection = psycopg2.connect(
    dbname=s.DB_NAME,
    user=s.DB_USER,
    password=s.DB_PASSWORD,
    host=s.DB_HOST,
    port=s.DB_PORT
)

cursor = connection.cursor()

### SELECT

select_query = '''
SELECT *
FROM users_test;
'''
cursor.execute(select_query)
results = cursor.fetchall()
for user in results:
    print(user)

### INSERT

# faker = Faker('en_US')
# insert_query = f'''
# INSERT into users_test (name, description, phone)
# VALUES ('{faker.name()}', '{faker.word()}', '{faker.phone_number()}')
# RETURNING id;
# '''
# cursor.execute(insert_query)
# print(cursor.fetchall())
# connection.commit()

### UPDATE

# update_query = '''
# UPDATE users_test
# set description = 'UPDATED'
# where id between 5 and 10
# '''
# cursor.execute(update_query)
# connection.commit()

### DELETE

# delete_query = '''
# DELETE
# FROM users_test
# where id > 8
# RETURNING id
# '''
# cursor.execute(delete_query)
# print(cursor.fetchall())
# connection.commit()

### CLOSE CONNECTION
cursor.close()
connection.close()