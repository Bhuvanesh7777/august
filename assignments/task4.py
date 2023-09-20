employee_database = {}

def add_employee():
    domain = input("Enter employee domain: ")
    name = input("Enter employee name: ")
    empid = input("Enter employee ID: ")
    email = input("Enter employee email: ")
    

    employee = {
        "Domain": domain,
        "Name": name,
        "Emp ID": empid,
        "Email": email
    }
    

    employee_database[empid] = employee
    print("Employee added successfully!")


def print_employee(empid):
    employee = employee_database.get(empid)
    if employee:
        print("\nEmployee Details:")
        for key, value in employee.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")

while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        empid = input("Enter Employee ID to print details: ")
        print_employee(empid)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")