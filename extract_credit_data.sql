-- lets think of a schema as a folder that groups related tables
-- the schema is created first becuase you can't put a table inside a schema that doesnt exist yet (will return an error)

-- PRIMARY KEY: (1) it tells the database this column muct be unique (no two customers can have the same ID)
-- 				(2) it tells the database this column can never be NULL
--		This is a database-enforce guarantee, not jsut documentation
--		If (2)'s Pyhton script ever tried to insert a dup client_id. the database itself would reject it

-- CHECK: This is a constraint, PRIMARY KEY enforces uniqueness; CHECK enforces a business rule directly at the database level
--		=> meaning: no row is allowed to exist where age is below 18 or above 100
--	This is important for data quality enforcement, if .py script ever had a bug about age, the check line would refuse the row
--	rather that letting garbage data silently flow into our ML model later


CREATE SCHEMA IF NOT EXISTS bank_production;

CREATE TABLE bank_production.cleint_credit_history(
	client_id INTEGER PRIMARY KEY,
	age INTEGER CHECK (age >= 18 AND age <= 100),
	monthly_income DECIMAL(10, 2) CHECK (monthly_income >= 0),
	active_dept DECIMAL(10, 2) CHECK (active_dept >= 0),
	credit_utilization_ratio DECIMAL(5, 4) CHECK (credit_utilization_ratio >= 0 AND credit_utilization_ratio <= 1),
	employment_status VARCHAR CHECK (employment_status IN ('employed', 'self-employed', 'unemployed')),
	days_in_arrears INTEGER CHECK (days_in_arrears >= 0) DEFAULT 0,
	defualt_flag BOOLEAN NOT NULL,
	record_date DATE NOT NULL DEFAULT CURRENT_DATE
);

