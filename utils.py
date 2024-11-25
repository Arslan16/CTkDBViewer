from sqlalchemy import select
from sqlalchemy.orm import Session
from customtkinter import CTkEntry

from admin import *
from models import *

def get_data_from_table(v_in_model) -> list[dict]:
    l_tuples = list()
    stmt = select(v_in_model)
    with Session(bind=DB_ENGINE) as session:
        tuples = session.execute(stmt)
        tuples = tuples.scalars().all()
        for tpl in tuples:
            dict_tpl = {column.name: getattr(tpl, column.name) for column in tpl.__table__.columns}
            l_tuples.append(dict_tpl)
    return l_tuples