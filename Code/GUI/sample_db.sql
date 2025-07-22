-- Create Database:
CREATE DATABASE IF NOT EXISTS homework_db
USE homework_db

-- Prepare tables with name as today's date and columns: sr_no: int primary key auto increment, class: varchar(50), teacher: varchar(100), subject: varchar(100), title: varchar(100), description: text, 2001: boolean, 2002: boolean, 2003: boolean, ..., 2020: boolean
CREATE TABLE IF NOT EXISTS `2025-07-22` (
    sr_no INT AUTO_INCREMENT PRIMARY KEY,
    class VARCHAR(50),
    teacher_id VARCHAR(50),
    subject VARCHAR(100),
    title VARCHAR(100),
    description VARCHAR(500),
    due DATE,
    id2001 BOOLEAN DEFAULT FALSE,
    id2002 BOOLEAN DEFAULT FALSE,
    id2003 BOOLEAN DEFAULT FALSE,
    id2004 BOOLEAN DEFAULT FALSE,
    id2005 BOOLEAN DEFAULT FALSE,
    id2006 BOOLEAN DEFAULT FALSE,
    id2007 BOOLEAN DEFAULT FALSE,
    id2008 BOOLEAN DEFAULT FALSE,
    id2009 BOOLEAN DEFAULT FALSE,
    id2010 BOOLEAN DEFAULT FALSE,
    id2011 BOOLEAN DEFAULT FALSE,
    id2012 BOOLEAN DEFAULT FALSE,
    id2013 BOOLEAN DEFAULT FALSE,
    id2014 BOOLEAN DEFAULT FALSE,
    id2015 BOOLEAN DEFAULT FALSE,
    id2016 BOOLEAN DEFAULT FALSE,
    id2017 BOOLEAN DEFAULT FALSE,
    id2018 BOOLEAN DEFAULT FALSE,
    id2019 BOOLEAN DEFAULT FALSE,
    id2020 BOOLEAN DEFAULT FALSE
);

INSERT INTO `2025-07-18` (class, teacher_id, subject, title, description, due)
VALUES
('8A', '5001', 'Mathematics', 'Linear Equations', 'Solve all linear equations from chapter 4', '2025-07-26'),
('9B', '5002', 'Science', 'Lab Report', 'Submit the lab report on magnetism', '2025-07-27'),
('10C', '5003', 'English', 'Book Review', 'Write a review of the assigned novel', '2025-07-28'),
('11A', '5004', 'Hindi', 'Story Writing', 'Write a short story based on a given theme', '2025-07-29'),
('12B', '5005', 'Social Studies', 'Civics Assignment', 'Complete the worksheet on Indian Constitution', '2025-07-30'),
('8C', '5006', 'Marathi', 'Essay Writing', 'Write an essay on your favorite festival', '2025-07-31'),
('9A', '5007', 'Computer', 'Database Project', 'Design a simple student database in MySQL', '2025-08-01'),
('10B', '5008', 'Mathematics', 'Trigonometry Homework', 'Solve trigonometric identities from chapter 6', '2025-08-02'),
('11C', '5009', 'Science', 'Chemistry Worksheet', 'Complete the worksheet on acids and bases', '2025-08-03'),
('12A', '5010', 'English', 'Poetry Analysis', 'Analyze the poem discussed in class', '2025-08-04'),
('8A', '5001', 'Mathematics', 'Probability Assignment', 'Solve probability problems from workbook', '2025-08-06'),
('9B', '5002', 'Science', 'Biology Project', 'Prepare a project on plant cells', '2025-08-07'),
('10C', '5003', 'English', 'Letter Writing', 'Write a formal letter to the principal', '2025-08-08'),
('11A', '5004', 'Hindi', 'Grammar Exercises', 'Complete grammar exercises from chapter 2', '2025-08-09'),
('12B', '5005', 'Social Studies', 'Economics Assignment', 'Research on Indian economy trends', '2025-08-10'),
('8C', '5006', 'Marathi', 'Reading Comprehension', 'Answer questions based on the given passage', '2025-08-11'),
('9A', '5007', 'Computer', 'Python Quiz', 'Prepare for the Python basics quiz', '2025-08-12'),
('10B', '5008', 'Mathematics', 'Algebra Worksheet', 'Complete the algebra worksheet', '2025-08-13'),
('11C', '5009', 'Science', 'Physics Assignment', 'Write a report on Newton’s Laws', '2025-08-14'),
('12A', '5010', 'English', 'Creative Writing', 'Write a short story on friendship', '2025-08-15');

