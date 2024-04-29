import MySQLdb
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# MySQL connection parameters
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_HOST = 'localhost'
MYSQL_DB = 'testdb'

# Test MySQLdb connection
try:
    conn = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_DB)
    print("MySQLdb connection successful!")
    conn.close()
except Exception as e:
    print("MySQLdb connection failed:", e)

# Test SQLAlchemy connection
try:
    # SQLAlchemy engine
    engine = create_engine(f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}')
    
    # Create a simple table
    metadata = MetaData()
    test_table = Table('test', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
    )
    metadata.create_all(engine)
    
    # Insert a row
    with engine.connect() as conn:
        conn.execute(test_table.insert(), [{'name': 'Test Name'}])
    
    print("SQLAlchemy connection and table creation successful!")
except Exception as e:
    print("SQLAlchemy connection failed:", e)

