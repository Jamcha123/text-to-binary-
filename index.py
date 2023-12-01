f1 = open("index.txt", "r")
newWord = "{0}".format(f1.read())
f1.close()
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "x", "z"]
asciiNums = []
for x in range(len(newWord)):
    num1 = 141
    for y in range(len(letters)):
        if(newWord[x] == letters[y]):
            asciiNums.append(num1)
        num1 += 1
binary1 = [1, 2, 4, 8, 16, 32, 64, 128]
binaryNums = []
for x in range(len(asciiNums)):
    binary2 = [0, 0, 0, 0, 0, 0, 0, 0]
    index = len(binary1)-1
    target = asciiNums[x]
    while(target != 0):
        if(target >= binary1[index]):
            target -= binary1[index]
            binary2.insert(index, 1)
            binary2.remove(binary2[index+1])
        index -= 1
    binaryNums.append(binary2)
f2 = open("binary.txt", "a")
for x in range(len(binaryNums)):
    for y in range(len(binaryNums[x])):
        f2.write(str(binaryNums[x][y]))
    f2.write("\n")
f2.close()