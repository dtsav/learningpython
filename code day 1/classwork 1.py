# we ask user for his name, surname, and grade
# we check if the user's name contains the letter "I" two or more times: https://www.w3schools.com/python/ref_string_count.asp
# we check if the user's surname ends with "va" b = "Hello, World!, print(b[len(b)-2:len(b)])
# we check if the grade is more than 80

name = input("enter your first name:")
surname = input("enter your surname: ")
grade = int(input("enter your grade percentage(do not include percent): "))

if name.count("i") >= 2:
    if surname[len(surname)-2:len(surname)] == "va":
        if grade > 80:
            print("congrats")
        else: 
            print("almost there")
    else: 
        print("sorry, not your lucky day")
else:
    print("not even close")

