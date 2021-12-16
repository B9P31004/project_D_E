import datetime

def semester_confirm():
    date=datetime.date.today()
    semester_1=datetime.date(date.year,4,1)
    semester_2=datetime.date(date.year,8,1)
    semester_3=datetime.date(date.year+1,1,1)
    if date<semester_1:
        return 3
    elif date>=semester_1 and date<semester_2:
        return 1
    elif date>=semester_2 and date<semester_3:
        return 2