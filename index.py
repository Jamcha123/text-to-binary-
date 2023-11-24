import json

f1 = open("index.json", "r")
numX = json.load(f1)
newWord = "{0}".format(numX["words"]).lower()
f1.close()

alpha = []
for x in range(25): 
    alpha.append(numX["letters"][x])
nums = []
start = 0
for x in range(len(newWord)):
    ascii = 141
    for x in range(len(alpha)): 
        if (newWord[start] == alpha[x]): 
            nums.append(ascii)
        ascii += 1
    start += 1
binaryNums = [1, 2, 4, 8, 16, 32, 64, 128]
myList = []
for x in range(len(nums)): 
    binary = [0, 0, 0, 0, 0, 0, 0, 0]
    num1 = nums[x]
    while (num1 != 0): 
        index = len(binaryNums)-1
        for x in range(len(binaryNums)): 
            if (num1 >= binaryNums[index]): 
                binary.insert(index, 1)
                binary.remove(binary[index+1])
                num1 -= binaryNums[index]
            index -= 1
    myList.append(binary)
f2 = open("index.txt", "a")
for x in range(len(myList)): 
    for y in range(len(myList[x])):
        f2.write(str(myList[x][y]))
    f2.write("\n")
f2.close() 
            