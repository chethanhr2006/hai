#numbers = [1,2,3,4]
#c1 = numbers[0]
#numbers[0] = 100
#print(numbers)
#print(c1)
#print(numbers.append(100))
#print(numbers)
#number1 = [1,2,3,4,8,9]
#print(number1.append(10))
#number1.insert(0,10)
#print(number1.sort())
#print(number1)

#num = [1,2,3,5,4,6]
#num.insert(0,10)
#num.sort()
#num.reverse()
#num.index(3)
#num.remove(5)
#value = num.pop(5)
#print(value)
#print(num)
#for num in num:
#    print(num)

#print(num[0])

num = [1,2,3]
print(num[2])
# two diminsional array but it works as list
matrix = [
    [1,2,3,4],
    [5,6,7,8]
]
matrix[0][0] = 2
matrix[0][1] = 4
matrix[0][2] = 6
matrix[0][3] = 8
matrix[1][0] = 10
matrix[1][1] = 12
matrix[1][2] = 14
matrix[1][3] = 16
#print(matrix[1][3].__index__())
#print(matrix)

#function
def add_sum(a,b,d):
    c = a+b+d
    if c >= 10:
        print(c)
    else:
        print("not equal to 10")
        
#add_sum(5,5,3)

def add_mul(a,b):
    while True:
        c = a+b
        if c>10:
            print(f"sum is done with given data {c}")
            break
        else:
            print("not done!")
            
#add_mul(1,10)

def marks_of_students():
    sci = 98
    soc = 99
    kannada = 98
    hin = 98
    total_marks = sci + soc + kannada +hin
    prece = total_marks/4
    while True:
        if total_marks > 390:
            print(f"student got marks of {total_marks}")
            #print(f"student got marks of {total_marks} and precentage of {prece}")
            break
    
        else:
            print(f"student got less than {total_marks}")
            print(prece)
            
        
            
    print(f"student got marks of {total_marks} and precentage of {prece}")
            
#marks_of_students()

def student_detials(name,age,clas):
    print("student detials")
    print("name", name)
    print("age", age)
    print("class", clas)
    return name,age

#student_detials("ram", 25, "C5")
#student_name, student_age = student_detials("ram", 25, "C5")
#print("student name returned is ",student_name)
#print("student age returned is ",student_age)

def boys_count(name,age):
    pass
def girls_count(count,name):
    pass

boys_count("ram", 25)
girls_count(10, "ram1")

#loops
#syntax of loops ->> start : stop : step(move)
# while, for, dowhile

#a = input("enter your name: ")
#for a in range(0,4):
    #print(a)
    #if a>5:
        #print("done!")
    #else:
        #print("doing....")
        

for i in range(1,-9):
    if i==3:
        break
    i+=1
    print(i)
    
names = ("ram","ramesh","suresh")
for name in names:
    print(name)
count  = 0
while (count<=10):
    print(count)
    count += 1
    
for i in range(10,-1,-1):
    print(i)