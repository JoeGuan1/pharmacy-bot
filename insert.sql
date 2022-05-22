-- Script name: inserts.sql
-- Author:      Joe Guan
-- Purpose:     Insert sample data to test the integrity of this database system
   
-- the database used to insert the data into.
-- USE PharmacyManagementDB
USE sql3492830; 
   
-- Role table inserts
INSERT INTO Role (Role_ID, Role_Type, Permissions) VALUES (1, 'Employee', 'Update'), (2, 'Doctor', 'Create'), (3, 'Manager', 'Assign');

-- SELECT * FROM Role;

-- User table inserts
INSERT INTO User (User_ID, First_Name, Last_Name, SSN) 
VALUES (1, 'Anthony', 'Smith', '123456789'), (2, 'Amy', 'Parker', '223456789'), (3, 'Bobby', 'Kim', '323456789'),
(4, 'Steve', 'Smith', '423456789'), (5, 'Rachel', 'Kwan', '523456789'), (6, 'Alice', 'Curry', '623456789'), 
(7, 'James', 'Kim', '723456789'), (8, 'Andrew', 'Parker', '823456789'), (9, 'Sam', 'Harben', '923456789'),
(10, 'James', 'Kwan', '723456798'), (11, 'Charlie', 'Parker', '823456798'), (12, 'Mac', 'Apple', '923456798');

-- SELECT * FROM User;

-- Employee table inserts
INSERT INTO Employee (Employee_ID, User_ID, First_Name, Last_Name, Role_ID) 
VALUES (1, 1, 'Anthony', 'Smith', '1'), (2, 2, 'Amy', 'Parker', '2'), (3, 4, 'Steve', 'Smith', '1'),
(4, 5, 'Rachel', 'Kwan', '2'),  (5, 7, 'James', 'Kim', '1'), (6, 8, 'Andrew', 'Parker', '2'),
(7, 10, 'James', 'Kwan', 2), (8, 11, 'Charlie', 'Parker', 2), (9, 12, 'Mac', 'Apple', 1);

-- SELECT * FROM Employee;

-- Clinic table inserts
INSERT INTO Clinic (Clinic_ID, Clinic_Name, Clinic_Address, Contact_Number, Primary_Doctor) 
VALUES (1, 'Safety One', '123 First St', '415-826-9109', 'Adam Smith'), (2, 'Health One', '432 Second St', '415-672-3203', 'Angel Nham'),
(3, 'Carbon One', '243 Third St', '415-278-3902', 'Nancy Yim'), (4, 'Clinic One', '532 Fourth St', '321-646-3203', 'Adam Nham');

-- SELECT * FROM Clinic;

-- Doctor table inserts
INSERT INTO Doctor (Doctor_ID, Employee_ID, First_Name, Last_Name, Role_ID) 
VALUES (1, 2, 'Amy', 'Parker', 2), (2, 4, 'Rachel', 'Kwan', 2),
(3, 6, 'Andrew', 'Parker', 2), (4, 7, 'James', 'Kwan', 2), (5, 8, 'Charlie', 'Parker', 2);

-- SELECT * FROM Doctor;

-- Manager table inserts
INSERT INTO Manager (Manager_ID, User_ID, First_Name, Last_Name, Role_ID) 
VALUES (1, 3, 'Bobby', 'Kim', 3), (2, 6, 'Alice', 'Curry', 3), (3, 9, 'Sam', 'Harben', 3);

-- SELECT * FROM Manager;

-- Payment_Method table inserts
INSERT INTO Payment_Method (Payment_Method_ID, Payment_Type, Total_Number) 
VALUES (1, 'PayPal', 4), (2, 'Bank Account', 8);

-- SELECT * FROM Payment_Method;

-- Region table inserts
INSERT INTO Region (Region_ID, Region_Name, Coverage) 
VALUES (1, 'San Fransico County', 'Medi-Cal'), (2, 'Los Angles County','Red-Cross'), (3, 'Fresno County', 'Kaiser');

-- SELECT * FROM Region;

-- Medical Insurance table inserts
INSERT INTO Medical_Insurance (Medical_Insurance_ID, Insurance_Name, Phone_Number, Region_ID) 
VALUES (1, 'Medi-One', '478-283-4800', 1),
(2, 'Red-One', '023-950-9024', 2),
(3, 'Medi-Two', '913-828-3290', 3),
(4, 'Blue-One', '394-2793-9952', 3),
(5, 'Green-One', '394-792-0832', 1),
(6, 'Black-One', '657-980-9234', 3);

