-- =========================
-- 7.1 INDEX
-- =========================

CREATE INDEX IF NOT EXISTS idx_students_gpa
ON students(gpa);

EXPLAIN QUERY PLAN
SELECT * FROM students WHERE gpa > 3.5;


-- =========================
-- 7.2 VIEW: enrollment_details
-- =========================

CREATE VIEW IF NOT EXISTS enrollment_details AS
SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    c.code AS course_code,
    c.title AS course_title,
    g.letter_grade
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
LEFT JOIN grades g ON g.student_id = s.id AND g.course_id = c.id;


-- Example query
SELECT * FROM enrollment_details
WHERE letter_grade = 'A';


-- =========================
-- 7.3 VIEW: course_statistics
-- =========================

CREATE VIEW IF NOT EXISTS course_statistics AS
SELECT
    c.code,
    c.title,
    COUNT(e.student_id) AS total_students,
    AVG(g.final) AS avg_final_score
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
LEFT JOIN grades g ON g.course_id = c.id
GROUP BY c.id;


-- =========================
-- 7.4 INSERT NEW STUDENT
-- =========================

INSERT INTO students (first_name, last_name, email, enrollment_year, gpa)
VALUES ('New', 'Student', 'newstudent@school.edu', 2024, NULL);


-- =========================
-- 7.5 UPDATE GPA
-- =========================

UPDATE students
SET gpa = 3.22
WHERE id = 17;


-- =========================
-- 7.6 SAFE DELETE (preview first)
-- =========================

-- Preview:
SELECT *
FROM grades
WHERE letter_grade = 'F';

-- Delete:
DELETE FROM grades
WHERE letter_grade = 'F';


-- =========================
-- 7.7 TRANSACTION: ENROLLMENT
-- =========================

BEGIN TRANSACTION;

INSERT INTO enrollments (student_id, course_id)
VALUES (1, 13);

INSERT INTO grades (student_id, course_id, final, letter_grade)
VALUES (1, 13, NULL, NULL);

COMMIT;


-- =========================
-- 7.8 TRANSACTION: LIBRARY LOAN
-- =========================

BEGIN TRANSACTION;

-- Check availability first (manual safety step)
SELECT available_copies FROM books WHERE id = 3;

-- If available > 0, proceed:
UPDATE books
SET available_copies = available_copies - 1
WHERE id = 3;

INSERT INTO loans (member_id, book_id, loan_date, due_date)
VALUES (3, 3, '2026-05-09', '2026-05-23');

COMMIT;


-- =========================
-- 7.9 EXPLAIN QUERY PLAN NOTES
-- =========================

-- A) Slow version:
-- SELECT * FROM students WHERE LOWER(email) = 'alice@school.edu';

-- B) Fast version:
-- SELECT * FROM students WHERE email = 'alice@school.edu';

-- NOTE:
-- The index cannot be used in version A because LOWER(email)
-- changes the column value at runtime, breaking index usage.


-- =========================
-- 7.10 COMPOUND INDEX
-- =========================

CREATE INDEX IF NOT EXISTS idx_enrollments_student_course
ON enrollments(student_id, course_id);

EXPLAIN QUERY PLAN
SELECT * FROM enrollments
WHERE student_id = 5 AND course_id = 1;
