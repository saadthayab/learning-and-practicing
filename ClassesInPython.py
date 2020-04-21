#this is how work with classes using Python

class MyClass:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 
 def GetName(self):
  return self.name

 def SetName(self, name):
  self.name = name

 def GetAge(self):
  return self.age

 def SetAge(self, age):
  self.age = age
 
 def __str__(self):
  return "{0} is aged {1}.".format(self.name, self.age)

hello = MyClass("saad",41)
print (hello)