-- SELECT * FROM Medical_Insurance;

-- Patient table inserts
INSERT INTO Patient (Patient_ID, SSN, Clinic_ID, First_Name, Last_Name, DOB, Phone_Number, Doctor_ID, Payment_Method_ID, Medical_Insurance_ID) 
VALUES (1, 098765432, 1, 'John', 'Roberts', 19980510, '672-425-7843',2, 1,3), (2, 987654321, 3, 'Lucy', 'Le', 19860813, '782-948-9723',5,2,1),
(3,908765432, NULL, 'Lily', 'Feng', 19760301, '782-782-6502', 5,2,2), (4, '328694302', 4 ,'Jane', 'Black', 20000617, '378-238-8023',3, 2,4), 
(5, 479203485, NULL, 'Jack', 'Black', 19930824, '379-283-1902', 3, 1,1), (6, 378205092, 2, 'Jill', 'Blue', 20021204, '425-983-8853',2,1,NULL), 
(7, 792034745, 4, 'Sam', 'Smith', 19800409, '893-234-5234',4,2,NULL), (8, 730571945, 2, 'Blake','Black', 19990817, '792-579-2783',1,2,1),
(9, 890283574, NULL, 'Jess', 'Blue', 19670308, '783-873-4752', 1,2,4), (10, 743903284, NULL, 'Josh', 'Kim', 19780314, '478-293-5892',2,2,3),
(11, 750372802, 3, 'Sam', 'Le', 19890710, '390-283-5743',4, 1,2), (12, 389204758, 2, 'David', 'Kang', 19860925, '578-387-4682', 4,1,5);

-- SELECT * FROM Patient;

-- PayPal table inserts
INSERT INTO PayPal (PayPal_ID, PayPal_Name, Email, Payment_Method_ID, SSN)
VALUES (1, 'JohnRoberts1', 'JR@mgail.com', 1, 098765432), (2, 'JackBlack','JB@mgail.com', 1, 479203485),
(3, 'SamLe','SL@mgail.com', 1, 750372802), (4, 'DavidKang','DK@mgail.com', 1, 389204758);

-- SELECT * FROM PayPal;

-- Credit_Card table inserts
INSERT INTO Credit_Card (Credit_ID, Credit_Card_Number, Billing_Address, Mailing_Address)
VALUES (1, '1098123290290345', '832 Fourth St', '832 Fourth St'), (2, '2098340290003823', '835 Fourth St', '835 Fourth St'),
(3, '3092329089203485', '932 Fourth St', '932 Fourth St'), (4, '8093729385802347', '293 Fifth St', '293 Fifth St'),
(5, '3902840237459892', '023 Mission St', '023 Mission St'), (6, '9032795365934723', '903 Mission St', '903 Mission St');

-- SELECT * FROM Credit_Card;

-- Debit_Card table inserts
INSERT INTO Debit_Card (Debit_ID, Debit_Card_Number, Billing_Address, Mailing_Address)
VALUES (1, '4094029089324573', '832 Third St', '832 Third St'), (2, '6098029092304824', '832 Fourth St', '832 Fourth St'),
(3, '3814029038950234', '835 Fourth St', '835 Fourth St'), (4, '8429748593203756', '903 Mission St','903 Mission St'),
(5, '8923758478256310', '893 Sachs St', '893 Sachs St');

-- SELECT * FROM Debit_Card;

-- Bank_Account table inserts
INSERT INTO Bank_Account (Bank_Account_ID, First_Name, Last_Name, SSN, Bank_Name, Payment_Method_ID, Credit_ID, Debit_ID)
VALUES (1, 'Lucy', 'Le', 987654321, 'Bank of America', 2, NULL, 1), (2, 'Lily', 'Feng', 908765432, 'Wells Fargo',2, 1, 2),
(3, 'Jane', 'Black', 328694302, 'Bank of America', 2, 2, 3), (4, 'Jill', 'Blue', 378205092, 'Chase', 2, 3, NULL),
(5, 'Sam', 'Smith', 792034745, 'Wells Fargo', 2, 4, NULL), (6, 'Blake','Black', 730571945, 'Bank of America', 2, 5, NULL),
(7, 'Jess', 'Blue', 890283574, 'Chase', 2, 6, 4), (8, 'Josh', 'Kim',743903284, 'Bank of America', 2 , NULL, 5);

-- SELECT * FROM Bank_Account;

