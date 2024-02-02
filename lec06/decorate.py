def printStarts(n):
    for i in range(n+8):
        print("#", end="")
    print()

def decorate(str):
    printStarts(len(str))
    print("***", str, "***")
    printStarts(len(str))

decorate("Jonah")
decorate("July June")
