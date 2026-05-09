-- 3.1 — Student + Course Names
SELECT s.first_name, s.last_name, c.title
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id;

-- 3.2 — Who teaches what?
SELECT c.title, t.first_name, t.last_name
FROM courses c
JOIN teachers t ON c.teacher_id = t.id;

-- 3.3 — Department + Teacher
SELECT t.first_name, t.last_name, d.name
FROM teachers t
JOIN departments d ON t.department_id = d.id;

-- 3.4 — Full enrollment details
SELECT s.first_name, s.last_name,
       c.title,
       t.first_name, t.last_name,
       g.letter_grade
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
JOIN teachers t ON c.teacher_id = t.id
JOIN grades g ON e.id = g.enrollment_id;

-- 3.5 — Students with no enrollments
SELECT s.first_name, s.last_name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.student_id IS NULL;

-- 3.6 — Courses with no students
SELECT c.title
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
WHERE e.course_id IS NULL;

-- 3.7 — Book + Author names
SELECT b.title, a.first_name, a.last_name
FROM books b
JOIN book_authors ba ON b.id = ba.book_id
JOIN authors a ON ba.author_id = a.id;

-- 3.8 — Genre + book count (including empty genres)
SELECT g.name, COUNT(b.id) AS book_count
FROM genres g
LEFT JOIN books b ON g.id = b.genre_id
GROUP BY g.name;

-- 3.9 — Member loan history
SELECT m.first_name, m.last_name, b.title
FROM members m
LEFT JOIN loans l ON m.id = l.member_id
LEFT JOIN books b ON l.book_id = b.id;

-- 3.10 — Challenge: full loan report
SELECT m.first_name || ' ' || m.last_name AS member,
       b.title,
       l.loan_date,
       COALESCE(l.return_date, 'Not returned') AS return_status
FROM loans l
JOIN members m ON l.member_id = m.id
JOIN books b ON l.book_id = b.id;
