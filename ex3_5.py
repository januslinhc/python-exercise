def convert(mystr):
    if mystr == 1:
        return "1/4"
    if mystr == 3:
        return "3/4"


# Driver program
mystr = int(input())
print(convert(mystr))