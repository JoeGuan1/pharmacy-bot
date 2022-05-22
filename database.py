# database.py
# This files has the implemention of the bot commands and of the queries givens to the databse to run the commands.
# Handles all the methods interacting with the database of the application.
# Students must implement their own methods here to meet the project requirements.

import os
import pymysql.cursors

db_host = os.environ['DB_HOST']
db_username = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']


def connect():
    try:
        conn = pymysql.connect(host=db_host,
                               port=3306,
                               user=db_username,
                               password=db_password,
                               db=db_name,
                               charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        print("Bot connected to database {}".format(db_name))
        return conn
    except:
        print("Bot failed to create a connection with your database because your secret environment variables " +
              "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
        print("\n")

# your code here

def response (msg):
  db_response = None;
  command_parts = msg.split();
  bot_command = command_parts[0]

  if '$activeplan' in bot_command:
    db_response = active()
    return db_response
  
  elif '$averagepayment' in bot_command:
    payment_name = command_parts[1]
    db_response = avgpay(payment_name)
    return db_response

  elif '$clinicpatients' in bot_command:
    db_response = clinicpatients()
    return db_response

  elif '$doctorpatient' in bot_command:
    db_response = docpatient()
    return db_response
  
  elif '$doctors' in bot_command:
    db_response = doctor()
    return db_response

  elif '$planfile' in bot_command:
    medication_name = command_parts[1]
    db_response = planfile(medication_name)
    return db_response

  elif '$insertmedication' in bot_command:
    medication_name = command_parts[1]
    supplier = command_parts[2]
    db_response = insertmedication(medication_name, supplier)
    return db_response
    
  elif '$insuranceperregion' in bot_command:
    db_response = insuranceregion()
    return db_response
  
  elif '$insurance' in bot_command:
    insurance = command_parts[1]
    db_response = insurancepatient(insurance)
    return db_response
    
  elif '$inventorystock' in bot_command:
    if len(command_parts) == 2:
      check = command_parts[1]
      db_response = check_stock(check)
    else:
      db_response = total_stock()
    return db_response  
    
  elif '$medicationcontact' in bot_command:
    db_response = medication_supplier_list()
    return db_response

  elif '$patientmedication' in bot_command:
    medication_name = command_parts[1]
    db_response = medicationpatients(medication_name)
    return db_response

  elif '$patientsperregion' in bot_command:
    db_response = regionpatient()
    return db_response
  
  elif '$patientpayment' in bot_command:
    payment_method = command_parts[1]
    db_response = paymentpatients(payment_method)
    return db_response

  elif '$paidplan' in bot_command:
    db_response = paid()
    return db_response
  
  elif '$plan' in bot_command:
    SSN = command_parts[1]
    db_response = plan(SSN)
    return db_response

  elif '$supplycheck' in bot_command:
    db_response = supplycheck()
    return db_response

#Finished #15
def active ():
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT COUNT(pfile.Patient_ID) AS COUNTER
    FROM Patient_File pfile
    JOIN Medication_Plan plan ON pfile.Medication_Plan_ID =      plan.Medication_Plan_ID 
    WHERE plan.Active = 1;"""
    cursor.execute(query)
    results = cursor.fetchall()
    result = []
    for count in results:
      total = count["COUNTER"]
      result.append(total)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
  active = str(result[0])
  statement = "The number of patients with an active medication plan are " + active + ".\n"
  return statement

#Finished #9
def avgpay (payment_name):
  result = None
  payment_type = payment_name.title()
  try: 
    connection = connect()
    cursor = connection.cursor()
    query = """CALL PaymentPatientAvg(%s, @avg);"""
    variables = (payment_type)
    cursor.execute(query,variables)
    cursor.execute("SELECT @avg")
    connection.commit()
    results = cursor.fetchall()
    result = []
    for avg in results:
      average = avg['@avg']
    result.append(average)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
  average = str(result[0])
  statement = "The average number of people with a payment type of " + payment_type + " are " + average + ".\n"
  return statement

#Finished #7
def check_stock(limit):
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT medication.Medication_Name, inventory.Total_Stock
FROM Medication_File medication
JOIN Inventory inventory ON medication.Medication_File_ID = inventory.Medication_File_ID
    WHERE inventory.Total_Stock > %s;"""
    variables = (limit)
    cursor.execute(query, variables)
    #cursor.comit()
    results = cursor.fetchall()
    result = []
    statement = None
    for medication in results:
      medication_name = medication["Medication_Name"]
      total_stock = medication["Total_Stock"]
      temp_stock = str(total_stock)
      statement = "Medication Name: " + medication_name + ", Total Stock: " + temp_stock + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp
  return final_print

#Finished #13
def clinicpatients():
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    count = 1
    result = []
    while True:
      query = """CALL ClinicPatitents(%s, @name,@counter);"""
      variables = (count)
      cursor.execute(query,variables)
      cursor.execute("SELECT @name")
      connection.commit()
      results = cursor.fetchall()
      name = None
      for clinic in results:
        name = clinic['@name']
      cursor.execute("SELECT @counter")
      results = cursor.fetchall()
      counter = None
      for clinic in results:
        counter = clinic['@counter']
      if name == None or counter == None:
        break
      else:
        temp_counter = str(counter)
        statement = "Clinic Name: " + name + ", Number of Patients: " + temp_counter + "\n"
        result.append(statement)
        count = count + 1

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()

  final_print = ""
  for temp in result:
    final_print = final_print + temp
  return final_print

#Finished #18
def docpatient():
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    count = 1
    result = []
    while True:
      query = """SELECT doc.First_Name, doc.Last_Name
      FROM Doctor doc WHERE doc.Doctor_ID = %s;"""
      variables = (count)
      cursor.execute(query,variables)
      results = cursor.fetchall()
      doc_name = None
      for doc in results:
        first = doc['First_Name']
        last = doc['Last_Name']
        doc_name = first + " " + last
      if doc_name == None:
        break
      query = """SELECT patient.First_Name, patient.Last_Name
      FROM Patient patient
      JOIN Doctor doc ON patient.Doctor_ID = doc.Doctor_ID
      WHERE patient.Doctor_ID = %s;"""
      cursor.execute(query,variables)
      connection.commit()
      results = cursor.fetchall()
      patient_names = ""
      for patients in results:
        first = patients['First_Name']
        last = patients['Last_Name']
        full = first + " " + last
        patient_names = patient_names + full + ", "
      statement = "Doctor: " + doc_name + ", List of Patients: " + patient_names + "\n"
      result.append(statement)
      count = count + 1

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print
    
#Finished #5
def doctor ():
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT employee.First_Name, employee.Last_Name
FROM Employee employee
JOIN Doctor doctor on employee.Employee_ID = doctor.Employee_ID;"""
    cursor.execute(query)
    #cursor.comit()
    results = cursor.fetchall()
    result = []
    for doctor in results:
      first_name = doctor["First_Name"]
      last_name = doctor["Last_Name"]
      full_name = first_name + ' ' + last_name
      statement = "Doctor " + full_name + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print

#Finished #12
def insertmedication(medication_name, supplierID):
  result = None
  medication = medication_name
  supplier = supplierID
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    result = []
    query = """CALL InsertFile(%s, %s);"""
    variables = (medication, supplier)
    cursor.execute(query,variables)
    query = """SELECT inventory.Medication_Name, inventory.Total_Stock FROM Inventory inventory WHERE inventory.Medication_Name = %s"""
    cursor.execute(query,(medication))
    connection.commit()
    results = cursor.fetchall()
    for inventory in results:
      name = inventory['Medication_Name']
      stock = inventory['Total_Stock']
      temp_stock = str(stock)
      statement = "Medication Name: " + name + ", Total Stock: " + temp_stock + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print
  
#Finished #3
def insurancepatient (insurance_name):
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    query = """SELECT patient.First_Name, patient.Last_Name
FROM Patient patient
JOIN Medical_Insurance insurance on patient.Medical_Insurance_ID = insurance.Medical_Insurance_ID
WHERE insurance.Insurance_Name = %s;"""
    variables = (insurance_name)
    cursor.execute(query, variables)
    connection.commit();
    results = cursor.fetchall()
    result = []
    for name in results:
      first = name["First_Name"]
      last = name["Last_Name"]
      full = first + " " + last
      result.append(full)
  
  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
  
  final_print = ""
  for temp in result:
    final_print = final_print + temp + ", "
  final_print = "Patients who have " + insurance_name.title() + " are " + final_print
  return final_print

#Finished #4
def insuranceregion():
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    count = 1
    result = []
    while True:
      query = """CALL InsuranceRegion(%s, @name,@counter);"""
      variables = (count)
      cursor.execute(query,variables)
      cursor.execute("SELECT @name")
      connection.commit()
      results = cursor.fetchall()
      name = None
      for region in results:
        name = region['@name']
      cursor.execute("SELECT @counter")
      results = cursor.fetchall()
      counter = None
      for region in results:
        counter = region['@counter']
      if name == None or counter == None:
        break
      else:
        temp_counter = str(counter)
        statement = "Region: " + name + ", Total Number of Insurance Within Region: " + temp_counter + "\n"
        result.append(statement)
        count = count + 1

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print

#Finished #10
def medicationpatients(medication_name):
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT COUNT(pfile.Patient_ID) AS COUNTER
    FROM Patient_File pfile
    JOIN Medication_Plan plan ON pfile.Medication_Plan_ID =      plan.Medication_Plan_ID 
    JOIN Medication_File medication ON     
    medication.Medication_File_ID = plan.Medication_File_ID  
    WHERE medication.Medication_Name = %s;"""
    variable = (medication_name)
    cursor.execute(query, variable)
    results = cursor.fetchall()
    result = []
    for count in results:
      total = count["COUNTER"]
      temp_total = str(total)
      statement = "Total number of patients with " + medication_name.title() + " in their medication plan is " + temp_total + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print

#Finished #11
def planfile(medication_name):
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT COUNT(plan.Medication_Plan_ID) AS COUNTER
    FROM Medication_Plan plan
    JOIN Medication_File medication ON     
    medication.Medication_File_ID = plan.Medication_File_ID  
    WHERE medication.Medication_Name = %s;"""
    variable = (medication_name)
    cursor.execute(query, variable)
    results = cursor.fetchall()
    result = []
    for count in results:
      total = count["COUNTER"]
      temp_total = str(total)
      statement = "Total number of medication plans with " + medication_name.title() + " is " + temp_total + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print

#Finished #8
def paymentpatients (payment_method):
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT COUNT(patients.Patient_ID) AS COUNTER
    FROM Patient patients
    JOIN Payment_Method payment ON       
    patients.Payment_Method_ID = payment.Payment_Method_ID
    WHERE payment.Payment_Type = %s;"""
    variable = (payment_method)
    cursor.execute(query, variable)
    results = cursor.fetchall()
    result = []
    for count in results:
      total = count["COUNTER"]
      temp_total = str(total)
      statement = "Total number of patients with a payment type of " + payment_method.title() + " is " + temp_total + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print
  
#Finished #14
def plan (SSN):
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    query = """SELECT plan.First_Name, plan.Last_Name, medication.Medication_Name, plan.Dosage, plan.Deration_Of_Plan, plan.Active, plan.Paid
FROM Medication_Plan plan
JOIN Medication_File medication ON medication.Medication_File_ID = plan.Medication_File_ID
JOIN Patient_File patient_file on patient_file.Medication_Plan_ID = plan.Medication_Plan_ID
JOIN Patient patient on patient.Patient_ID = patient_file.Patient_ID
WHERE patient.SSN = %s;"""
    variable = (SSN)
    cursor.execute(query,variable)
    results = cursor.fetchall()
    result = []
    statement = ""
    for mp in results:
      first_name = mp["First_Name"]
      last_name = mp["Last_Name"]
      medication_name = mp["Medication_Name"]
      dosage = mp["Dosage"]
      duration = mp["Deration_Of_Plan"]
      active = mp["Active"]
      paid = mp["Paid"]
      check_active = "Not Active"
      check_paid = "Not Paid"
      if active == 1:
        check_active = "Active"
      if paid == 1:
        check_paid = "Paid"
      full_name = first_name + " " + last_name
      statement = "Patient Name: " + full_name + "\n Medication Name: " + medication_name + "\n Dosage: " + dosage + "\n Duration of Plan: " + duration + "\n Active Status: " + check_active + "\n Paid Status: " + check_paid + "\n"
      

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
  return statement
  
#Finished #16
def paid ():
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT COUNT(pfile.Patient_ID) AS COUNTER
    FROM Patient_File pfile
    JOIN Medication_Plan plan ON pfile.Medication_Plan_ID =      plan.Medication_Plan_ID 
    WHERE plan.Paid = 1;"""
    cursor.execute(query)
    results = cursor.fetchall()
    result = []
    for count in results:
      total = count["COUNTER"]
      temp_total = str(total)
      statement = "Total number of patients who have a paid billing information is " + temp_total + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print

#Finished #17
def regionpatient():
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    count = 1
    result = []
    while True:
      query = """CALL RegionPatitents (%s, @name,@counter);"""
      variables = (count)
      cursor.execute(query,variables)
      cursor.execute("SELECT @name")
      connection.commit()
      results = cursor.fetchall()
      name = None
      for region in results:
        name = region['@name']
      cursor.execute("SELECT @counter")
      results = cursor.fetchall()
      counter = None
      for region in results:
        counter = region['@counter']
      if name == None or counter == None:
        break
      else:
        temp_counter = str(counter)
        statement = "Region: " + name + ", Total Number of Patients Within Region: " + temp_counter + "\n"
        result.append(statement)
        count = count + 1

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
    
  return final_print
  
#Finished #6
def total_stock():
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT medication.Medication_Name, inventory.Total_Stock
FROM Medication_File medication
JOIN Inventory inventory ON medication.Medication_File_ID = inventory.Medication_File_ID;"""
    cursor.execute(query)
    #cursor.comit()
    results = cursor.fetchall()
    result = []
    for medication in results:
      medication_name = medication["Medication_Name"]
      total_stock = medication["Total_Stock"]
      temp_stock = str(total_stock)
      statement = "Medication Name: " + medication_name + ", Total Stock: " + temp_stock + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
  return final_print
  
#Finished #2
def medication_supplier_list ():
  result = None
  try:
    connection = connect()
    cursor = connection.cursor()
    query = """SELECT medication.Medication_Name, supplier.Supplier_Name, supplier.Contact_Number
FROM Medication_File medication
JOIN Supplier supplier on medication.Supplier_ID = supplier.Supplier_ID;"""
    cursor.execute(query)
    #cursor.comit()
    results = cursor.fetchall()
    result = []
    for medication in results:
      medication_name = medication["Medication_Name"]
      supplier_name = medication["Supplier_Name"]
      contact_number = medication["Contact_Number"]
      statement = "Medication Name: " + medication_name + ", Supplier Name: " + supplier_name + ", Contact Number: " + contact_number + "\n"
      result.append(statement)

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
  return final_print

#Finished #1
def supplycheck ():
  result = None
  try: 
    connection = connect()
    #if connection:
    cursor = connection.cursor()
    count = 1
    result = []
    while True:
      query = """CALL SupplyMedicationCheck(%s, @name,@counter);"""
      variables = (count)
      cursor.execute(query,variables)
      cursor.execute("SELECT @name")
      connection.commit()
      results = cursor.fetchall()
      name = None
      for supply in results:
        name = supply['@name']
      cursor.execute("SELECT @counter")
      results = cursor.fetchall()
      counter = None
      for supply in results:
        counter = supply['@counter']
      if name == None or counter == None:
        break
      else:
        temp_counter = str(counter)
        statement = "Supplier Name: " + name + ", Total Number of Medication File Linked: " + temp_counter + "\n"
        result.append(statement)
        count = count + 1

  except Exception as error:
    result = error

  finally:
    cursor.close()
    connection.close()
    
  final_print = ""
  for temp in result:
    final_print = final_print + temp  
  return final_print
