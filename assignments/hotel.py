patients = []

def add_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    
    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender
    }
    
    patients.append(patient)
    print("Patient added successfully.")

def display_patients():
    if len(patients) == 0:
        print("No patients in the system.")
    else:
        for patient in patients:
            print(patient)

def search_patient_by_id():
    patient_id = input("Enter the ID of the patient you want to search: ")
    for patient in patients:
        if patient["ID"] == patient_id:
            print("Patient found:")
            print(patient)
            return
    print("Patient not found.")


def delete_patient_by_id():
    patient_id = input("Enter the ID of the patient you want to delete: ")
    for patient in patients:
        if patient["ID"] == patient_id:
            patients.remove(patient)
            print("Patient deleted successfully.")
            return
    print("Patient not found.")


def update_patient_by_id():
    patient_id = input("Enter the ID of the patient you want to update: ")
    for patient in patients:
        if patient["ID"] == patient_id:
            patient["Name"] = input("Enter updated name: ")
            patient["Age"] = input("Enter updated age: ")
            patient["Gender"] = input("Enter updated gender: ")
            print("Patient details updated successfully.")
            return
    print("Patient not found.")

while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient by ID")
    print("4. Delete Patient by ID")
    print("5. Update Patient by ID")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        search_patient_by_id()
    elif choice == "4":
        delete_patient_by_id()
    elif choice == "5":
        update_patient_by_id()
    elif choice == "6":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please select a valid option.")