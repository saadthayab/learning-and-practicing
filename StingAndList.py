#String and List in Python

colors =["Red","Orange","Yellow","Green","Blue","Purple"]

sentence = "The quick brown fox jumped over the lazy dog"

print (sentence[0])
print (sentence[4])
print (sentence[4:])
print (sentence.split(' '))


print (colors[0])
print (colors[0:4])

# join convert that list into string, we can get the lest back by using split
print ("-".join(colors))

print ("-".join(colors).split("-"))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# for loop
for collor in colors : print(collor)

for number in [1,2,3,4,5,6,7,8,9]:
    doubbldouble = number*2
    print ((" the number is " + str(number) + " and the double" + str(doubbldouble)))

countdown = 10
while countdown >0:
    print(countdown)
    countdown-=1

my_stirng = "whats the status statooos please provide your status"
print (my_stirng.upper())
print ( str(len(my_stirng))+ "this the the length of the statussss") # dont forget that we cant mix 
# int and string 

# In Python there comparing two string using == , not .equal

# in python and and or
if (7==8) or  (9==9):
     print ('true')
else:
    print ("fail")
