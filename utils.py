from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from datetime import datetime

from admin import *
from models import *

str_to_date = datetime.strptime
date_to_str = datetime.strftime


def get_error_by_traceback(v_in_traceback: str) -> str:
    "Возвращает ошибку, ключевую часть из traceback"
    #print(f"{v_in_traceback=}")
    clear_traceback = ""
    traceback = v_in_traceback.split('\n')
    for line in traceback:
        status = False
        if "file" in line:
            status = True
            continue
        if status:
            continue
        clear_traceback += line
    return clear_traceback


def get_data_from_table(v_in_model: Model) -> list[dict]:
    l_tuples = list()
    stmt = select(v_in_model).order_by(v_in_model.id)
    with Session(bind=DB_ENGINE) as session:
        tuples = session.execute(stmt)
        tuples = tuples.scalars().all()
        for tpl in tuples:
            dict_tpl = {column.name: getattr(tpl, column.name) for column in tpl.__table__.columns}
            l_tuples.append(dict_tpl)
    return l_tuples


def save_to_t_customer(dict_data: dict):
    incoming_customer = Customer(
            id = int(dict_data.get("id")),
            law_face = str(dict_data.get("law_face")),
            law_addres = str(dict_data.get("law_addres")),
            director = str(dict_data.get("director")),
            work_phone = str(dict_data.get("work_phone"))
        )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_customer)
        session.commit()


# Функция для сохранения в таблицу t_commands
def save_to_t_commands(dict_data: dict):
    incoming_command = Command(
        id = int(dict_data.get("id")),
        name=str(dict_data.get("name"))
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_command)
        session.commit()


# Функция для сохранения в таблицу t_technical_tasks
def save_to_t_technical_tasks(dict_data: dict):
    incoming_technical_task = TechnicalTask(
        id = int(dict_data.get("id")),
        description=dict_data.get("description")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_technical_task)
        session.commit()


# Функция для сохранения в таблицу t_orders
def save_to_t_orders(dict_data: dict):
    incoming_order = Order(
        id = int(dict_data.get("id")),
        id_customer=int(dict_data.get("id_customer")),
        accept_date=str_to_date(dict_data.get("accept_date"), "%Y-%m-%d"),
        deadline=dict_data.get("deadline"),
        id_command=int(dict_data.get("id_command")),
        payment=float(dict_data.get("payment")),
        id_tt=int(dict_data.get("id_tt"))
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_order)
        session.commit()


# Функция для сохранения в таблицу t_employees
def save_to_t_employees(dict_data: dict):
    incoming_employee = Employee(
        id = int(dict_data.get("id")),
        surname=dict_data.get("surname"),
        name=dict_data.get("name"),
        last_name=dict_data.get("last_name"),
        position=dict_data.get("position"),
        job=dict_data.get("job"),
        date_of_employment=str_to_date(dict_data.get("date_of_employment"), "%Y-%m-%d"),
        grade=dict_data.get("grade"),
        id_command=int(dict_data.get("id_command"))
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_employee)
        session.commit()


# Функция для сохранения в таблицу t_expenses_items
def save_to_t_expenses_items(dict_data: dict):
    incoming_expenses_item = ExpensesItem(
        id = int(dict_data.get("id")),
        name=dict_data.get("name"),
        description=dict_data.get("description")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_expenses_item)
        session.commit()


# Функция для сохранения в таблицу t_expenses
def save_to_t_expenses(dict_data: dict):
    incoming_expense = Expense(
        id = int(dict_data.get("id")),
        date=str_to_date(dict_data.get("date"), "%Y-%m-%d" ),
        cost=float(dict_data.get("cost")),
        expense_id=int(dict_data.get("expense_id")),
        note=dict_data.get("note")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_expense)
        session.commit()


