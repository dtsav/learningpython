# number is called cool if it is even and between 10 and 30
num = input("enter number: ")
num = int(num)
if num%2 == 0:
    if num>= 10 and num<=30:
        print(num, "is cool")
    else:
        print(num, "is half cool, its not between 10 and 30")
else:
    print(num, "is definitely not cool")