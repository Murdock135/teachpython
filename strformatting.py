age1 = input('What is your age')
age2 = int(input('What is your age'))

print("Your age is", age1)
print("Your age is ", age2)#method1

print(f"your age is {age1}")#method2
print('your age is {}'.format(age1))#method3

print('your age is {0} and my age is {1}'.format(age1, age2))

print('your age is {1} and my age is {0}'.format(age1, age2))