-- Add 20 different values to the table for 2025-07-21
INSERT INTO `2025-07-21` (class, teacher_id, subject, title, description, due)
VALUES
('8A', '5001', 'Mathematics', 'Geometry Assignment', 'Draw and label all types of triangles', '2025-07-29'),
('9B', '5002', 'Science', 'Physics Experiment', 'Document results of the pendulum experiment', '2025-07-30'),
('10C', '5003', 'English', 'Debate Preparation', 'Prepare arguments for the upcoming debate', '2025-07-31'),
('11A', '5004', 'Hindi', 'Translation Exercise', 'Translate the given passage to Hindi', '2025-08-01'),
('12B', '5005', 'Social Studies', 'Political Science Project', 'Make a chart on Indian political parties', '2025-08-02'),
('8C', '5006', 'Marathi', 'Grammar Worksheet', 'Complete the grammar worksheet', '2025-08-03'),
('9A', '5007', 'Computer', 'HTML Assignment', 'Create a webpage about your school', '2025-08-04'),
('10B', '5008', 'Mathematics', 'Statistics Homework', 'Solve problems on mean, median, mode', '2025-08-05'),
('11C', '5009', 'Science', 'Biology Worksheet', 'Label the parts of a plant cell', '2025-08-06'),
('12A', '5010', 'English', 'Essay Writing', 'Write an essay on technology in education', '2025-08-07'),
('8A', '5001', 'Mathematics', 'Number Systems', 'Complete exercises on rational numbers', '2025-08-09'),
('9B', '5002', 'Science', 'Chemistry Assignment', 'Write a report on chemical reactions', '2025-08-10'),
('10C', '5003', 'English', 'Reading Comprehension', 'Answer questions based on the passage', '2025-08-11'),
('11A', '5004', 'Hindi', 'Poetry Recitation', 'Prepare for poetry recitation contest', '2025-08-12'),
('12B', '5005', 'Social Studies', 'Geography Worksheet', 'Mark major rivers of India on a map', '2025-08-13'),
('8C', '5006', 'Marathi', 'Essay Writing', 'Write an essay on your favorite sport', '2025-08-14'),
('9A', '5007', 'Computer', 'Scratch Project', 'Create a simple animation in Scratch', '2025-08-15'),
('10B', '5008', 'Mathematics', 'Algebra Quiz', 'Prepare for the algebra quiz', '2025-08-16'),
('11C', '5009', 'Science', 'Physics Quiz', 'Revise for the quiz on electricity', '2025-08-17'),
('12A', '5010', 'English', 'Book Review', 'Write a review of a book you read', '2025-08-18');

