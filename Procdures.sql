-- The procedure I was to help create my bot commands

USE sql3492830;

DROP PROCEDURE IF EXISTS DocPatient;

DELIMITER $$
CREATE PROCEDURE DocPatient (IN check_ID INT, OUT doc_name VARCHAR(100), OUT people VARCHAR(250))
    BEGIN 
		DECLARE first_name VARCHAR(100);
        DECLARE last_name VARCHAR(100);
        SET first_name = (SELECT doc.First_Name FROM Doctor doc WHERE doc.Doctor_ID = check_ID);
        SET last_name = (SELECT doc.Last_Name FROM Doctor doc WHERE doc.Doctor_ID = check_ID);
        SELECT CONCAT (first_name, " ", last_name) AS full_doc;
        SET doc_name = full_doc;
        SELECT CONCAT (patient.First_Name, " ", patient.Last_Name) AS patients
        FROM Patient patient
        JOIN Doctor doc ON patient.Doctor_ID = doc.Doctor_ID
        WHERE doc.Doctor_ID = check_ID;
        SET people = patients;
	END$$


-- 9
DROP PROCEDURE IF EXISTS PaymentPatientAvg;

CREATE PROCEDURE PaymentPatientAvg (IN paymentType VARCHAR(100), OUT average FLOAT)
    BEGIN 
    DECLARE payment_ID INT;
    DECLARE totalPatients INT;
        SET payment_ID = (SELECT Payment_Method_ID FROM Payment_Method WHERE Payment_Method.Payment_Type = paymentType);
        SET totalPatients = (SELECT COUNT(patients.Payment_Method_ID) 
        FROM Patient patients 
        JOIN Payment_Method payment_method ON payment_method.Payment_Method_ID = patients.Payment_Method_ID);
        SET average = (SELECT totalPatients/Total_Number FROM Payment_Method WHERE Payment_Method.Payment_Type = paymentType);
	END$$
DELIMITER ;
SELECT @avg;
CALL PaymentPatientAvg('Paypal', @avg);

-- 1
DELIMITER $$
CREATE PROCEDURE SupplyMedicationCheck (IN check_ID INT, OUT supplier_name VARCHAR(100), OUT counter INT)
    BEGIN 
        SET supplier_name = (SELECT supplier.Supplier_Name FROM Supplier supplier WHERE supplier.Supplier_ID = check_ID);
        SET counter = (SELECT COUNT(files.Medication_File_ID) 
        FROM Medication_File files 
        JOIN Supplier supplier ON supplier.supplier_ID = files.supplier_ID
        WHERE supplier.supplier_ID = check_ID);
	END$$
DELIMITER ; 

-- 4
DELIMITER $$
CREATE PROCEDURE InsuranceRegion (IN check_ID INT, OUT region_name VARCHAR(100), OUT counter INT)
    BEGIN 
        SET region_name = (SELECT region.Region_Name FROM Region region WHERE region.Region_ID = check_ID);
        SET counter = (SELECT COUNT(insurance.Medical_Insurance_ID) 
        FROM Medical_Insurance insurance
        JOIN Region region ON region.Region_ID = insurance.Region_ID
        WHERE region.Region_ID = check_ID);
	END$$
DELIMITER ;

-- 13
DELIMITER $$
CREATE PROCEDURE ClinicPatitents (IN check_ID INT, OUT clinic_name VARCHAR(100), OUT counter INT)
    BEGIN 
        SET clinic_name = (SELECT clinic.Clinic_Name FROM Clinic clinic WHERE clinic.Clinic_ID = check_ID);
        SET counter = (SELECT COUNT(patients.Patient_ID) 
        FROM Patient patients
        JOIN Clinic clinic ON clinic.Clinic_ID = patients.Clinic_ID
        WHERE clinic.Clinic_ID = check_ID);
	END$$
DELIMITER ;

-- 17
DELIMITER $$
CREATE PROCEDURE RegionPatitents (IN check_ID INT, OUT region_name VARCHAR(100), OUT counter INT)
    BEGIN 
        SET region_name = (SELECT region.Region_Name FROM Region region WHERE region.Region_ID = check_ID);
        SET counter = (SELECT COUNT(patients.Patient_ID) 
        FROM Patient patients
        JOIN Medical_Insurance insurance on patients.Medical_Insurance_ID = insurance.Medical_Insurance_ID
        JOIN Region region ON region.Region_ID = insurance.Region_ID
        WHERE region.Region_ID = check_ID);
	END$$
DELIMITER ;

-- 12
DELIMITER $$
CREATE PROCEDURE InsertFile (IN medication_name VARCHAR(250), IN supplier_id INT)
    BEGIN 
		DECLARE medication_id INT;
        INSERT INTO Medication_File (Medication_Name, Supplier_ID)
        VALUES (medication_name, supplier_ID);
		
        SET medication_id = (SELECT medication.Medication_File_ID FROM Medication_File medication WHERE medication.Medication_Name = medication_name);
        
        INSERT INTO Inventory (Medication_Name, Total_Stock, Medication_File_ID)
        VALUES (medication_name, 0, medication_id);
        
	END$$
DELIMITER ;

-- SELECT FROM Supplier
