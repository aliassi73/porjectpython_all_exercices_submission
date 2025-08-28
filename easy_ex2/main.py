while True:
    usernum = input("give me a number:")
    try:
        number=int(usernum)
    except ValueError:
        print("try again wrong number!!")
        continue
    if number %2 == 0:
        print( + number + " is even")
    else:
        print( + number + " is odd")
    break          