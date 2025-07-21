-- Prepare tables with name as today's date and columns: sr_no: int primary key auto increment, class: varchar(50), teacher: varchar(100), subject: varchar(100), title: varchar(100), description: text, 2001: boolean, 2002: boolean, 2003: boolean, ..., 2020: boolean
CREATE TABLE IF NOT EXISTS `2023-10-01` (
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

--List of students for reference:
/* id,name,DOB,class,address
2001,"Kiran Salunke",2010-05-14,8A,"301, Dhayari, Pune"
2002,"Priya Singh",2011-08-22,9B,"45, Kothrud, Pune"
2003,"Rahul Verma",2010-12-03,8A,"78, Hadapsar, Pune"
2004,"Sneha Patel",2011-03-17,10C,"33, Viman Nagar, Pune"
2005,"Vikram Joshi",2010-09-29,9B,"56, Koregaon Park, Pune"
2006,"Riya Kulkarni",2011-01-11,8A,"101, Baner, Pune"
2007,"Arjun Deshmukh",2010-07-25,10C,"202, Camp, Pune"
2008,"Meera Pawar",2011-04-19,9B,"303, Aundh, Pune"
2009,"Sahil Patil",2010-11-30,8A,"404, Erandwane, Pune"
2010,"Tanvi More",2011-06-05,10C,"505, Pashan, Pune"
2011,"Rohan Desai",2009-03-21,8A,"201, Baner, Pune"
2012,"Simran Kaur",2008-07-15,9B,"212, Kothrud, Pune"
2013,"Aditya Patil",2007-11-09,10C,"223, Hadapsar, Pune"
2014,"Pooja Joshi",2006-02-28,11A,"234, Viman Nagar, Pune"
2015,"Manav Sharma",2005-05-17,12B,"245, Camp, Pune"
2016,"Isha Kulkarni",2009-09-03,8C,"256, Aundh, Pune"
2017,"Yash Pawar",2008-12-25,9A,"267, Erandwane, Pune"
2018,"Snehal More",2007-06-14,10B,"278, Shivaji Nagar, Pune"
2019,"Aman Verma",2006-10-30,11C,"289, Bavdhan, Pune"
2020,"Tanisha Shinde",2005-01-19,12A,"290, Kalyani Nagar, Pune" */

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

-- Add 20 values to the table with teachers names matching the class and subject
INSERT INTO `2023-10-01` (class, teacher_id, subject, title, description,due)
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
