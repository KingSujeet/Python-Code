print("************************ Number Division Test **********************************")
print(" ")
print(" ")

i=int(input("Enter the first value: "))
j=int(input("Enter the second value: "))
try :
    print(i/j)
except ZeroDivisionError:
    print("ERROR!!! --> You cannot divide any number by zero (second value should not be Zero) ")
