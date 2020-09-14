arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
       'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def createCombos(newArr, arr, original, depth):
    for x in arr:
        for y in original:
            newArr.append(x+y)
    print(depth)
    if(depth > 1):
        return createCombos([], newArr[::], original[::], depth-1)
    else:
        return newArr


combo = createCombos([], arr, arr, 2)
with open("combo.txt","a+") as file:
    for x in combo:
        file.write(x+"\n")
