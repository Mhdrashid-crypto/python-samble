
class Employee:
    def __init__(self, emp_id, name, place, address, phone):
        self.emp_id = emp_id
        self.name = name
        self.place = place
        self.address = address
        self.phone = phone

    def display_employee(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Place:", self.place)
        print("Address:", self.address)
        print("Phone:", self.phone)


class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, place, address, phone,
                 joining_date, designation, salary):
        
        super().__init__(emp_id, name, place, address, phone)

        self.joining_date = joining_date
        self.designation = designation
        self.salary = salary

    def display_permanent(self):
        self.display_employee()
        print("Joining Date:", self.joining_date)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, place, address, phone,
                 start_date, contract_end_date, hourly_rate):
        
        super().__init__(emp_id, name, place, address, phone)

        self.start_date = start_date
        self.contract_end_date = contract_end_date
        self.hourly_rate = hourly_rate

    def display_contract(self):
        self.display_employee()
        print("Start Date:", self.start_date)
        print("End Date:", self.contract_end_date)
        print("Hourly Rate:", self.hourly_rate)

print("----- Permanent Employee -----")
emp1 = PermanentEmployee(1, "Rashid", "Kochi", "ABC House", "9876543210",
                         "01-01-2023", "Manager", 50000)
emp1.display_permanent()

print("\n----- Contract Employee -----")
emp2 = ContractEmployee(2, "Aman", "Calicut", "XYZ Villa", "9123456780",
                        "01-02-2024", "01-08-2024", 300)
emp2.display_contract()