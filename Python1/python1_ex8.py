from random import seed, random

N = 50

def getRandomNumbers(amount):
    seed()
    numbers = []
    for i in range(amount):
        numbers.append(int(random()*amount*5))
    return numbers

def sortNumbers(numbers):
    sortedNumbers = numbers
    for j in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if (sortedNumbers[i] > sortedNumbers[i+1]):
                sortedNumbers[i], sortedNumbers[i+1] = sortedNumbers[i+1] , sortedNumbers[i]

    print("Sorted numbers: ",sortedNumbers)


unsortedNumbers = getRandomNumbers(N)
print("Unsorted numbers ",unsortedNumbers)
print("Expected sorted numbers: ",sorted(unsortedNumbers))
sortNumbers(unsortedNumbers)