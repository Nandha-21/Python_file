#Date and Month Module:
import datetime as d
print(d.datetime.now())
print(d.date(2023,12,21))       #yyyy,mm,dd                                     
date=d.date.today()
print(date)
print(date.day)
print(date.month)
print(date.year)
print(date.weekday())       #start 0 to 6 (monday=0)
print(date.isoweekday())    #start 1 to 7 (monday=1)

anotherdays=d.timedelta(days=100)     #add and subs
print(date+anotherdays)

nextday=date+anotherdays
print(nextday)
print((nextday-date).days)      #different between days

#Time Module:
print(d.time(5,20,40,22))       #hh,mm,ss,(optional)ms
time=(d.time(5,20,40,22))
print(time.hour)
print(time.minute)
print(time.second)

Dt=d.datetime.now()
print(Dt.strftime('%B'))
