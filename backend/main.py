from app.app import app
from database.sqlite_setup import create_tables_from_models, rewrite_tables_from_models

if __name__ == '__main__':
    #create_tables_from_models()
    #rewrite_tables_from_models()

    app.run()
