listOfNums = []
count = 0

while count<5:
    string_nums = input('Enter a digit: ')
    nums = int(string_nums) #convert to int


target = int(input('What\'s the target'))

listLength = len(listOfNums)

for m in range(0, listLength-1):
    for n in range(m+1, listLength-1):
        if listOfNums[m]==listOfNums[n]:
            continue
        elif listOfNums[m]+listOfNums[n]==target:
            print(m,n)


