from date_op import date_operation
obj = date_operation()
obj.get_current_datetime()
year = int(input("enter your birth year"))
month = int(input("enter the month number of your birth"))
day = int(input("enter the date of your birth"))
obj.birth_date(year, month, day)
obj.get_age(year, month, day)
