from datetime import date

def dates(input_date):
    y = int(str(input_date)[:4])
    m = int(str(input_date)[4:6])
    d = int(str(input_date)[6:8])
    return y,m,d

def numOfDays(start_date, end_date):
    return (end_date - start_date).days

#take input from user     
date1 = int(input(""))
date2 = int(input(""))

#sorts the dates accordingly
start_date = min(date1,date2)
end_date = max(date1,date2)

#extracts year, month, day from the date
y1,m1,d1 = dates(start_date)
y2,m2,d2 = dates(end_date)

if m1<1 or m1>12 or m2<1 or m2>12:
    print("Incorrect Date!!")
    exit()
elif d1<1 or d1>31 or d2<1 or d2>31:
    print("Incorrect Date!!")
    exit()
else:
    start_date = date(y1, m1, d1)
    end_date = date(y2, m2, d2)
    print(numOfDays(start_date, end_date), "days")