from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

from admin import *
from models import *

str_to_date = datetime.strptime
date_to_str = datetime.strftime


def get_error_by_traceback(v_in_traceback: str) -> str:
    "Возвращает ошибку, ключевую часть из traceback"
    print(f"{v_in_traceback=}")
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


def save_to_t_customer(dict_data: dict):
    try:
        incoming_customer = Customer(
            law_face = str(dict_data.get("law_face")),
            law_addres = str(dict_data.get("law_addres")),
            director = str(dict_data.get("director")),
            work_phone = str(dict_data.get("work_phone"))
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_customer)
            session.commit()
    except Exception as e:
        err = get_error_by_traceback(str(e))
        print(err)


# Функция для сохранения в таблицу t_commands
def save_to_t_commands(dict_data: dict):
    try:
        incoming_command = Command(
            name=str(dict_data.get("name"))
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_command)
            session.commit()
        print("Данные успешно сохранены в таблицу t_commands")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_commands: {str(e)}")


# Функция для сохранения в таблицу t_technical_tasks
def save_to_t_technical_tasks(dict_data: dict):
    try:
        incoming_technical_task = TechnicalTask(
            description=dict_data.get("description")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_technical_task)
            session.commit()
        print("Данные успешно сохранены в таблицу t_technical_tasks")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_technical_tasks: {str(e)}")


# Функция для сохранения в таблицу t_orders
def save_to_t_orders(dict_data: dict):
    try:
        incoming_order = Order(
            id_customer=int(dict_data.get("id_customer")),
            accept_date=datetimedict_data.get("accept_date"),
            deadline=dict_data.get("deadline"),
            id_command=int(dict_data.get("id_command")),
            payment=float(dict_data.get("payment")),
            id_tt=int(dict_data.get("id_tt"))
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_order)
            session.commit()
        print("Данные успешно сохранены в таблицу t_orders")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_orders: {str(e)}")


# Функция для сохранения в таблицу t_employees
def save_to_t_employees(dict_data: dict):
    try:
        incoming_employee = Employee(
            surname=dict_data.get("surname"),
            name=dict_data.get("name"),
            last_name=dict_data.get("last_name"),
            position=dict_data.get("position"),
            job=dict_data.get("job"),
            date_of_employment=dict_data.get("date_of_employment"),
            grade=dict_data.get("grade"),
            id_command=dict_data.get("id_command")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_employee)
            session.commit()
        print("Данные успешно сохранены в таблицу t_employees")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_employees: {str(e)}")


# Функция для сохранения в таблицу t_expenses_items
def save_to_t_expenses_items(dict_data: dict):
    try:
        incoming_expenses_item = ExpensesItem(
            name=dict_data.get("name"),
            description=dict_data.get("description")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_expenses_item)
            session.commit()
        print("Данные успешно сохранены в таблицу t_expenses_items")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_expenses_items: {str(e)}")


# Функция для сохранения в таблицу t_expenses
def save_to_t_expenses(dict_data: dict):
    try:
        incoming_expense = Expense(
            date=dict_data.get("date"),
            cost=dict_data.get("cost"),
            expense_id=dict_data.get("expense_id"),
            note=dict_data.get("note")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_expense)
            session.commit()
        print("Данные успешно сохранены в таблицу t_expenses")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_expenses: {str(e)}")


# Функция для сохранения в таблицу t_profit_items
def save_to_t_profit_items(dict_data: dict):
    try:
        incoming_profit_item = ProfitItem(
            name=dict_data.get("name"),
            description=dict_data.get("description")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_profit_item)
            session.commit()
        print("Данные успешно сохранены в таблицу t_profit_items")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_profit_items: {str(e)}")


# Функция для сохранения в таблицу t_profits
def save_to_t_profits(dict_data: dict):
    try:
        incoming_profit = Profit(
            date=dict_data.get("date"),
            cost=dict_data.get("cost"),
            profit_id=dict_data.get("profit_id"),
            note=dict_data.get("note"),
            order_id=dict_data.get("order_id")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_profit)
            session.commit()
        print("Данные успешно сохранены в таблицу t_profits")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_profits: {str(e)}")


# Функция для сохранения в таблицу t_applicants
def save_to_t_applicants(dict_data: dict):
    try:
        incoming_applicant = Applicant(
            surname=dict_data.get("surname"),
            name=dict_data.get("name"),
            last_name=dict_data.get("last_name"),
            job=dict_data.get("job")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_applicant)
            session.commit()
        print("Данные успешно сохранены в таблицу t_applicants")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_applicants: {str(e)}")


# Функция для сохранения в таблицу t_testing_result
def save_to_t_testing_result(dict_data: dict):
    try:
        incoming_testing_result = TestingResult(
            applicant_id=dict_data.get("applicant_id"),
            correct_answers=dict_data.get("correct_answers"),
            incorrect_answers=dict_data.get("incorrect_answers"),
            is_passed=dict_data.get("is_passed")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_testing_result)
            session.commit()
        print("Данные успешно сохранены в таблицу t_testing_result")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_testing_result: {str(e)}")


# Функция для сохранения в таблицу t_testing_questions
def save_to_t_testing_questions(dict_data: dict):
    try:
        incoming_testing_question = TestingQuestion(
            question_number=dict_data.get("question_number"),
            job=dict_data.get("job"),
            question_text=dict_data.get("question_text"),
            question_type=dict_data.get("question_type")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_testing_question)
            session.commit()
        print("Данные успешно сохранены в таблицу t_testing_questions")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_testing_questions: {str(e)}")


# Функция для сохранения в таблицу t_answers
def save_to_t_answers(dict_data: dict):
    try:
        incoming_answer = Answer(
            question_number=dict_data.get("question_number"),
            question_text=dict_data.get("question_text"),
            is_correct=dict_data.get("is_correct"),
            question_id=dict_data.get("question_id")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_answer)
            session.commit()
        print("Данные успешно сохранены в таблицу t_answers")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_answers: {str(e)}")


# Функция для сохранения в таблицу t_interview
def save_to_t_interview(dict_data: dict):
    try:
        incoming_interview = Interview(
            applicant_id=dict_data.get("applicant_id"),
            interview_date=dict_data.get("interview_date"),
            interview_time=dict_data.get("interview_time"),
            is_passed=dict_data.get("is_passed")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_interview)
            session.commit()
        print("Данные успешно сохранены в таблицу t_interview")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_interview: {e}")


def save_to_t_files(dict_data: dict):
    try:
        incoming_file = File(
            file_name=dict_data.get("file_name"),
            b_data=dict_data.get("b_data"),
            order_id=dict_data.get("order_id"),
            life_time=dict_data.get("life_time")
        )
        with Session(DB_ENGINE) as session:
            session.merge(incoming_file)
            session.commit()
        print("Данные успешно сохранены в таблицу t_interview")
    except Exception as e:
        print(f"Ошибка при сохранении данных в t_interview: {e}")


dict_save_functions = {
    Customer : save_to_t_customer, Command : save_to_t_commands,
    TechnicalTask : save_to_t_technical_tasks, Order: save_to_t_orders, 
    ExpensesItem: save_to_t_expenses_items, Expense: save_to_t_expenses,
    ProfitItem: save_to_t_profit_items, Profit: save_to_t_profits,
    Applicant: save_to_t_applicants, TestingResult: save_to_t_testing_result,
    TestingQuestion: save_to_t_testing_questions, Answer: save_to_t_answers,
    Interview: save_to_t_interview, File : save_to_t_files, Employee: save_to_t_employees,
}