# Функция для сохранения в таблицу t_profit_items
def save_to_t_profit_items(dict_data: dict):
    incoming_profit_item = ProfitItem(
        id = int(dict_data.get("id")),
        name=dict_data.get("name"),
        description=dict_data.get("description")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_profit_item)
        session.commit()


# Функция для сохранения в таблицу t_profits
def save_to_t_profits(dict_data: dict):
    incoming_profit = Profit(
        id = int(dict_data.get("id")),
        date=str_to_date(dict_data.get("date"), "%Y-%m-%d"),
        cost=float(dict_data.get("cost")),
        profit_id=int(dict_data.get("profit_id")),
        note=dict_data.get("note"),
        order_id=int(dict_data.get("order_id"))
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_profit)
        session.commit()


# Функция для сохранения в таблицу t_applicants
def save_to_t_applicants(dict_data: dict):
    incoming_applicant = Applicant(
        id = int(dict_data.get("id")),
        surname=dict_data.get("surname"),
        name=dict_data.get("name"),
        last_name=dict_data.get("last_name"),
        job=dict_data.get("job")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_applicant)
        session.commit()


# Функция для сохранения в таблицу t_testing_result
def save_to_t_testing_result(dict_data: dict):
    incoming_testing_result = TestingResult(
        id = int(dict_data.get("id")),
        applicant_id=int(dict_data.get("applicant_id")),
        correct_answers=int(dict_data.get("correct_answers")),
        incorrect_answers=int(dict_data.get("incorrect_answers")),
        is_passed=True if dict_data.get("is_passed") == "True" else False
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_testing_result)
        session.commit()


# Функция для сохранения в таблицу t_testing_questions
def save_to_t_testing_questions(dict_data: dict):
    incoming_testing_question = TestingQuestion(
        id = int(dict_data.get("id")),
        question_number=int(dict_data.get("question_number")),
        job=dict_data.get("job"),
        question_text=dict_data.get("question_text"),
        question_type=dict_data.get("question_type")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_testing_question)
        session.commit()


# Функция для сохранения в таблицу t_answers
def save_to_t_answers(dict_data: dict):
    incoming_answer = Answer(
        id = int(dict_data.get("id")),
        question_number=int(dict_data.get("question_number")),
        question_text=dict_data.get("question_text"),
        is_correct= True if dict_data.get("is_correct") == "True" else False,
        question_id=int(dict_data.get("question_id"))
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_answer)
        session.commit()


# Функция для сохранения в таблицу t_interview
def save_to_t_interview(dict_data: dict):
    incoming_interview = Interview(
        id = int(dict_data.get("id")),
        applicant_id=int(dict_data.get("applicant_id")),
        interview_date=str_to_date(dict_data.get("interview_date"), "%Y-%m-%d"),
        interview_time=str_to_date(dict_data.get("interview_time"), "%H:%M"),
        is_passed= True if dict_data.get("is_passed") == "True" else False
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_interview)
        session.commit()


def save_to_t_files(dict_data: dict):
    incoming_file = File(
        id = int(dict_data.get("id")),
        file_name=dict_data.get("file_name"),
        b_data=dict_data.get("b_data"),
        order_id=int(dict_data.get("order_id")),
        life_time=str_to_date(dict_data.get("life_time"), "%Y-%m-%d")
    )
    with Session(DB_ENGINE) as session:
        session.merge(incoming_file)
        session.commit()


dict_save_functions = {
    Customer : save_to_t_customer, Command : save_to_t_commands,
    TechnicalTask : save_to_t_technical_tasks, Order: save_to_t_orders, 
    ExpensesItem: save_to_t_expenses_items, Expense: save_to_t_expenses,
    ProfitItem: save_to_t_profit_items, Profit: save_to_t_profits,
    Applicant: save_to_t_applicants, TestingResult: save_to_t_testing_result,
    TestingQuestion: save_to_t_testing_questions, Answer: save_to_t_answers,
    Interview: save_to_t_interview, File : save_to_t_files, Employee: save_to_t_employees,
}

