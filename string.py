# adding a comment in the remote repo
'''
# print("Hello World")
# print(help('keywords'))
# a = b = c = 10
# print(a,b,c)
# x = 47  #statement
# y = 47 + 10
'''
# print(int(10.24))
# print(int("10.24"))
# print(int(float("10.24")))
# print(str(20))
# print(type(str(20)))
# print(list('hello'))
# first_name = ('jane')
# print(first_name)
# last_name = "doe"
# print(last_name)
# address = '''10 Main St'''
# print(address)
# # job1 = "physician's assistant"
# emp_name = "jane Doe"
# print(len(emp_name))
# print(emp_name.upper())
# print(emp_name.lower())
# first_name = "jane"
# last_name = "Doe"
# print(first_name + " " + last_name)
# age = 24
# print(first_name + " " + last_name + " " + str(age))
# print("hello " * 3)
# emp_name = "Jane doe"
# print(emp_name[3])
# # print(emp_name[8])
# print(emp_name.index("n"))

emp_name = "jane Doe"
print(emp_name[2:6])
print(emp_name[:4])
print(emp_name[5:])
print(emp_name[-4:-1])
print(emp_name[1:6:2])#the third number allows you to count every other number because it is 2 so it prints every other from 1-6
print(emp_name.count('e'))
print(emp_name.find('Doe'))
emp_name = emp_name.replace("jane", "john")
print("oh" in emp_name)

student_name = "alice"
score = 87
print(student_name + ": " + str(score))
print("{}: {}".format(student_name, score))
print(f'{student_name}: {score}')
print(f'10 times 3 is {10*3}')
