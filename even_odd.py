def odd_even(a):
    return (a)

number1 = 5



if (number1 %2==0):
    print(f"it is even number {number1}")
else:
    print(f"it is odd number {number1}")

odd_even(number1)

def isnumbers(number):
    isinteger = True

    for eachinteger in number:
        if(eachinteger >= "0" and eachinteger <= "9"):
            continue
        else:
            isinteger = False
            break

    return isinteger

result  = isnumbers("12311")

if result:
    print("yes it is an integer")
else:
    print("it is not integer")


def simplegreeting():
    name = input("enter your name /n")
    age = input("enter your age")
    #print("/n")
    print(f"namasakara {name}")
    print(f"you are {age} in next year")

#simplegreeting()
def printASCIIofstring(string):
    for character in string:
        ascii_value = ord(character)
        print(f"{character} -> {ascii_value} ")

#printASCIIofstring("ABCDEFGHIGKLMNOPQRSTUVWXYZ")
#printASCIIofstring("12345")
#printASCIIofstring("abcdefghijklmnopqrstuvwxyz")


def getstrlength(string):
    counter = 0
    if string != None:
        for character in string:
            counter = counter +1

    return counter 
input1 = "maesha"
input2 = "12525253"
length = getstrlength(input1)
length = getstrlength(input2)
#print(f"string length of {input1} is {getstrlength(input1)}")
#print(f"string length of {input2} is {getstrlength(input2)}")


def count_vowels(str) -> int:
    counter = 0

    if str is not None:
        for character in str:
            if (character == "a" or
                character == "e" or
                character == "i" or
                character == "o" or
                character == "u" or
                character == "A" or
                character == "E" or
                character == "I" or
                character == "O" or
                character == "U" ):
                counter += 1
    return counter

#print(f"number of vowels in {"hello"} is = {count_vowels(input)}")

def reverseString(string):
    length = len(string)
    middle = int(length/2)

    print(f"length = {length}")
    print(f"middle = {middle}")

    print("first loop")
    for start in range(0, middle, 1):
        print(start)

    print("second loop")
    for end in range(length -1, middle, -1):
        print(end)

name = "abcdeg"
reverseString(name)
print(name)


def getsum(numbers):
    sum = 0

    for number in numbers:
        print(f"sum of two numbers",sum)
        number = number +1

#getsum()
#numbers = [1,2,3,4]
#print(numbers)