-- Add 20 different values to the table for 2025-07-22
INSERT INTO `2025-07-22` (class, teacher_id, subject, title, description, due)
VALUES
('8A', '5001', 'Mathematics', 'Fractions Homework', 'Solve fraction problems from chapter 5', '2025-07-30'),
('9B', '5002', 'Science', 'Environmental Science Project', 'Prepare a poster on pollution', '2025-07-31'),
('10C', '5003', 'English', 'Speech Writing', 'Write a speech on climate change', '2025-08-01'),
('11A', '5004', 'Hindi', 'Essay Writing', 'Write an essay on your favorite author', '2025-08-02'),
('12B', '5005', 'Social Studies', 'History Timeline', 'Create a timeline of Indian freedom struggle', '2025-08-03'),
('8C', '5006', 'Marathi', 'Reading Assignment', 'Read the assigned story and summarize', '2025-08-04'),
('9A', '5007', 'Computer', 'JavaScript Basics', 'Write basic JavaScript programs', '2025-08-05'),
('10B', '5008', 'Mathematics', 'Measurement Assignment', 'Solve measurement problems from workbook', '2025-08-06'),
('11C', '5009', 'Science', 'Chemistry Quiz', 'Prepare for the quiz on acids and bases', '2025-08-07'),
('12A', '5010', 'English', 'Creative Writing', 'Write a poem about nature', '2025-08-08'),
('8A', '5001', 'Mathematics', 'Decimals Worksheet', 'Complete decimal exercises', '2025-08-10'),
('9B', '5002', 'Science', 'Physics Assignment', 'Write a report on simple machines', '2025-08-11'),
('10C', '5003', 'English', 'Book Analysis', 'Analyze the main character of the novel', '2025-08-12'),
('11A', '5004', 'Hindi', 'Grammar Quiz', 'Prepare for the grammar quiz', '2025-08-13'),
('12B', '5005', 'Social Studies', 'Economics Worksheet', 'Complete the worksheet on Indian economy', '2025-08-14'),
('8C', '5006', 'Marathi', 'Essay Writing', 'Write an essay on your favorite food', '2025-08-15'),
('9A', '5007', 'Computer', 'Python Project', 'Create a calculator in Python', '2025-08-16'),
('10B', '5008', 'Mathematics', 'Geometry Quiz', 'Prepare for the geometry quiz', '2025-08-17'),
('11C', '5009', 'Science', 'Biology Assignment', 'Write a report on photosynthesis', '2025-08-18'),
('12A', '5010', 'English', 'Letter Writing', 'Write a letter to your friend', '2025-08-19');

-- Add 20 different values to the table for 2025-07-23
INSERT INTO `2025-07-23` (class, teacher_id, subject, title, description, due)
VALUES
('8A', '5001', 'Mathematics', 'Multiplication Homework', 'Solve multiplication problems from chapter 2', '2025-07-31'),
('9B', '5002', 'Science', 'Physics Worksheet', 'Complete worksheet on force and motion', '2025-08-01'),
('10C', '5003', 'English', 'Essay Writing', 'Write an essay on your favorite hobby', '2025-08-02'),
('11A', '5004', 'Hindi', 'Story Analysis', 'Analyze the story from chapter 4', '2025-08-03'),
('12B', '5005', 'Social Studies', 'Geography Project', 'Prepare a project on Indian states', '2025-08-04'),
('8C', '5006', 'Marathi', 'Poetry Writing', 'Write a poem about your school', '2025-08-05'),
('9A', '5007', 'Computer', 'Scratch Animation', 'Create an animation in Scratch', '2025-08-06'),
('10B', '5008', 'Mathematics', 'Algebra Assignment', 'Solve algebra problems from workbook', '2025-08-07'),
('11C', '5009', 'Science', 'Chemistry Assignment', 'Write a report on chemical reactions', '2025-08-08'),
('12A', '5010', 'English', 'Book Review', 'Write a review of a classic novel', '2025-08-09'),
('8A', '5001', 'Mathematics', 'Division Worksheet', 'Complete division exercises', '2025-08-11'),
('9B', '5002', 'Science', 'Biology Quiz', 'Prepare for the biology quiz', '2025-08-12'),
('10C', '5003', 'English', 'Reading Comprehension', 'Answer questions based on the passage', '2025-08-13'),
('11A', '5004', 'Hindi', 'Essay Writing', 'Write an essay on your favorite place', '2025-08-14'),
('12B', '5005', 'Social Studies', 'Political Science Worksheet', 'Complete worksheet on Indian government', '2025-08-15'),
('8C', '5006', 'Marathi', 'Grammar Quiz', 'Prepare for the grammar quiz', '2025-08-16'),
('9A', '5007', 'Computer', 'Web Design Project', 'Design a homepage for a website', '2025-08-17'),
('10B', '5008', 'Mathematics', 'Statistics Quiz', 'Prepare for the statistics quiz', '2025-08-18'),
('11C', '5009', 'Science', 'Physics Project', 'Prepare a project on electricity', '2025-08-19'),
('12A', '5010', 'English', 'Creative Writing', 'Write a story about a memorable day', '2025-08-20');

