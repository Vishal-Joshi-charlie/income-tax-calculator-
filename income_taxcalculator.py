#income tax calculation

#input5 from User
income=int(input("Enter your income="))
tax=0
cess=0
#income does not exceed Rs.2,50,000/-
if (income<=250000):
    print("No need to pay tax")
    tax=0
#income between Rs.2,50,000/- to Rs.5,00,000/-
elif (income>250000 and income<=500000):
    tax=income*0.05
#income between Rs.5,00,000/- to Rs.10,00,000/-
elif (income>500000 and income<=1000000):
        tax=income*0.2
#income exceed Rs.10,00,000/-
else:
    tax=income*0.3
cess=income*0.04
ttax=tax+cess
famount=income+ttax
print("Income Tax=",tax)
print("Health and Educational Cess=",cess)
print("Total Tax=",ttax)
print("Final Amount to pay=",famount)
