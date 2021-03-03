def two_sum(NumList):
    # listOfNums = []
    listOfNums = NumList
    count = 0

    # while count<5:
    #     string_nums = input('Enter a digit: ')
    #     nums = int(string_nums) #convert to int


    target = int(input('What\'s the target'))

    listLength = len(listOfNums)

    for m in range(0, listLength):
        for n in range(m+1, listLength):
            if listOfNums[m]==listOfNums[n]:
                continue
            elif listOfNums[m]+listOfNums[n]==target:
                print(m,n)

answer = two_sum([3,2,4,5,11])
print(answer)