INSERT INTO `2025-07-16` (class, teacher_id, subject, title, description,due)
VALUES 
('8A', '5001', 'Mathematics', 'Algebra Homework', 'Solve the problems on page 42', '2023-10-05'),
('9B', '5002', 'Science', 'Physics Assignment', 'Complete the experiments from chapter 5', '2023-10-06'),
('10C', '5003', 'English', 'Essay Writing', 'Write an essay on your favorite book', '2023-10-07'),
('11A', '5004', 'Hindi', 'Poetry Analysis', 'Analyze the poem from chapter 3', '2023-10-08'),
('12B', '5005', 'Social Studies', 'History Project', 'Prepare a project on Indian Independence', '2023-10-09'),
('8C', '5006', 'Marathi', 'Grammar Exercises', 'Complete the exercises in workbook', '2023-10-10'),
('9A', '5007', 'Computer', 'Programming Assignment', 'Write a program in Python', '2023-10-11'),
('10B', '5008', 'Mathematics', 'Geometry Problems', 'Solve the problems on page 50', '2023-10-12'),
('11C', '5009', 'Science', 'Biology Assignment', 'Research on human anatomy', '2023-10-13'),
('12A', '5010', 'English', 'Literature Review', 'Review the novel studied in class', '2023-10-14'),
('8A', '5001', 'Mathematics', 'Statistics Homework', 'Complete the exercises on data interpretation', '2023-10-15'),
('9B', '5002', 'Science', 'Chemistry Assignment', 'Complete the lab report on chemical reactions', '2023-10-16'),
('10C', '5003', 'English', 'Grammar Exercises', 'Complete the exercises in workbook', '2023-10-17'),
('11A', '5004', 'Hindi', 'Essay Writing', 'Write an essay on your favorite festival', '2023-10-18'),
('12B', '5005', 'Social Studies', 'Geography Project', 'Prepare a project on world geography', '2023-10-19'),
('8C', '5006', 'Marathi', 'Literature Review', 'Review the poem studied in class', '2023-10-20'),
('9A', '5007', 'Computer', 'Web Development Assignment', 'Create a simple webpage using HTML and CSS', '2023-10-21'),
('10B', '5008', 'Mathematics', 'Calculus Problems', 'Solve the problems on page 60 of the textbook', '2023-10-22'),
('11C', '5009', 'Science', 'Physics Project', 'Prepare a project on renewable energy sources', '2023-10-23'),
('12A', '5010', 'English', 'Creative Writing Assignment', 'Write a short story based on a given prompt.',  "2023-10-24");

-- Add 20 different values to the table with teachers names matching the class and subject
INSERT INTO `2023-07-17` (class, teacher_id, subject, title, description,due)
VALUES
('8A', '5001', 'Mathematics', 'Algebra Quiz', 'Prepare for the algebra quiz on Friday', '2023-10-05'),
('9B', '5002', 'Science', 'Physics Quiz', 'Revise chapter 5 for the quiz', '2023-10-06'),
('10C', '5003', 'English', 'Literature Quiz', 'Prepare for the literature quiz on Monday', '2023-10-07'),
('11A', '5004', 'Hindi', 'Grammar Quiz', 'Revise grammar rules for the quiz', '2023-10-08'),
('12B', '5005', 'Social Studies', 'History Quiz', 'Study the Indian Independence movement for the quiz', '2023-10-09'),
('8C', '5006', 'Marathi', 'Vocabulary Quiz', 'Learn new vocabulary words for the quiz', '2023-10-10'),
('9A', '5007', 'Computer', 'Programming Quiz', 'Revise Python basics for the quiz', '2023-10-11'),
('10B', '5008', 'Mathematics', 'Geometry Quiz', 'Prepare for the geometry quiz on Wednesday', '2023-10-12'),
('11C', '5009', 'Science', 'Biology Quiz', 'Revise human anatomy for the quiz on Thursday.',  "2023-10-13"),
('12A', '5010', 'English', 'Essay Writing Contest.',  "Write an essay on environmental conservation.",  "2023-10-14"),
('8A','5001','Mathematics','Statistics Quiz','Prepare for the statistics quiz next week.','2023-10-15'),
('9B','5002','Science','Chemistry Quiz','Revise chemical reactions for the quiz.','2023-10-16'),
('10C','5003','English','Grammar Quiz','Complete grammar exercises in workbook.','2023-10-17'),
('11A','5004','Hindi','Essay Writing Contest','Write an essay on your favorite festival.','2023-10-18'),
('12B','5005','Social Studies','Geography Quiz','Prepare for world geography quiz.','2023-10-19'),
('8C','5006','Marathi','Literature Review Assignment.','Review the poem studied in class.','2023-10-20'),
('9A','5007','Computer','Web Development Quiz','Create a simple webpage using HTML and CSS.','2023-10-21'),
('10B','5008','Mathematics','Calculus Quiz','Solve calculus problems on page 60 of the textbook.','2023-10-22'),
('11C','5009','Science','Physics Project Presentation.','Prepare a project on renewable energy sources.','2023-10-23'),
('12A','5010','English','Creative Writing Contest.','Write a short story based on a given prompt.','2023-10-24');

