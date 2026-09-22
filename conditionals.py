# GB, Conditionals Notes

# Boolean -> a data type that is true of false

# Conditional

# if -> starts a conditional : "time < 1200" ex. of boolean statement
    # whenever code ends w/ : you indent next line of code, indent only happens when condition above is True

# else -> end of conditional -- catch-all
    # if the above conditional is False, this will happen

# Comparison operators
    # < : less than
    # > : greater than
    # == : equal to
    # <= : less than or equal to
    # >= : greater than or equal to
    # != : not equal

# Logical operators
    # and : both conditions True
    # or : one condition True
    # not : checks if False  

time = 1417
day = "Tuesday"

if time < 1200 and time > 500:
    print("Good Morning!")
elif time < 1700:
     print("Good Afternoon!")
    if day != 'Saturday' or day != 'Sunday':
        print("How has school been?")
elif time < 2000:
    print("Good Evening!")
else:
    print("Good night.")

print("Code is done.")
