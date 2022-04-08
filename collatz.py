start = int(input("what is the starting number "))

def collatz(currnum: int):
    while True:
        if currnum %2 == 0:
            currnum /= 2
        else:
            currnum = currnum*3+1
        print(int(currnum))
        if currnum == 1:
            break
collatz(start)