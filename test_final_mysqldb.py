# Import SQLAlchemy modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL database connection parameters
MYSQL_USER = 'your_mysql_user'
MYSQL_PASSWORD = 'your_mysql_password'
MYSQL_HOST = 'localhost'
MYSQL_DB = 'your_mysql_database'

# Define SQLAlchemy engine
engine = create_engine(f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}")

# Define declarative base
Base = declarative_base()

# Define User class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add some data
session.add_all([
    User(name='Alice', age=30),
    User(name='Bob', age=25)
])

# Commit the session
session.commit()

# Query the data
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

# Close the session
session.close()

