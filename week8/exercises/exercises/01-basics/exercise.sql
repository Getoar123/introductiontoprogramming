-- 1.1 — All students
SELECT first_name, last_name
FROM students;

-- 1.2 — Emails alphabetically
SELECT email
FROM students
ORDER BY email;

-- 1.3 — High achievers
SELECT first_name, last_name, gpa
FROM students
WHERE gpa > 3.5;

-- 1.4 — Class of 2021
SELECT *
FROM students
WHERE enrollment_year = 2021;

-- 1.5 — Middle GPAs
SELECT first_name, last_name, gpa
FROM students
WHERE gpa BETWEEN 3.0 AND 3.5;

-- 1.6 — Specific student
SELECT *
FROM students
WHERE email = 'grace@school.edu';

-- 1.7 — First 5 students
SELECT *
FROM students
ORDER BY id
LIMIT 5;

-- 1.8 — Who has no GPA?
SELECT *
FROM students
WHERE gpa IS NULL;

-- 1.9 — High salary teachers
SELECT first_name, last_name, salary
FROM teachers
WHERE salary > 80000;

-- 1.10 — Courses worth 4 credits
SELECT code, title
FROM courses
WHERE credits = 4;
