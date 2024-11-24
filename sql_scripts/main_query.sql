USE t_scos;
-- 1 
BEGIN TRANSACTION;

IF OBJECT_ID('dbo.t_commands') IS NULL
BEGIN
	CREATE TABLE t_commands(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_commands_id PRIMARY KEY ,
		name VARCHAR(50) NOT NULL CONSTRAINT t_commands_name UNIQUE(name)
	);
END;

COMMIT;


BEGIN TRANSACTION;


-- 2 
IF OBJECT_ID('dbo.t_technical_tasks') IS NULL
BEGIN
	CREATE TABLE t_technical_tasks(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_technical_tasks_id PRIMARY KEY,
		description VARBINARY NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 3 
IF OBJECT_ID('dbo.t_customers') IS NULL
BEGIN
	CREATE TABLE t_customers(
		id BIGINT NOT NULL IDENTITY PRIMARY KEY,
		law_face VARCHAR(100) NOT NULL CONSTRAINT t_customers_law_face UNIQUE(law_face),
		law_addres VARCHAR(250) NOT NULL,
		director VARCHAR(100) NOT NULL,
		work_phone VARCHAR(20) NOT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 4 
IF OBJECT_ID('dbo.t_orders') IS NULL
BEGIN
	CREATE TABLE t_orders(
		-- Create id field with primary key and auto increment :
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_orders_id PRIMARY KEY,
		id_customer BIGINT NOT NULL CONSTRAINT fk_t_orders_id_customer FOREIGN KEY (id_customer) REFERENCES t_customers(id),
		accept_date DATE NOT NULL,
		deadline DATE NOT NULL,
		id_command BIGINT NOT NULL CONSTRAINT fk_t_orders_id_command FOREIGN KEY (id_command) REFERENCES t_commands(id),
		payment MONEY NOT NULL CONSTRAINT payment CHECK(payment > 0),
		id_tt BIGINT NOT NULL CONSTRAINT fk_t_orders_id_tt FOREIGN KEY (id_tt) REFERENCES t_technical_tasks(id)
	);
END;

COMMIT;


BEGIN TRANSACTION;
-- Allow package execution :
GO

-- Trigger for check deadline value inserted or updated 
CREATE TRIGGER trg_t_orders_deadline_check
ON t_orders
AFTER INSERT, UPDATE
AS
BEGIN
	IF EXISTS ( SELECT 1 FROM inserted WHERE deadline <= accept_date )
    BEGIN
        RAISERROR ('Deadline must be greater than order_date.', 16, 1);
        ROLLBACK TRANSACTION;
    END
END;

-- Close allow package execution :
GO

COMMIT;

BEGIN TRANSACTION;

-- 5 
IF OBJECT_ID('dbo.t_employees') IS NULL
BEGIN
	CREATE TABLE t_employees(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_employees_id PRIMARY KEY,
		surname VARCHAR(50) NOT NULL,
		name VARCHAR(50) NOT NULL,
		last_name VARCHAR(50) NOT NULL,
		position VARCHAR(50) NOT NULL,
		job VARCHAR(50) NOT NULL,
		date_of_employment DATE NOT NULL,
		grade VARCHAR(30) NOT NULL,
		id_command BIGINT NOT NULL CONSTRAINT fk_t_employees_id_command FOREIGN KEY (id_command) REFERENCES t_commands(id)
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 6 
IF OBJECT_ID('dbo.t_expenses_items') IS NULL
BEGIN
	CREATE TABLE t_expenses_items(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_expenses_items_id PRIMARY KEY,
		name VARCHAR(100) NOT NULL,
		description VARCHAR(300) NOT NULL
	);
END;

COMMIT;

BEGIN TRANSACTION;

-- 7 
IF OBJECT_ID('dbo.t_expenses') IS NULL
BEGIN
	CREATE TABLE t_expenses(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_expenses_id PRIMARY KEY,
		date DATE NOT NULL,
		cost MONEY NOT NULL CONSTRAINT t_expenses_cost CHECK (cost > 0),
		expense_id BIGINT NOT NULL CONSTRAINT fk_t_expenses_expense_id FOREIGN KEY (expense_id) REFERENCES t_expenses_items(id),
		note VARCHAR(300) NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 8 
IF OBJECT_ID('dbo.t_profit_items') IS NULL
BEGIN
	CREATE TABLE t_profit_items(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_profit_items_id PRIMARY KEY,
		name VARCHAR(100) NOT NULL,
		description VARCHAR(300) NOT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 9 
IF OBJECT_ID('dbo.t_profits') IS NULL
BEGIN
	CREATE TABLE t_profits(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_profits_id PRIMARY KEY,
		date DATE NOT NULL,
		cost MONEY NOT NULL CONSTRAINT t_profits_cost CHECK (cost > 0),
		profit_id BIGINT NOT NULL CONSTRAINT fk_t_profits_profit_id FOREIGN KEY (profit_id) REFERENCES t_profit_items(id),
		note VARCHAR(300) NOT NULL,
		order_id BIGINT NOT NULL CONSTRAINT fk_t_profits_order_id FOREIGN KEY (order_id) REFERENCES t_orders(id)
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 10 
IF OBJECT_ID('dbo.t_applicants') IS NULL
BEGIN
	CREATE TABLE t_applicants(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_applicants_id PRIMARY KEY,
		surname VARCHAR(50) NOT NULL,
		name VARCHAR(50) NOT NULL,
		last_name VARCHAR(50) NOT NULL,
		job VARCHAR(50) NOT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;


-- 11 
IF OBJECT_ID('dbo.t_testing_result') IS NULL
BEGIN
	CREATE TABLE t_testing_result(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_testing_result_id PRIMARY KEY,
		applicant_id BIGINT NOT NULL CONSTRAINT fk_t_testing_result_applicant_id FOREIGN KEY (applicant_id) REFERENCES 	t_applicants(id),
		correct_answers INT NOT NULL,
		incorrect_answers INT NOT NULL,
		is_passed BIT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 12 
IF OBJECT_ID('dbo.t_testing_questions') IS NULL
BEGIN
	CREATE TABLE t_testing_questions(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_testing_questions_id PRIMARY KEY,
		question_number BIGINT NOT NULL,
		job VARCHAR(50) NOT NULL,
		question_text VARCHAR(300) NOT NULL,
		question_type VARCHAR(100) NOT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 13 
IF OBJECT_ID('dbo.t_answers') IS NULL
BEGIN
	CREATE TABLE t_answers(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_answers_id PRIMARY KEY,
		question_number BIGINT NOT NULL,
		question_text VARCHAR(300) NOT NULL,
		is_correct BIT NULL,
		question_id BIGINT NOT NULL CONSTRAINT fk_t_answers_question_id FOREIGN KEY (question_id) REFERENCES t_testing_questions(id)
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 14 
IF OBJECT_ID('dbo.t_interview') IS NULL
BEGIN
	CREATE TABLE t_interview(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_interview_id PRIMARY KEY,
		applicant_id BIGINT NOT NULL CONSTRAINT fk_t_interview_applicant_id FOREIGN KEY (applicant_id) REFERENCES t_applicants(id),
		interview_date DATE NOT NULL,															 
		interview_time DATE NOT NULL,
		is_passed BIT NOT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;

-- 15
IF OBJECT_ID('dbo.t_files') IS NULL
BEGIN
	CREATE TABLE t_files(
		id BIGINT NOT NULL IDENTITY CONSTRAINT pk_t_files_id PRIMARY KEY,
		file_name VARCHAR(100) NOT NULL,
		b_data VARBINARY,
		order_id BIGINT NOT NULL CONSTRAINT fk_t_files_order_id FOREIGN KEY (order_id) REFERENCES t_orders(id),
		life_time DATE NOT NULL
	);
END;

COMMIT;


BEGIN TRANSACTION;


-- INSERTS :
-- Insert into t_commands
INSERT INTO dbo.t_commands (name) VALUES 
('beta'), 
('alpha'), 
('dev'), 
('desgin'), 
('Маркетологи'),
('Управляющий персонал'),
('Кадры'),
('Дизайнеры'),
('bell'),
('simple');

COMMIT;


BEGIN TRANSACTION;


-- Insert into t_customers (must be done first as t_orders references this table)
INSERT INTO dbo.t_customers (law_face, law_addres, director, work_phone) VALUES 
('ООО Цифра', 'г. Санкт-Петербург, ул. Фонтанная 10, п. 1', 'Витенин Олег Олегович', '+79457815687'),
('ООО Клиник-Супер', 'г. Новосибирск, ул. Ленина 40, п. 5', 'Сицин Артём Петрович', '+79625451287'),
('ОАО Диджитал-Сити', 'г. Красноярск, ул. Восточная, 15', 'Гончаров РУслан Максимович', '1234567892'),
('ООО Продукт Качества', 'г. Павловсикий посад, пл. Будапешская, 57', 'Соловьева Ирина Николаевна', '1234567893'),
('ООО Аврора', 'г. Воскресенск, ул. Домодедовская, 97', 'Ильинская Елизавета Макаровна', '1234567894'),
('МФО ЗарайскОрион', 'г. Зарайск, пр. Ладыгина, 88', 'Сидорова Таисия Кирилловна', '1234567895'),
('ОАО СервисРосДизайн', 'г. Можайск, пр. Ломоносова, 81', 'Пирогов Максим Артёмович', '1234567896'),
('МКК РосВектор', 'г. Дмитров, пл. Гагарина, 63', 'Рыбакова Лидия Марковна', '1234567897'),
('ООО Тверь IT', 'г. Тверь, ул. Будапешская, 33', 'Горлова Ксения Тихонова', '1234567898'),
('ЗАО Вектор', 'г. Солнечногорск, б. Косиора, 34', 'Наумова Полина Эмировна', '1234567899');


COMMIT;


BEGIN TRANSACTION;


-- Insert into t_technical_tasks
INSERT INTO dbo.t_technical_tasks (description) VALUES 
(NULL),
(NULL),
(NULL),
(NULL),
(NULL),
(NULL),
(NULL),
(NULL),
(NULL),
(NULL);

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_orders (after t_customers to ensure valid id_customer references)
INSERT INTO dbo.t_orders (id_customer, accept_date, deadline, id_command, payment, id_tt) VALUES
(1, '2024-11-01', '2024-11-10', 1, 1000, 1),
(2, '2024-11-02', '2024-11-15', 2, 1500, 2),
(3, '2024-11-03', '2024-11-20', 3, 1200, 3),
(4, '2024-11-04', '2024-11-25', 4, 1100, 4),
(5, '2024-11-05', '2024-11-30', 5, 1300, 5),
(6, '2024-11-06', '2024-12-05', 6, 1400, 6),
(7, '2024-11-07', '2024-12-10', 7, 1600, 7),
(8, '2024-11-08', '2024-12-15', 8, 1700, 8),
(9, '2024-11-09', '2024-12-20', 9, 1800, 9),
(10, '2024-11-10', '2024-12-25', 10, 1900, 10);

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_expenses_items
INSERT INTO dbo.t_expenses_items (name, description) VALUES
('Корпоротив', 'Вечер в кафе (Мама Варит Кофе)'),
('Роутер', 'TP Link Archer 5'),
('Ноутбук', 'ASUS Vivobook f757857'),
('Ручки', 'Ручки Ericrouther x2'),
('Такси', 'Такси в час пик пн 8:00'),
('Лосось', '6 кг'),
('usb-Ethernet', '5 штук'),
('Принтер ЧБ', '1 штука'),
('Сканнер', '2 штуки'),
('Сервер', '1 юнит, 2GB RAM 1 core CPU 2.88 Ghz');

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_expenses (after t_expenses_items to ensure valid expense_id references)
INSERT INTO dbo.t_expenses (date, cost, expense_id, note) VALUES
('2024-11-01', 100.00, 1, '4 чашки экспрессо '),
('2024-11-02', 200.00, 2, 'вовремя'),
('2024-11-03', 150.00, 3, 'Спас проект'),
('2024-11-04', 120.00, 4, 'Директор доволен'),
('2024-11-05', 130.00, 5, 'вовремя попал на встречу'),
('2024-11-06', 140.00, 6, 'было вкусно'),
('2024-11-07', 160.00, 7, 'работают хорошо !'),
('2024-11-08', 170.00, 8, 'Отчёт был распечатан вовремя'),
('2024-11-09', 180.00, 9, 'Данные были загруженны на сервер'),
('2024-11-10', 190.00, 10, '10 ошибок ПО было поймано на тестировании )))');

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_profit_items
INSERT INTO dbo.t_profit_items (name, description) VALUES
('Telegram-бот Семинары  ИБ', 'Бот для регистрации на семинары по ИБ'),
('Игра lucky boxes', 'В игре можно открывать коробки и в  них могут лежать как бонусы так и что-то другое'),
('Веб админ панель', 'авторизованному пользователю даёт возможность управлять ботами'),
('Продажа сервера', 'CPU x86 Xeon 4373F'),
('Интеграция Telegram бота на сайт', 'Просрочек 3'),
('Админ панель для управления сервером', 'Срочный заказ'),
('Бот', 'для регистрации и личного кабинета на сайте'),
('Aiogram v 3.x bot', 'webhook setted !'),
('Profit Item 9', 'Description of profit item 9'),
('Profit Item 10', 'Description of profit item 10');

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_profits (after t_orders to ensure valid order_id references)
INSERT INTO dbo.t_profits (date, cost, profit_id, note, order_id) VALUES
('2024-11-01', 1000.00, 1, 'интересный заказ', 1),
('2024-11-02', 1500.00, 2, 'Душный заказ', 2),
('2024-11-03', 1200.00, 3, 'Заказчик доволен', 3),
('2024-11-04', 1100.00, 4, 'Морально устарел', 4),
('2024-11-05', 1300.00, 5, 'Не успели', 5),
('2024-11-06', 1400.00, 6, 'Сдано вовремя', 6),
('2024-11-07', 1600.00, 7, 'Интересный заказ', 7),
('2024-11-08', 1700.00, 8, 'научился ставить webhook aiogram v 3.x', 8),
('2024-11-09', 1800.00, 9, 'Profit from project 9', 9),
('2024-11-10', 1900.00, 10, 'Profit from project 10', 10);

COMMIT;


BEGIN TRANSACTION;


-- Insert into t_applicants
INSERT INTO dbo.t_applicants (surname, name, last_name, job) VALUES
('Smith', 'John', 'Doe', 'Engineer'),
('Johnson', 'Jane', 'Doe', 'Manager'),
('Brown', 'Alice', 'Smith', 'Developer'),
('Williams', 'Bob', 'Jones', 'Designer'),
('Jones', 'Tom', 'Taylor', 'Analyst'),
('Miller', 'Emily', 'Davis', 'Manager'),
('Davis', 'Michael', 'Wilson', 'Engineer'),
('Garcia', 'Sophia', 'Martinez', 'Technician'),
('Rodriguez', 'Daniel', 'Lopez', 'Salesperson'),
('Martinez', 'David', 'Garcia', 'Consultant');

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_testing_result (after t_applicants to ensure valid applicant_id references)
INSERT INTO dbo.t_testing_result (applicant_id, correct_answers, incorrect_answers, is_passed) VALUES
(1, 8, 2, 1),
(2, 7, 3, 1),
(3, 9, 1, 1),
(4, 6, 4, 0),
(5, 8, 2, 1),
(6, 7, 3, 1),
(7, 5, 5, 0),
(8, 10, 0, 1),
(9, 4, 6, 0),
(10, 8, 2, 1);

COMMIT;


BEGIN TRANSACTION;

-- Insert into t_testing_questions
INSERT INTO dbo.t_testing_questions (question_number, job, question_text, question_type) VALUES
(1, 'Engineer', 'What is SQL?', 'Multiple Choice'),
(2, 'Manager', 'Describe your experience with management tools.', 'Open Answer'),
(3, 'Developer', 'What is a join in', 'Open Answer'),
(4, 'Designer', 'What software tools do you use for designing?', 'Open Answer'),
(5, 'Analyst', 'Explain the importance of data visualization in analytics.', 'Multiple Choice'),
(6, 'Technician', 'What is the purpose of a network switch?', 'Multiple Choice'),
(7, 'Salesperson', 'Describe a successful sales strategy you implemented.', 'Open Answer'),
(8, 'Consultant', 'What is your approach to solving complex client problems?', 'Open Answer'),
(9, 'Engineer', 'What is the difference between TCP and UDP protocols?', 'Multiple Choice'),
(10, 'Manager', 'How do you handle conflicts within your team?', 'Open Answer');

COMMIT;


BEGIN TRANSACTION;


INSERT INTO t_employees (surname, name, last_name, position, job, date_of_employment, grade, id_command)
VALUES
    ('Smith', 'John', 'Doe', 'Manager', 'Sales', '2020-05-15', 'A', 1),
    ('Johnson', 'Jane', 'Smith', 'Developer', 'IT', '2021-03-20', 'B', 2),
    ('Williams', 'Michael', 'Taylor', 'Analyst', 'Finance', '2019-07-30', 'A', 3),
    ('Brown', 'Emily', 'Davis', 'HR Specialist', 'HR', '2022-01-10', 'B', 4),
    ('Jones', 'David', 'Miller', 'Technician', 'IT Support', '2020-06-25', 'C', 2),
    ('Garcia', 'Maria', 'Rodriguez', 'Marketing Manager', 'Marketing', '2018-09-11', 'A', 5),
    ('Martinez', 'Luis', 'Hernandez', 'Accountant', 'Finance', '2021-02-18', 'B', 3),
    ('Hernandez', 'Laura', 'Lopez', 'Team Leader', 'IT', '2022-04-05', 'A', 6),
    ('Young', 'James', 'Scott', 'Designer', 'Creative', '2017-11-22', 'B', 7),
    ('King', 'Patricia', 'Wright', 'Assistant Manager', 'Sales', '2020-08-12', 'C', 1);

COMMIT;
