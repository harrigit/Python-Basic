#example creating Set
myset={"HAris","Khan","Niazi"}
print(myset) #{'Niazi', 'HAris', 'Khan'}
#that why we called set as a unordered List

#Example Acessing Index or Values
for i in myset:
    print(i)
print("Khan" in myset) #True
# Adding ANd Updating in SEt
myset.add("HAshir")
print(myset)
myset.update(["HAshir Niazi","Zarar Niazi"])
print(myset)