import json
from datetime import date
from dateutil.parser import parse

with open("dates.json", encoding="utf8") as file:
    dates_list = file.read()

def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age

today = date.today()

dates_str = ""
dates=json.loads(dates_list)
lena = len(dates)
vozrast = 0
for x in range(0,lena):
    dates_str = ""
    dates_str=str((dates[x]['birthday']))
    dates_obj = parse(dates_str)
    dates_obj= str(dates_obj.date())
    dates_obj= dates_obj.replace('-',' ')
    dates_obj= dates_obj.split(' ')
    vozrast = vozrast+ (calculateAge(date(int(dates_obj[0]), int(dates_obj[1]), int(dates_obj[2]))))

print(vozrast/lena)
