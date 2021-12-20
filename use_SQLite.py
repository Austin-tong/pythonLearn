from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector

"""
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()
"""

conn = mysql.connector.connect(user='root', passwd='root', auth_plugin='mysql_native_password')
cursor = conn.cursor()
