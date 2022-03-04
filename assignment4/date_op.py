from datetime import datetime, date, timedelta
class date_operation:
    def __init__(self):
        pass

    def get_current_datetime(self):
        today = datetime.now()
        print("today's date and time  is ", today)
        
    def birth_date(self, year, month, days):
        birth_date = date(year, month, days)
        print(birth_date)
     
    def get_age(self, year, month, days):
        birth_date = date(year, month, days)
        today = datetime.now()
        curr_year = today.year - year
        curr_month = abs(today.month - month)
        curr_days = abs(today.day - days)
        print(curr_year, "years",curr_month,"months",curr_days, "days")
        time_to_take_fifty = timedelta(days = 18250) + birth_date
        final_time = time_to_take_fifty.year - year
        print("time_to_take_fifty",final_time-curr_year,"year")

