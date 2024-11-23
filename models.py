from sqlalchemy import create_engine, Column, BigInteger, Numeric, String, ForeignKey, Date, Integer, Boolean, CheckConstraint, Text, VARBINARY

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Таблица t_commands
class Command(Base):
    __tablename__ = "t_commands"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)


# Таблица t_technical_tasks
class TechnicalTask(Base):
    __tablename__ = "t_technical_tasks"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    description = Column(VARBINARY)


# Таблица t_customers
class Customer(Base):
    __tablename__ = "t_customers"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    law_face = Column(String(100), unique=True, nullable=False)
    law_addres = Column(String(250), nullable=False)
    director = Column(String(100), nullable=False)
    work_phone = Column(String(20), nullable=False)


# Таблица t_orders
class Order(Base):
    __tablename__ = "t_orders"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_customer = Column(BigInteger, ForeignKey("t_customers.id"), nullable=False)
    accept_date = Column(Date, nullable=False)
    deadline = Column(Date, nullable=False)
    id_command = Column(BigInteger, ForeignKey("t_commands.id"), nullable=False)
    payment = Column(Numeric, nullable=False)
    id_tt = Column(BigInteger, ForeignKey("t_technical_tasks.id"), nullable=False)
    CheckConstraint("payment > 0")


# Таблица t_employees
class Employee(Base):
    __tablename__ = "t_employees"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    job = Column(String(50), nullable=False)
    date_of_employment = Column(Date, nullable=False)
    grade = Column(String(30), nullable=False)
    id_command = Column(BigInteger, ForeignKey("t_commands.id"), nullable=False)


# Таблица t_expenses_items
class ExpensesItem(Base):
    __tablename__ = "t_expenses_items"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(300), nullable=False)


# Таблица t_expenses
class Expense(Base):
    __tablename__ = "t_expenses"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    cost = Column(Numeric, nullable=False)
    expense_id = Column(BigInteger, ForeignKey("t_expenses_items.id"), nullable=False)
    note = Column(String(300))


# Таблица t_profit_items
class ProfitItem(Base):
    __tablename__ = "t_profit_items"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(300), nullable=False)


# Таблица t_profits
class Profit(Base):
    __tablename__ = "t_profits"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    cost = Column(Numeric, nullable=False)
    profit_id = Column(BigInteger, ForeignKey("t_profit_items.id"), nullable=False)
    note = Column(String(300), nullable=False)
    order_id = Column(BigInteger, ForeignKey("t_orders.id"), nullable=False)


# Таблица t_applicants
class Applicant(Base):
    __tablename__ = "t_applicants"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    job = Column(String(50), nullable=False)


# Таблица t_testing_result
class TestingResult(Base):
    __tablename__ = "t_testing_result"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    applicant_id = Column(BigInteger, ForeignKey("t_applicants.id"), nullable=False)
    correct_answers = Column(Integer, nullable=False)
    incorrect_answers = Column(Integer, nullable=False)
    is_passed = Column(Boolean)


# Таблица t_testing_questions
class TestingQuestion(Base):
    __tablename__ = "t_testing_questions"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    question_number = Column(BigInteger, nullable=False)
    job = Column(String(50), nullable=False)
    question_text = Column(String(300), nullable=False)
    question_type = Column(String(100), nullable=False)


# Таблица t_answers
class Answer(Base):
    __tablename__ = "t_answers"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    question_number = Column(BigInteger, nullable=False)
    question_text = Column(String(300), nullable=False)
    is_correct = Column(Boolean)
    question_id = Column(BigInteger, ForeignKey("t_testing_questions.id"), nullable=False)


# Таблица t_interview
class Interview(Base):
    __tablename__ = "t_interview"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    applicant_id = Column(BigInteger, ForeignKey("t_applicants.id"), nullable=False)
    interview_date = Column(Date, nullable=False)
    interview_time = Column(Date, nullable=False)
    is_passed = Column(Boolean, nullable=False)


# Таблица t_files
class File(Base):
    __tablename__ = "t_files"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    file_name = Column(String(100), nullable=False)
    b_data = Column(VARBINARY)
    order_id = Column(BigInteger, ForeignKey("t_orders.id"), nullable=False)
    life_time = Column(Date, nullable=False)


l_models = [Command, TechnicalTask, Customer, Order, Employee,
            ExpensesItem, Expense, ProfitItem, Profit, Applicant, 
            TestingResult, TestingQuestion, Answer, Interview, File
]
