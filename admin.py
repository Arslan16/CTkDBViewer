from sqlalchemy import create_engine

DB_URL = "mssql+pyodbc://arslan:211621@localhost/t_scos?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
DB_ENGINE = create_engine(DB_URL)
BASE_BACKGROUND_COLOR = "#2b2b2b"
