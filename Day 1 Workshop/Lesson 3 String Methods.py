text = "Hello World!"

#Upper String Method
print(text.upper())

#lower String Method
print(text.lower())

#remove whitespace String Method
print(text.strip())

#String SLice
print(text[4:9])

#replacing strings
print(text.replace("Hell", "z"))

#Adding Strings Together and Formating
name = "Name"
surname = "Surname"
age = 22

fullname1 = f'My name is {name}, and my surname is {surname}. I am turning {age} years old'
fullname2 = 'My name is {}, and my surname is {}. I am turning {} years old'

print(fullname1)
print(fullname2.format(name, surname, age))