from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Create an engine to connect to an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Define metadata
metadata = MetaData()

# Define a table
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

# Create all tables in the metadata
metadata.create_all(engine)

# Create a connection
conn = engine.connect()

# Insert a row into the table
conn.execute(users.insert(), [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
])

# Select all rows from the table
result = conn.execute(users.select())

# Fetch and print the results
for row in result:
    print(row)

# Close the connection
conn.close()

