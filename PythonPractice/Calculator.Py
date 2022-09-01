a = '+'
b = '-'
c = "x"
d = "/"

Number_1 = int(input("Enter First Number:"))
Number_2 = int(input("Enter Second Number:"))
print()
print("Enter Expression From Following: +  ,  -  ,  x  ,    /")
print()
Expression = str(input("what you want?Enter Please!   "))
print()
if Expression == a:
    print("Answer Is ", (Number_1+Number_2))
elif Expression == b:
    print("Answer Is ", (Number_1-Number_2))
elif Expression == c:
    print("Answer Is ", (Number_1*Number_2))
elif Expression == d:
    print("Answer Is ", (Number_1/Number_2))
else:
    print("Seda Expression dal panga na la smjha ho na!")
print(" ")
print("-----------------End-------------------")
print()
