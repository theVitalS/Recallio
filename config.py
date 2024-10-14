import os

project_location = os.path.dirname(os.path.abspath(__file__))

db_relative_path = 'backend/database/'
db_name = 'dummy_base'
db_path = project_location + '/' + db_relative_path + db_name
DATABASE_URL = f"sqlite:///{db_path}.db"