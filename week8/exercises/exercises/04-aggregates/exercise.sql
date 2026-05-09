-- 4.1 — Total students
SELECT COUNT(*) AS total_students
FROM students;

-- 4.2 — Students per enrollment year
SELECT enrollment_year, COUNT(*) AS count
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year;

-- 4.3 — Average GPA
SELECT ROUND(AVG(gpa), 2) AS avg_gpa
FROM students;

-- 4.4 — Highest, lowest, average GPA
SELECT 
    MAX(gpa) AS highest_gpa,
    MIN(gpa) AS lowest_gpa,
    ROUND(AVG(gpa), 2) AS avg_gpa
FROM students;

-- 4.5 — Courses per department (include empty departments)
SELECT d.id, COUNT(c.id) AS course_count
FROM departments d
LEFT JOIN courses c ON d.id = c.department_id
GROUP BY d.id;

-- 4.6 — Students per course
SELECT course_id, COUNT(*) AS student_count
FROM enrollments
GROUP BY course_id
ORDER BY student_count DESC;

-- 4.7 — Popular courses only (> 3 students)
SELECT course_id, COUNT(*) AS student_count
FROM enrollments
GROUP BY course_id
HAVING COUNT(*) > 3;

-- 4.8 — Average grade per course
SELECT course_id, ROUND(AVG(final), 1) AS avg_final
FROM grades
GROUP BY course_id;

-- 4.9 — Department salary stats
SELECT department_id,
       COUNT(*) AS teacher_count,
       ROUND(AVG(salary), 0) AS avg_salary,
       MAX(salary) AS max_salary
FROM teachers
GROUP BY department_id;

-- 4.10 — Overdue fines
SELECT SUM(fine) AS total_fines,
       AVG(fine) AS avg_fine
FROM loans
WHERE fine > 0;

-- 4.11 — Books per genre
SELECT genre_id, COUNT(*) AS book_count
FROM books
GROUP BY genre_id
ORDER BY book_count DESC;

-- 4.12 — High salary departments
SELECT department_id, ROUND(AVG(salary), 0) AS avg_salary
FROM teachers
GROUP BY department_id
HAVING AVG(salary) > 75000;
