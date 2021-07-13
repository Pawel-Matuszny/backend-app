from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import settings

engine = create_engine(
    '{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
    **settings.POSTGRESQL
    ), echo=True
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
