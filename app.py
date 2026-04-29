from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from Bill import Bill
from Medicine import Medicine
import json
import pandas as pd
import os

def save_file(file_name,data):
  try:
   with open(file_name,"r") as f:
       old=json.load(f)
  except:
    old=[]

  old.append(data)

  with open(file_name,"w")as f:
    json.dump(old,f,indent=4)


def add_patient():
  patient_id=input("Patient ID Sir/Madam:")
  name=input("Name:")
  age=input("Age:")
  gender=input("Gender :")
  phone=input("Phone Number:")
  
  p= Patient(patient_id,name,age,gender,phone)
  save_file("Patients.json",p.to_dict())

  print("Patient added Successfully")

def add_doctor():
  doctor_id=input("Doctor Id:")
  name=input("Doctor Name:")
  specialization=input("Specialization:")
  phone=input("Phone Number")

  d=Doctor(doctor_id,name,specialization,phone)
  save_file("Doctor.json",d.to_dict())
  print("Doctor Added Successfully")

def add_appointment():
  appointment_id=input("Appointment id:")
  patient_id=input("Patient Id :")
  doctor_id=input("Doctor Id :")
  date=input("Date :")
  disease=input("Disease Name :")

  a=Appointment(appointment_id,patient_id,doctor_id,date,disease)
  save_file("Appointment.json",a.to_dict())
  print("Appointment Added Successfully")
  save_appointments_csv()

def save_appointments_csv():

    p = pd.read_json("Patients.json")
    d = pd.read_json("Doctor.json")
    a = pd.read_json("Appointment.json")

    # 🔴 convert ids to SAME type
    p["patient_id"] = p["patient_id"].astype(str)
    a["patient_id"] = a["patient_id"].astype(str)

    d["doctor_id"] = d["doctor_id"].astype(str)
    a["doctor_id"] = a["doctor_id"].astype(str)

    m1 = a.merge(p, on="patient_id")
    m2 = m1.merge(d, on="doctor_id", suffixes=("_patient","_doctor"))

    report = m2[["name_patient","name_doctor","disease","date"]]

    report.to_csv("Appointments_Report.csv", index=False)

    print("CSV Updated Successfully")
  
  
def generate_bill():
  bill_id=input("Bill ID:")
  patient_id=input("Patient ID:")
  appointment_id=input("Appointment ID:")
  total_amount=input("Total Amount:")

  generate_b=Bill(bill_id,patient_id,appointment_id,total_amount)
  save_file("Bill.json",generate_b.to_dict())
  print("Generated Bill Successfully")


def hospital_analysis():
  df=pd.read_json("Appointment.json")

  print("Most comman disease:")
  print(df["disease"].value_counts().head())
  print("\n Appoinment per Doctor:")
  print(df["doctor_id"].value_counts())
  print("\n")

def check_appointment():
   p=pd.read_json("Patients.json")
   d=pd.read_json("Doctor.json")
   a=pd.read_json("Appointment.json")
   m1=a.merge(p,on="patient_id")
   m2=m1.merge(d,on="doctor_id", suffixes=("_patient","_doctor"))
   print(m2[["name_patient","name_doctor","disease"]])
   

while True:

    print("\n --- Hospital System ---")
    print("1 Add Patient")
    print("2 Add Doctor")
    print("3 Book Appointment")
    print("4 Generate Bill")
    print("5 Analysis")
    print("6 Check Appoiment")
    print("7 Exit")
    
    choice =input("Select Option:")
    if choice == "1":
        add_patient()

    elif choice == "2":
        add_doctor()

    elif choice == "3":
        add_appointment()

    elif choice == "4":
        generate_bill()

    elif choice == "5":
        hospital_analysis()

    elif choice == "6":
        check_appointment()

    elif choice == "7":
          break