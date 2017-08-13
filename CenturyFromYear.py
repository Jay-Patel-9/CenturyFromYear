year = int(input("Enter the year"))
x = year / 100
y = year % 100
if y == 0 :
	print "The Century of the year is:",x
else: 
	x = x + 1
	print "The Century of the year is:",x
