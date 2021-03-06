from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os

env_username = os.environ['DB_USERNAME']
env_password = os.environ['DB_PASSWORD']
env_host = os.environ['DB_HOST']
env_db_name = os.environ['DB_NAME']
env_port = os.environ['DB_PORT']

POSTGRESQL = {
    'engine': 'postgresql+psycopg2',
    'username': env_username,
    'password': env_password,
    'host': env_host,
  	'port': env_port,
    'db_name': env_db_name,
}

sql_url ='{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(**POSTGRESQL) 
engine = create_engine(sql_url, echo=True
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
