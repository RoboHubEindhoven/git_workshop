#changed only comments to not fuck up the code :)

year =  input("Give the year in 4 digits    : ")
month = input("Give the number or the month : ")
day =   input("Give the number of the day   : ")

doomsday = 0

doomsday_month = [0, 31, 28, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]

weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']






def check_years_doomsday(year):
	century = int(year/100)
	#print century

	if century in {15, 19, 23}:
		century_doomsday = 3
	elif century in {16, 20, 24}:
		century_doomsday = 2
	elif century in {17, 21, 25}:
		century_doomsday = 0
	elif century in {18, 22, 26}:
		century_doomsday = 5
	else:
		print("Date not available for calculation")
		return
	#print "century = ",century
 
	y = year - century*100
	doomsday = ((y+(y/4))%7 + century_doomsday)%7

	return doomsday

def check_for_leap(year):
	if (year % 4) == 0:  
	   if (year % 100) == 0:  
		   if (year % 400) == 0:  
		       return True
		   else:  
		       return False
	   else:  
		   return True 
	else:  
	   return False

def doomsday_of_month_checker(year, month):
	day = doomsday_month[month]
	if check_for_leap(year) and (month == 1 or month == 2):
		day += 1
	return day

year_doomsday = check_years_doomsday(year)
#print "The doomsday of ",year,"is :" ,year_doomsday,"."


doomsday_of_month = doomsday_of_month_checker(year, month)


print "doomsday_of_month is : ",doomsday_of_month

diff_days = day-doomsday_of_month
tmp = diff_days+year_doomsday
day_of_week = tmp%7
day_name_of_week = weekday[day_of_week]

#print "day of the week is :",day_of_week

print "That day was a:",day_name_of_week

