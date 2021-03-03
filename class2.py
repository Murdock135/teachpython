#for loops and if statements

tuple1 = ("keys", 2, "cars") #accessible but not mutable
set1 = {"yo", 1, "hello"}#immutables
list1 = [1,2,"yo"]

# for count in tuple1:
#     print(count)

# # print(len(tuple1))
# print()

# for count in range(0, len(tuple1)):
#     print(count)

# varB = input('what is your variable? ')

# if "keys" not in varB:
#     print(tuple1)
# else:
#     print(list1)

# count=1
# while count<10:
#     print(varB[count])
#     count = count +1

'''summary
1. input
2. for loop
3. while loop
4. if statement
5. in/not in
6. immutables and iterables
7. range()
8. len() '''

#PROJECT EULER PROBLEM 1

listOfMults = []
for i in range(0,1000):
    if i%3==0 or i%5==0:
        listOfMults.append(i)

print(listOfMults)
print(sum(listOfMults))