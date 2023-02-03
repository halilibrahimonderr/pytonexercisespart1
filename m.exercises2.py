#the number types can be converted to each other wit the int() float() complex() methods also float numbers can be rounded with the method round()

num1=7 # convert num1 to float and assign to itself
num2=5.8 # convert num2 to int and assign to itself
num3=9 # convert num3 to complex and assign to itself
num4=1.453 # use round method for num4 and assign to itself
num5=5.71 # use round method for num5 and assign to itself
# print them all
# print their types

num1 = float(num1)
num2 = int(num2)
num3 = complex(num3)
num4 = round(num4)
num5 = round(num5)

print(num1,'=>',type(num1))
print(num2,'=>',type(num2))
print(num3,'=>',type(num3))
print(num4,'=>',type(num4))
print(num5,'=>',type(num5))
