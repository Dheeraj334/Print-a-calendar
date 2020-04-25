import calendar
month=12
n=1
year=int(input("Enter the year which you want to see month:::-"))
for i in range(0,month):
    calendar.prmonth(year,n)
    n=n+1