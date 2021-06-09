import calendar

year = int(input("Enter the Year:"))
month =int(input("Enter the month:"))
day = int(input("Enter the day:"))
calendar.setfirstweekday(calendar.SUNDAY)
mycal=calendar.month(year,month)
mycal=calendar.calendar(year)
print(mycal)