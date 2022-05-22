This bot is built to run commands that are based off of businesses rules for a pharmacy management database. Each business rule has a command associated with it and the bot will run qurieres to the database from the command that is given.


Business Rules and Bot Commands:

 1. For each supplier, find the number of medication files they are linked with

 Command: $supplycheck

 Prints each supplier's name and how many medication files they are link with

2. For each medication file, find the suppliers they are linked with and print the supplier's name and contact number

 Command: $medicationcontact

Prints each medication file's name and it's supplier's name and contact number

3. For each medical insurance, list all the patients that have that insurance

 Command: $insurance <insurance name>

Prints the name of the insurance entered and lists all the patients who have this insurance
e.g: $insurance Medi-One

4. Find the number of medical insurance in the same region

 Command: $insuranceperregion
 
Prints the name of each region and the number of insurances that are within that region

5. List all of the doctors from employees

Command: $doctors
 
Prints the name of each doctor from the employee's list

6. For each medication file in inventory, list the total stock of each medication file

 Command: $inventorystock

Prints the name of each medication file and it's total stock from the inventory's list

7. For each medication file in inventory, list each medication file that has a higher total stock than the number entered.

 Command: $inventorystock <number>

 Prints the name of each medication file and it's total stock from the inventory's list that's higher than the number entered (meaning entering 50 prints all medication file name whose total stock is 51 or higher)
e.g: $inventorystock 50

8. Find the number of patients who have a specific payment method

 Command: $patientpayment <payment_type>

 Prints the payment type entered and the number of patients who has this payment type (Only supported payment type are Paypal and Bank_Account)
e.g: $patientpayment Bank_Account

9. For each payment method, find the average of patients with that payment

 Command:$averagepayment <payment_type>

 Prints the payment type entered and the average number of patients who has this payment type (Only supported payment type are Paypal and Bank_Account)
e.g: $averagepayment Bank Account

10. Find the number of patients who have a certain medication name listed in their medication plan

 Command: $patientmedication <medication_name>

 Prints the medication name entered and the number of patients who have that medication name in their medication plan
e.g: $patientmedication Atorvastatin

11. Find the number of medication plans that list a certain medication name

 Command: $planfile <medication_name>

 Prints the medication name entered and the number of medication plans who use the medication
e.g: $planfile Metformin

12. Update the inventory table automatically with a new medication file whenever a medication file is inserted.

 Command: $insertmedication <medication_name> <supply_id>

 Takes the medication name and supply id and inserts it into the medication_file table. Then the medication name is inserted into the inventory table with a total stock of 0 and prints out the medication name and total stock that was just inserted into memory (if the supplier id does not exist with the supplier table, then the command won't do anything)
e.g: $insertmedication Amlodipine 4

13. For each clinic, find the number of patients.

 Command: $clinicpatients

 Prints out the name of each clinic and the number of patients that come from those clinics
 
14. Create a function that returns the medication plan for a patient.

 Command: $plan <patient_SSN>

 Prints the entire medication plan of the patient's SSN that was entered
e.g: $plan 328694302

15. Find the number of patients that have an active medication plan

 Command: $activeplan

 Prints the number of patients with an active medication plan

16. Find the number of patients that have a paid billing information

 Command: $paidplan

 Prints the number of the patients with a paid billing information

17. Create a function that returns the number of patients for each region of medical insurance.

 Command: $patientsperregion

 Prints the name of each region and the number of patients who have insurance with the region

18. For each doctor, list all of the patients they oversee.

 Command: $doctorpatient

 Prints the name of each doctor and the names of the patients that are under each doctor 

