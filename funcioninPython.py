#Function in Python
# python is _ not camelCase only under score
name ='saad'
print ("there are {0} frinds in my life".format(name))


def namer(name):
    print ("hello from function or method %s" %name )
namer("saad")


def adding_two_numbers(first_n,second_n):
    return (first_n+second_n)
# use return and as an variable 
adding_three_numbers = 9 + adding_two_numbers(9,9)
print (adding_three_numbers)

fav_pizzaDictionary ={
    "faysal":"poporiny",
    "koskos":"hello",
    "koskokkkkoss":"hellohello"

}

for keeeyyyss, value in fav_pizzaDictionary.items():
    print (value)
    print(keeeyyyss)

