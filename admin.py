from sqlalchemy import create_engine

DB_URL = 'mssql+pymssql://Арслан:@DESKTOP-TGHDOEF/t_scos?charset=utf8'
DB_ENGINE = create_engine(DB_URL)
BASE_BACKGROUND_COLOR = "#2b2b2b"
