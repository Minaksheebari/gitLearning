SELECT * FROM students.students;

-- 1. Question: For each class, find the student(s) who scored the highest in Science.
SELECT c.class_name, st.student_name
FROM Classes c
JOIN students st ON c.class_id = st.class_id
JOIN scores sc ON st.student_id = sc.student_id
WHERE sc.subject = 'Science'
AND sc.score = (
  SELECT MAX(score) 
  FROM Scores 
  WHERE subject = 'Science'
);

-- Query 2: List the names of students who scored lower in Math than their average Science score.
SELECT st.student_name
FROM Students st
JOIN Scores sm ON st.student_id = sm.student_id
JOIN (
  SELECT student_id, AVG(score) AS avg_sci_score
  FROM Scores
  WHERE subject = 'Science'
  GROUP BY student_id
) asv ON st.student_id = asv.student_id
WHERE sm.subject = 'Math'
AND sm.score < asv.avg_sci_score;

-- Query 3: Display the class names with the highest number of students who scored above 80 in any subject.
SELECT c.class_name
FROM Classes c
JOIN Students st ON c.class_id = st.class_id
JOIN Scores sc ON st.student_id = sc.student_id
WHERE sc.score > 80
GROUP BY c.class_name
HAVING COUNT(DISTINCT st.student_id) = (
  SELECT MAX(student_count)
  FROM (
    SELECT COUNT(DISTINCT st.student_id) AS student_count
    FROM Students st
    JOIN Scores sc ON st.student_id = sc.student_id
    WHERE sc.score > 80
    GROUP BY st.class_id
  ) subquery
);

-- Query 4: Find the students who scored the highest in each subject.
SELECT subject, student_name, score AS highest_score
FROM (
  SELECT subject, student_name, score,
         ROW_NUMBER() OVER (PARTITION BY subject ORDER BY score DESC) AS rn
  FROM Scores
  JOIN Students ON Scores.student_id = Students.student_id
) ranked_scores
WHERE rn = 1;

-- Query 5: List the names of students who scored higher than the average of any student's score in their own class.
SELECT s.student_name
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
WHERE sc.score > (
  SELECT AVG(score)
  FROM Scores
  WHERE student_id IN (
    SELECT student_id
    FROM Students
    WHERE class_id = s.class_id
  )
);

-- Query 6: Find the class(es) where the students' average age is above the average age of all students.
SELECT c.class_name
FROM Classes c
JOIN Students st ON c.class_id = st.class_id
GROUP BY c.class_name
HAVING AVG(st.age) > (
  SELECT AVG(age)
  FROM Students
);

-- Query 7: Display the student names and their total scores, ordered by the total score in descending order.
SELECT student_name, SUM(score) AS total_score
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY student_name
ORDER BY total_score DESC;

-- Query 7: Display the student names and their total scores, ordered by the total score in descending order.
SELECT student_name, SUM(score) AS total_score
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY student_name
ORDER BY total_score DESC;

-- Query 8: Find the student(s) who scored the highest in the class with the lowest average score.
SELECT s.student_name
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
WHERE sc.score = (
  SELECT MAX(score)
  FROM Scores
  WHERE student_id IN (
    SELECT student_id
    FROM Students
    WHERE class_id = (
      SELECT class_id
      FROM (
        SELECT class_id, AVG(score) AS avg_score
        FROM Students s
        JOIN Scores sc ON s.student_id = sc.student_id
        GROUP BY class_id
        ORDER BY avg_score ASC
        LIMIT 1
      ) subquery
    )
  )
);

-- Query 9: List the names of students who scored the same as Alice in at least one subject
SELECT DISTINCT s.student_name
FROM Students s
JOIN Scores sa ON s.student_id = sa.student_id
JOIN Scores alice ON alice.student_id = (
  SELECT student_id
  FROM Students
  WHERE student_name = 'Alice'
)
WHERE sa.score = alice.score
AND s.student_name <> 'Alice';


-- Query 10: Display the class names along with the number of students who scored below the average score in their class.
SELECT c.class_name, COUNT(*) AS below_average_count
FROM Classes c
JOIN Students s ON c.class_id = s.class_id
JOIN Scores sc ON s.student_id = sc.student_id
WHERE sc.score < (
  SELECT AVG(score)
  FROM Scores
  WHERE student_id IN (
    SELECT student_id
    FROM Students
    WHERE class_id = s.class_id
  )
)
GROUP BY c.class_name;







