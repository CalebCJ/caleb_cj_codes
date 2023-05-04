
employee_name=input("Enter the employee Name:")
employee_ID=input("Enter teh employee ID:")
basic_pay=float(input("enter the basic pay:"))
DA=basic_pay*(12/100)
HRA=basic_pay*(5/100)
PF=3200
Net_salary=basic_pay+DA+HRA-PF
print("Net_salary")
