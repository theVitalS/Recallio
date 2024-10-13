from app.app import db, app
from database.sqlite_setup import *
from database.models import *

#rewrite_tables_from_models()

db_uri = 'sqlite:////home/vital/PycharmProjects/Lernotik/database/database.db'

# Create the engine
engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()
#session.close()

subj = Subject(name='Subject1')
session.add(subj)
session.commit()

session.close()