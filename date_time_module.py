import datetime
mytime = datetime.time(2,30)
print(mytime.minute) #this will show minutes
print(mytime.hour)
print(mytime)
print(type(mytime)) #only hold values of time, there is no day associated with this 
today=datetime.date.today()
print(today) #date shown as europien standard
print(today.ctime()) #return current date

from datetime import datetime
mydatetime= datetime(2021,6,28,6,29) #(yyyy,mn,date,hh,mm,ss,ms,timezone) if you mis place anthing then value error comes
print(mydatetime)

print(mydatetime.replace(year=2022)) #this will help to replace value 

#Arithmetic in datetime
#checking date time difference
from datetime import date
date1=date(2021,6,28)
date2=date(1993,1,9)
result=date1-date2
print(result) #this will show days and it is datetime.timedelta

#method 2
dat1=datetime(2021,6,28,6,51,0)
dat2=datetime(1993,1,9,6,52,0)
result=dat1-dat2
print(result) #there are diff b/w d1-d2 due to leap yr