-- Supplier table inserts
INSERT INTO Supplier (Supplier_ID, Supplier_Name, Contact_Number) 
VALUES (1, 'Vitality Medical', '134-345-7933'),(2, 'Save Rite Medical', '223-904-2835'),
(3, 'Home Care Delivered', '390-349-1245'), (4, 'Allegro Medical', '489-390-5489');

-- SELECT * FROM Supplier;

-- Medication_File table inserts
INSERT INTO Medication_File (Medication_File_ID, Medication_Name, Supplier_ID) 
VALUES (1, 'Atorvastatin', 3), (2, 'Metformin', 2), (3, 'Lisinopril', 2),
(4, 'Levothyroxine', 4), (5, 'Amoxicillin', 1), (6, 'Albuterol', 4);

-- SELECT * FROM Medication_File;

-- Billing_Information table inserts
INSERT INTO Billing_Information (Billing_Info_ID, First_Name, Last_Name, Cost, Medication_Name, Paid) 
VALUES (1, 'John', 'Roberts', 50.00, 'Atorvastatin', 1), (2, 'Lucy', 'Le', 30.50, 'Metformin', 0), (3, 'Lily', 'Feng', 20.00, 'Lisinopril', 1),
(4, 'Jane', 'Black', 80.00, 'Levothyroxine', 0), (5, 'Jack', 'Black', 25.00, 'Amoxicillin', 1), (6, 'Jill', 'Blue', 25.00, 'Lisinopril', 1),
(7, 'Sam', 'Smith', 40.00, 'Atorvastatin', 0),(8, 'Blake', 'Black', 70.00, 'Levothyroxine', 1), (9, 'Jess', 'Blue', 30.00, 'Albuterol', 0),
(10, 'Josh', 'Kim', 60.00, 'Levothyroxine', 1), (11, 'Sam', 'Le', 25.00, 'Amoxicillin', 0), (12, 'David', 'Kang', 30.00, 'Albuterol', 0);

-- SELECT * FROM Billing_Information;

-- Medication_Plan table inserts
INSERT INTO Medication_Plan (Medication_Plan_ID, First_Name, Last_Name, Dosage, Deration_Of_Plan, Active, Paid, Medication_File_ID, Billing_Info_ID) 
VALUES (1, 'John', 'Roberts', 'Once a Day', '10 Months', 0, 1, 1, 1), (2, 'Lucy', 'Le', '1-3 Times a Day', '8 Months', 1, 0, 2, 2),
(3, 'Lily', 'Feng', 'Once a Day', '10 Months', 1, 1, 3, 3), (4, 'Jane', 'Black', 'Once 30 Minutes - 1 Hour Before Breakfast', '10 Months', 1, 0, 4, 4),
(5, 'Jack', 'Black', 'Every 8 or 12 Hours', '6 Months', 0, 1, 5, 5), (6, 'Jill', 'Blue', 'Once a Day', '1 Year', 0, 1, 4, 6),
(7, 'Sam', 'Smith', 'Once a Day', '8 Months', 1, 0, 1, 7),(8, 'Blake', 'Black', 'Once 30 Minutes - 1 Hour Before Breakfast', '8 Months', 0, 1, 4, 8),
(9, 'Jess', 'Blue','4-6 Hours as Needed', '1 Year', 1, 0, 6, 9), (10, 'Josh', 'Kim', 'Once 30 Minutes - 1 Hour Before Breakfast', '9 Months', 1, 1, 4, 10),
(11, 'Sam', 'Le', 'Every 8 or 12 Hours', '6 Months', 1, 0, 5, 11), (12, 'David', 'Kang', '4-6 Hours as Needed', '1 Year', 1, 0, 6, 12);

-- SELECT * FROM Medication_Plan;

-- Patient_File table inserts
INSERT INTO Patient_File (Patient_File_ID, Patient_ID, Medication_Plan_ID) 
VALUES (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6),(7, 7, 7), (8, 8, 8), (9, 9, 9), (10, 10, 10), (11, 11, 11) ,(12, 12, 12);

-- SELECT * FROM Patient_File;

-- Inventory table inserts
INSERT INTO Inventory (Inventory_ID, Medication_Name, Total_Stock, Medication_File_ID) 
VALUES (1, 'Atorvastatin', 150, 1), (2, 'Metformin', 100, 2), (3, 'Lisinopril', 50, 3),
(4, 'Levothyroxine', 225, 4), (5, 'Amoxicillin', 185, 5), (6, 'Albuterol', 75, 6);

-- SELECT * FROM Inventory;
