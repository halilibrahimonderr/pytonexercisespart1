# to convert a number to string we can use str() function this is called casting
num1=5716321453
num1_str=str(num1) # cast num1 to string and assign to num1_str
num2=str(num2)
num3=str(num3)

print(len(num1_str)) # check the length of the string
print(num1_str[2]) # get the third element of string (the one in the 3rd order)
print(num1_str[2:5]) # get the 3-5 elements of string (both inclusive) by string slicing
print(num2 in num1_str) # check if num2 in string (cast if necessary)
print(num3 in num1_str) # check if num3 in string (cast if necessary)


string_with_0='0'+num1_str
print(string_with_0) # concatenate 0 to the string from left and assign to string_with_0
print(string_with_0[:4]) # get the characters of string_with_0 from start to position 4 (end point exclusive)
print(string_with_0[5:]) # get the characters of string_with_0 from position 5 until the end
print(string_with_0[-10:-7]) # use negative indexing to reach the "567" string_with_0 