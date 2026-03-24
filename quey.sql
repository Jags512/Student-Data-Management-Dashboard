-- Average Marks
SELECT AVG(marks) FROM students;

-- Branch-wise Performance
SELECT branch, AVG(marks) AS avg_marks
FROM students
GROUP BY branch;

-- Attendance Analysis
SELECT year, AVG(attendance)
FROM students
GROUP BY year;
