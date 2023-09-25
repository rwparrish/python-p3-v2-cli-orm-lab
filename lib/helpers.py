from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for emp in employees:
        print(emp)
        

def find_employee_by_name():
    name = input("Please enter employee name: ")
    if employee := Employee.find_by_name(name):
        print(employee)
    else:
        print(f'Employee with name {name} not found')


def find_employee_by_id():
    id_ = input("Please enter Employee ID: ")
    if employee := Employee.find_by_id(id_):
        print(employee)
    else:
        print(f'No employee with an ID of {id_} found')


def create_employee():
    name = input("Please enter Employee Name: ")
    title = input("Please enter Employee Job Title: ")
    department_id = int(input("Please enter Department ID: "))
    
    try:
        new_employee = Employee.create(name, title, department_id)
        print(new_employee)
    except Exception as exc:
        print('Error creating employee: ', exc)


def update_employee():
    id_ = input("Please enter Employee ID: ")
    if employee := Employee.find_by_id(id_):

        try: 
            name = input("Please enter Employee Name: ")
            employee.name = name
            title = input("Please enter Employee Job Title: ")
            employee.job_title = title
            department_id = int(input("Please enter Department ID: "))
            employee.department_id = department_id
            employee.update()
            print(employee)
            
        except Exception as exc:
            print('Error updating employee: ', exc)
    else:
        print(f'No employee with an ID of {id_} found')
        
        

def delete_employee():
    emp_id = input('Please enter the employee ID: ')
    if emp := Employee.find_by_id(emp_id):
        emp.delete()
        print(f'Employee with ID of {emp_id} has been destroyed.')
    else:
        print(f'Employee with ID of {emp_id} not found.')
        
        


def list_department_employees():
    dept_id = input("Please enter a Department ID: ")
    if dep := Department.find_by_id(dept_id):
        for emp in dep.employees():
            print(emp)
    else:
        print(f'Department ID {dept_id} not found.')