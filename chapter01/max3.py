# input 3 integers and find max

print("Input max among 3 integers")
a = int(input("Input integer a:"))
b = int(input("Input integer b:"))
c = int(input("Input integer c:"))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print(f"max is {maximum}")