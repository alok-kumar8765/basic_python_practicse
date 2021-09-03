work_hour=[('raj',200),('aryan',250),('lex',300)]
def check_employ(work_hour):
    max_hour=0
    employee_of_month = ' '
    for employee,hour in work_hour:
        if hour > max_hour:
            max_hour = hour
            employee_of_month = employee
        else:
            pass
    return(employee_of_month,max_hour)
result=(check_employ(work_hour))
print(result)