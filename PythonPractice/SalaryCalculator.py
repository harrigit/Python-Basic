
print("")
print("---------------------------------------------------------------------")
print("                   Hello!Welcome to Salary Calculator"                )
print("---------------------------------------------------------------------")
print("")
Slaray=int(input("Enter Employee Salary of Month: "))
WorkingHours=int(input("Enter total working Hours In a Month: "))
print("")
if WorkingHours>176:
    print("Aba Sae Dal working Hours and Must Not greater Than 176 ")
elif Slaray==110000:
    perday=Slaray/22
    perhour=perday/8
    Total=WorkingHours*perhour
    print("Total Salary Afer calculation is= ",Total)
elif Slaray==40000:
    perday=Slaray/22
    perhour=perday/8
    Total=WorkingHours*perhour
    print("Total Salary Afer calculation is= ",Total)
else:
    print("Abhi baki employees ki Salary ka mujha Ni pta ")
 
print("")  
print("---------------------The End----------------------")
print("")