--create table for teachers
CREATE TABLE IF NOT EXISTS teachers (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    class VARCHAR(50),
    subject VARCHAR(100),
    address VARCHAR(500)
);

-- Insert teachers data into the teachers table
INSERT INTO teachers (id, name, class, subject, address) VALUES
('5001', 'Sunil Kulkarni', '8A', 'Mathematics', '10, Model Colony, Pune'),
('5002', 'Neha Joshi', '9B', 'Science', '22, Katraj, Pune'),
('5003', 'Amit Deshmukh', '10C', 'English', '35, Magarpatta, Pune'),
('5004', 'Priya Patil', '11A', 'Hindi', '47, Sinhagad Road, Pune'),
('5005', 'Rajesh Sharma', '12B', 'Social Studies', '59, Swargate, Pune'),
('5006', 'Sneha Pawar', '8C', 'Marathi', '63, Wanowrie, Pune'),
('5007', 'Anil More', '9A', 'Computer', '74, Vishrantwadi, Pune'),
('5008', 'Meera Singh', '10B', 'Mathematics', '88, Bavdhan, Pune'),
('5009', 'Suresh Verma', '11C', 'Science', '91, Dhayari, Pune'),
('5010', 'Kavita Kulkarni', '12A', 'English', '104, Karve Nagar, Pune');

-- Create a table for students
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    class VARCHAR(50),
    address VARCHAR(200)
);

-- Insert students data into the students table
INSERT INTO students (id, name, dob, class, address) VALUES
(2001, 'Kiran Salunke', '2010-05-14', '8A', '301, Dhayari, Pune'),
(2002, 'Priya Singh', '2011-08-22', '9B', '45, Kothrud, Pune'),
(2003, 'Rahul Verma', '2010-12-03', '8A', '78, Hadapsar, Pune'),
(2004, 'Sneha Patel', '2011-03-17', '10C', '33, Viman Nagar, Pune'),
(2005, 'Vikram Joshi', '2010-09-29', '9B', '56, Koregaon Park, Pune'),
(2006, 'Riya Kulkarni', '2011-01-11', '8A', '101, Baner, Pune'),
(2007, 'Arjun Deshmukh', '2010-07-25', '10C', '202, Camp, Pune'),
(2008, 'Meera Pawar', '2011-04-19', '9B', '303, Aundh, Pune'),
(2009, 'Sahil Patil', '2010-11-30', '8A', '404, Erandwane, Pune'),
(2010, 'Tanvi More', '2011-06-05', '10C', '505, Pashan, Pune'),
(2011, 'Rohan Desai', '2009-03-21', '8A', '201, Baner, Pune'),
(2012, 'Simran Kaur', '2008-07-15', '9B', '212, Kothrud, Pune'),
(2013, 'Aditya Patil', '2007-11-09', '10C', '223, Hadapsar, Pune'),
(2014, 'Pooja Joshi', '2006-02-28', '11A', '234, Viman Nagar, Pune'),
(2015, 'Manav Sharma', '2005-05-17', '12B', '245, Camp, Pune'),
(2016, 'Isha Kulkarni', '2009-09-03', '8C',  "256, Aundh, Pune"),
(2017, "Yash Pawar", '2008-12-25', '9A', '267, Erandwane, Pune'),
(2018, 'Snehal More', '2007-06-14', '10B', '278, Shivaji Nagar, Pune'),
(2019, 'Aman Verma', '2006-10-30', '11C', '289, Bavdhan, Pune'),
(2020, 'Tanisha Shinde', '2005-01-19', '12A', '290, Kalyani Nagar, Pune');