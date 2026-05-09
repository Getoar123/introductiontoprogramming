-- 2.1 — Last name contains "s"
SELECT *
FROM students
WHERE last_name LIKE '%s%';

-- 2.2 — Email domain search
SELECT *
FROM teachers
WHERE email LIKE '%@cs50.harvard.edu';

-- 2.3 — Top 5 GPAs
SELECT first_name, last_name, gpa
FROM students
ORDER BY gpa DESC
LIMIT 5;

-- 2.4 — Distinct enrollment years
SELECT DISTINCT enrollment_year
FROM students;

-- 2.5 — Departments 1 or 2
SELECT *
FROM courses
WHERE department_id IN (1, 2);

-- 2.6 — Not from 2018
SELECT *
FROM students
WHERE enrollment_year NOT IN (2018);

-- 2.7 — Sort courses by credits then title
SELECT *
FROM courses
ORDER BY credits DESC, title ASC;

-- 2.8 — Books starting with "The"
SELECT *
FROM books
WHERE title LIKE 'The%';

-- 2.9 — Non-returned loans
SELECT loan_id, member_id, due_date
FROM loans
WHERE return_date IS NULL;

-- 2.10 — British authors
SELECT *
FROM authors
WHERE country = 'British'
ORDER BY last_name;

-- 2.11 — Premium and student members
SELECT *
FROM members
WHERE membership_type IN ('premium', 'student');

-- 2.12 — 4-letter first names
SELECT *
FROM students
WHERE first_name LIKE '____';
