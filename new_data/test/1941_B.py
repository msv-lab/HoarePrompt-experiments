answers = []


def processArray(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array

    # check for success


def CheckForSuccess(arrayForSuccess):
    # print(f"Checking this array for success: {arrayForSuccess}")
    for x in arrayForSuccess:
        if x != 0:
            return False

    return True


def mainAlgorithm(inputarray):
    if CheckForSuccess(inputarray):
        answers.append("YES")
        return

    loop_counter = 1
    while (loop_counter != 100):
        length = len(inputarray)
        # print(f"Array length {length}")

        # find index to highest element that is not 0 and not n-1
        highestNumber = -1
        highestIndex = -1
        for elementIndex in range(1, length - 1):
            if inputarray[elementIndex] >= highestNumber:
                highestIndex = elementIndex
                highestNumber = inputarray[elementIndex]

        # print(f"Highest Index of {inputarray} is {highestIndex}")

        if (highestNumber < 0):
            # Bail out time
            answers.append("NO")
            return

        newArray = processArray(inputarray, highestIndex)
        # print (f"New Array: {newArray}")

        if (CheckForSuccess(newArray)):
            answers.append("YES")
            return

        loop_counter += 1

    answers.append("NO")


# my algorithm is find highest number and always start wit hthat one.


numberOfArrays = int(input())
for arrayCounter in range(0, numberOfArrays):
    elementSize = int(input())
    array = list(map(int, input().split()))

    mainAlgorithm(array)

for ans in answers:
    print(f"{ans}")

