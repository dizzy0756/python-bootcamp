from datetime import datetime

print(f"Date : {datetime.today().date()}")
print(f"Time : {datetime.today().time()}")
print(f"Weekday : {datetime.today().strftime("%A")}")
