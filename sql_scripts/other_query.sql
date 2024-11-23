-- CREATE DATABASE t_scos;

USE t_scos;


INSERT INTO dbo.t_commands (code_name) VALUES ('alpha_one'), ('beta_two'), ('gamma_three'), ('delta_four'), ('epsilon_five'), ('zeta_six'), 
('eta_seven'), ('theta_eight'), ('iota_nine'), ('kappa_ten');


INSERT INTO dbo.t_employees (surname, name, last_name, position, job, date_of_employment, grade, id_command) VALUES
('Smith', 'John', 'Doe', 'Manager', 'Sales', '2020-01-01', 'A', 1),
('Johnson', 'Alice', 'Brown', 'Developer', 'Software', '2019-02-15', 'B', 2),
('Williams', 'Bob', 'Jones', 'Analyst', 'Business', '2021-03-20', 'C', 3),
('Jones', 'Catherine', 'Davis', 'Designer', 'Graphic', '2018-04-25', 'A', 4),
('Brown', 'David', 'Wilson', 'Tester', 'Quality', '2022-05-30', 'B', 5),
('Davis', 'Elizabeth', 'Taylor', 'Support', 'Technical', '2023-06-10', 'C', 6),
('Miller', 'George', 'Anderson', 'Administrator', 'System', '2017-07-05', 'A', 7),
('Wilson', 'Sarah', 'Thomas', 'HR', 'Human Resources', '2020-08-15', 'B', 8),
('Moore', 'James', 'Martinez', 'Manager', 'Marketing', '2021-09-25', 'A', 9),
('Taylor', 'Michael', 'Jackson', 'CEO', 'Executive', '2015-10-01', 'A', 10);


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


INSERT INTO dbo.t_customers (law_face, law_addres, director, work_phone) VALUES 
('Customer1', 'Address1', 'Director1', '1234567890'),
('Customer2', 'Address2', 'Director2', '1234567891'),
('Customer3', 'Address3', 'Director3', '1234567892'),
('Customer4', 'Address4', 'Director4', '1234567893'),
('Customer5', 'Address5', 'Director5', '1234567894'),
('Customer6', 'Address6', 'Director6', '1234567895'),
('Customer7', 'Address7', 'Director7', '1234567896'),
('Customer8', 'Address8', 'Director8', '1234567897'),
('Customer9', 'Address9', 'Director9', '1234567898'),
('Customer10', 'Address10', 'Director10', '1234567899');


INSERT INTO dbo.t_technical_tasks (description) VALUES 
('Task description 1'), ('Task description 2'), ('Task description 3'),
('Task description 4'), ('Task description 5'), 
('Task description 6'), ('Task description 7'), ('Task description 8'),
('Task description 9'), ('Task description 10');


INSERT INTO dbo.t_profit_items (name, description) VALUES
('Profit1', 'Description for profit item 1'),
('Profit2', 'Description for profit item 2'),
('Profit3', 'Description for profit item 3'),
('Profit4', 'Description for profit item 4'),
('Profit5', 'Description for profit item 5'),
('Profit6', 'Description for profit item 6'),
('Profit7', 'Description for profit item 7'),
('Profit8', 'Description for profit item 8'),
('Profit9', 'Description for profit item 9'),
('Profit10', 'Description for profit item 10');



INSERT INTO dbo.t_profits (date, cost, profit_id, note, order_id) VALUES
('2024-11-01', 1000.00, 1, 'Profit from project 1', 1),
('2024-11-02', 1500.00, 2, 'Profit from project 2', 2),
('2024-11-03', 1200.00, 3, 'Profit from project 3', 3),
('2024-11-04', 1100.00, 4, 'Profit from project 4', 4),
('2024-11-05', 1300.00, 5, 'Profit from project 5', 5),
('2024-11-06', 1400.00, 6, 'Profit from project 6', 6),
('2024-11-07', 1600.00, 7, 'Profit from project 7', 7),
('2024-11-08', 1700.00, 8, 'Profit from project 8', 8),
('2024-11-09', 1800.00, 9, 'Profit from project 9', 9),
('2024-11-10', 1900.00, 10, 'Profit from project 10', 10);



INSERT INTO dbo.t_applicants (surname, name, last_name, job) VALUES
('Smith', 'John', 'Doe', 'Developer'),
('Johnson', 'Alice', 'Brown', 'Manager'),
('Williams', 'Bob', 'Jones', 'Analyst'),
('Jones', 'Catherine', 'Davis', 'Tester'),
('Brown', 'David', 'Wilson', 'HR'),
('Davis', 'Elizabeth', 'Taylor', 'Designer'),
('Miller', 'George', 'Serge', 'Developer');




/*
Сортировка, поиск, фильтрация данных
Формирование и вывод отчётов 
Организация запросов SQL 
Работа с макросами.
*/