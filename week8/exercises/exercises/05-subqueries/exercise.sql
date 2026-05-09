-- 5.1 Above Average GPA
SELECT first_name, last_name, gpa
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);


-- 5.2 CS50 Students
SELECT first_name, last_name
FROM students
WHERE id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT id FROM courses WHERE code = 'CS50'
    )
);


-- 5.3 NOT in CS50
SELECT first_name, last_name
FROM students
WHERE id NOT IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT id FROM courses WHERE code = 'CS50'
    )
);


-- 5.4 Courses taught by highest-paid teacher
SELECT title
FROM courses
WHERE teacher_id = (
    SELECT id
    FROM teachers
    WHERE salary = (SELECT MAX(salary) FROM teachers)
);


-- 5.5 Students with 3+ courses
SELECT first_name, last_name
FROM students
WHERE id IN (
    SELECT student_id
    FROM enrollments
    GROUP BY student_id
    HAVING COUNT(*) >= 3
);


-- 5.6 Well-read members (>2 books)
SELECT first_name, last_name
FROM members
WHERE id IN (
    SELECT member_id
    FROM loans
    GROUP BY member_id
    HAVING COUNT(*) > 2
);


-- 5.7 Books above average page count
SELECT title, pages
FROM books
WHERE pages > (
    SELECT AVG(pages) FROM books
);


-- 5.8 EXISTS: students with grades
SELECT first_name, last_name
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM grades g
    WHERE g.student_id = s.id
);


-- 5.9 NOT EXISTS: courses with no grades
SELECT title
FROM courses c
WHERE NOT EXISTS (
    SELECT 1
    FROM grades g
    WHERE g.course_id = c.id
);


-- 5.10 Most popular course(s) — no LIMIT
SELECT title
FROM courses
WHERE id IN (
    SELECT course_id
    FROM enrollments
    GROUP BY course_id
    HAVING COUNT(*) = (
        SELECT MAX(course_count)
        FROM (
            SELECT COUNT(*) AS course_count
            FROM enrollments
            GROUP BY course_id
        )
    )
);
