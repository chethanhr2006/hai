num = int(input("Num:"))

match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _:
        print("some other number is continueing")
        

day = input("enter the day:")
match day:
    case "monday":
        print("starting of week")
    case "tuesday":
        print("second day of a week")
    case "wednesday":
        print("mid of the week")
    case "thursday":
        print("mid day of the week ")
    case "friday":
        print("weekend starting")
    case "saturady":
        print("weekend started")
    case "sunday":
        print("weekend comeing to end")
    case _:
        print("continue of their work,\nnext week started")
        
        
time = int(input("Num:"))
is_hungery = True
match time:
    case 8:
        print("Brakefast")
    case 14 | 13:
        print("Lunch")
    case 18 if is_hungery:
        print("Take Snacks")
    case 20:
        print("Dinner")
    case _:
        print("Do Your Work")