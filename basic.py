#3 types string

a =  'Hello python'
print(a)

b = "Hello python"
print(b)

c = """ Hello student's, "how are you"? """
print(c)

#Numbers in python

e = 345
print(e)
print(type(e))

f = 3.55
print(f)
print(type(f))

g = 555555555666666 #long datatype for python v2 not v3
print(g)
print(type(g))


h = 8 + 7j
print(h)
print(type(h))
print(h.real, "real part")
print(h.imag, "imaginary part")

x = 28
print(float(x))

y = 5.667
print(int(y))

#ints are narrower than floats
#floats are wider than ints

print(complex(y + 0j))  #j = sqrt(-1)
#float to complex but vice versa is not possible
#floats are narrower than complex numbers and complex numbers are wider than floats

ab = 4
ac = 5.7
cd = 12 + 8j

#Rule: Widen numbers so they'r the same types
#add
print(ab + ac) #int+float

#sub
print(ac - ab) #float-int

#mul
print(ac * cd) #float * complex

#Div
print(cd / ac) #complex/float

print(16/5) #return float
print(16 // 5) #return only integer part(quotient)
print(16 % 5) #return remainder
#print(2/0) #undefined

print(dir())  #short for "directory" - this contains collection of common objects which are always available
print(__builtins__)

#use of help
#print(help(pow))

print(pow(4, 2))
print(4 ** 2) #double asterisk works for power


#hex(number) -> string (hexadecimal representation of the number"
print(hex(10)) #hexadecimal in python begins with 0x

print(0xa) #it prints the decimal number (hex -> dec)

import math
print(dir(math))
print(help(math.radians))

print(math.radians(180))


print(type(True))
print(type(False))
t = 4
s = 6
print(t == s) #it will return boolean result
print(t != s) #it will return boolean result

#in python 0 is converted to false other numbers are ture
print(bool(20))
print(bool(0))

#for boolean not empty string will return true and empty will false
print(bool("Hello"))
print(bool(""))
print(bool(" ")) #this string contains space so this is not empty

#boolean to string, the string has quotes boolean does not
print(str(True))
print(str(False))

#boolean to integer
print(int(True))
print(int(False))

print(67 + True)
print(67 + False)
print(3 * False)

import datetime
#print(help(datetime))

ft = datetime.date(1952, 2, 21)
print(ft) #can access the year month day seperately
print(ft.day)

dt = datetime.timedelta(100)
print(ft + dt)

ct = datetime.timedelta(-365)
print(ft + ct)


#Day name, month name, day, year
print(ft.strftime("%A, %B %d, %Y"))


launch_date = datetime.date(2017, 1, 15)  #y, m, d
launch_time = datetime.time(12, 15, 5)  #h, m, s
launch_datetime = datetime.datetime(2017, 1, 15, 12, 15, 5)
print(launch_date)
print(launch_time)
print(launch_datetime)

now = datetime.datetime.today()
print(now)
print(now.microsecond)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))

print(datetime.timedelta(8, 9, 5, 6, 7, 2))

